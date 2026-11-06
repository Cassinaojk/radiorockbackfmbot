import os, re, json, requests, time, random, io, contextlib, unicodedata, warnings
import builtins
from datetime import datetime, date, timezone, timedelta

_VERBOSE_LOG = os.getenv("VERBOSE_LOG", "false").lower() in ("1", "true", "yes", "sim")
_original_print = builtins.print

def print(*args, **kwargs):
    if _VERBOSE_LOG:
        return _original_print(*args, **kwargs)

    message = " ".join(str(a) for a in args).strip()
    important = (
        message.startswith("RÁDIO ROCKBACK FM - ROBÔ")
        or message.startswith("VERSÃO ")
        or message.startswith("Posts existentes verificados:")
        or message.startswith("✓ Publicada:")
        or message.startswith("✓ Imagem:")
        or message.startswith("RESULTADO")
        or message.startswith("Publicações:")
        or message.startswith("Ignoradas:")
        or message.startswith("Falhas:")
        or message.startswith("⚠ Duplicata de assunto:")
        or message.startswith("⚠ Notícia antiga:")
        or message.startswith("⚠ Limite diário:")
        or message.startswith("Erro:")
        or message.startswith("Fontes encontradas:")
        or message.startswith("Puladas:")
        or message.startswith("Novas matérias")
        or message.startswith("MAX_AGE_DAYS")
    )
    if important:
        return _original_print(*args, **kwargs)

from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
from urllib.parse import urlparse, urljoin, quote
from google import genai
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

print("RÁDIO ROCKBACK FM - ROBÔ DE NOTÍCIAS 3.2 (Filtro de Imagens + IA 3.5 + Debug de Fontes)")

BLOGGER_BLOG_ID = os.environ["BLOGGER_BLOG_ID"]
GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]
GOOGLE_CLIENT_SECRET = os.environ["GOOGLE_CLIENT_SECRET"]
BLOGGER_REFRESH_TOKEN = os.environ["BLOGGER_REFRESH_TOKEN"]
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

# ===== SEO =====
BLOG_NAME = os.getenv("BLOG_NAME", "Rádio RockBack FM").strip() or "Rádio RockBack FM"
BLOG_HOME_URL = os.getenv("BLOG_HOME_URL", "https://radiorockbackfm.blogspot.com").strip().rstrip("/")
BLOG_LOCALE = os.getenv("BLOG_LOCALE", "pt_BR").strip() or "pt_BR"
BLOG_TWITTER = os.getenv("BLOG_TWITTER", "").strip()
SEO_TITLE_SUFFIX = os.getenv("SEO_TITLE_SUFFIX", f" | {BLOG_NAME}").strip()
SEO_DESCRIPTION_MAX = int(os.getenv("SEO_DESCRIPTION_MAX", "160"))
SEO_KEYWORDS_MAX = int(os.getenv("SEO_KEYWORDS_MAX", "12"))

# Limites
MAX_POSTS_PER_RUN = int(os.getenv("MAX_POSTS_PER_RUN", "1"))
MAX_GEMINI_TEXT_CALLS_PER_RUN = int(os.getenv("MAX_GEMINI_TEXT_CALLS_PER_RUN", "6"))
GEMINI_MAX_RETRIES = 3
GEMINI_RETRY_BASE_SECONDS = 4
MAX_LINKS_PER_SOURCE = 120

# Filtro de data flexível (Hoje + 3 dias anteriores)
MAX_AGE_DAYS = int(os.getenv("MAX_AGE_DAYS", "4")) 
MIN_SOURCE_CHARS = 250
MIN_SOURCE_PARAGRAPHS = 1
TIMEOUT = 25

# Modelos de IA Atualizados
GEMINI_MODEL_TEXT = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")
GEMINI_FALLBACK_MODEL = os.getenv("GEMINI_FALLBACK_MODEL", "gemini-3.5-flash-lite")
GEMINI_API_KEY_2 = os.getenv("GEMINI_API_KEY_2", "").strip()
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "").strip()
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192").strip()
MISTRAL_MODEL = os.getenv("MISTRAL_MODEL", "mistral-small-latest").strip()
AI_PROVIDER_TIMEOUT = int(os.getenv("AI_PROVIDER_TIMEOUT", "90"))

# ===== Filtros =====
TITLE_BLOCK_TERMS = (
    "atualizações recentes", "atualizacoes recentes", "últimas atualizações", "ultimas atualizacoes",
    "novidades da", "novidades do", "extreme sound records", "sound records",
    "nossa equipe", "nossa redação", "nossa redacao", "sobre nós", "sobre nos", "quem somos",
    "contato", "fale conosco", "política de privacidade", "politica de privacidade",
    "termos de uso", "anuncie", "publicidade", "parceria", "parcerias",
    "comunicado", "comunicados", "expediente", "nota da redação", "nota da redacao",
    "retratação", "retratacao", "agradecimento", "agradecimentos",
    "feliz natal", "feliz ano novo", "boas festas", "boas férias",
)

ROCK_STRONG_TERMS = (
    "rock", "metal", "heavy metal", "hard rock", "punk", "grunge", "indie", "alternativo",
    "progressivo", "glam", "new metal", "classic rock", "album", "single", "turnê", "show",
    "festival", "guitarra", "bateria", "baixo", "vocalista", "banda", "disco", "lançamento",
    "videoclipe", "clipe", "turnê mundial", "line-up", "rock'n'roll", "rock and roll",
    "headbanger", "mosh", "palco", "metallica", "iron maiden", "guns n' roses", "nirvana",
    "ac/dc", "led zeppelin", "pink floyd", "queen", "ozzy", "black sabbath", "slipknot",
    "korn", "system of a down", "evanescence", "audioslave", "pearl jam", "soundgarden",
    "alice in chains", "foo fighters", "red hot chili peppers", "linkin park", "green day",
    "offspring",
)
ROCK_SUPPORT_TERMS = (
    "cantor", "cantora", "artista", "banda", "dupla", "musico", "musica", "musical",
    "musicista", "gravadora", "compositor", "compositora", "composicao", "instrumental",
    "vocal", "voz", "repertorio", "hit", "producao musical", "produtor musical",
    "guitarrista", "baixista", "baterista", "tecladista",
)

# Imagens a serem ignoradas (logos genéricas dos sites de origem)
BLOCKED_IMAGES = (
    "https://whiplash.net/imagens/whip_thumb_512.png",
    "https://www.rocknoticias.com.br/site/assets/img/og-image.png"
)

def _rock_norm(value):
    value = unicodedata.normalize("NFKD", str(value or ""))
    value = "".join(c for c in value if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", value.lower()).strip()

def is_rock_related(article=None, generated=None, raw_text=""):
    article = article or {}
    generated = generated or {}
    parts = [article.get("title", ""), article.get("text", ""), generated.get("titulo", ""), generated.get("resumo", ""), generated.get("materia", ""), raw_text]
    combined = _rock_norm(" ".join(str(x or "") for x in parts))
    title = _rock_norm(article.get("title", "") or generated.get("titulo", ""))
    if not combined: return False
    if any(term in title for term in ROCK_STRONG_TERMS): return True
    strong_hits = sum(1 for term in ROCK_STRONG_TERMS if term in combined)
    support_hits = sum(1 for term in ROCK_SUPPORT_TERMS if term in combined)
    if strong_hits >= 1 and support_hits >= 1: return True
    if strong_hits >= 2: return True
    return False

def quick_rock_prefilter(article):
    title = _rock_norm(article.get("title", ""))
    if any(term in title for term in TITLE_BLOCK_TERMS): return False, "post institucional/genérico"
    head = _rock_norm(article.get("text", "")[:400])
    combined = f"{title} {head}"
    if any(t in title for t in ROCK_STRONG_TERMS): return True, ""
    strong = sum(1 for t in ROCK_STRONG_TERMS if t in combined)
    support = sum(1 for t in ROCK_SUPPORT_TERMS if t in combined)
    if strong >= 1 and support >= 1: return True, ""
    return False, "sem termos de rock/metal fortes"

SOURCES = [
    {"nome": "Rock Notícias", "url": "https://www.rocknoticias.com.br/", "feeds": ["https://www.rocknoticias.com.br/feed/"]},
    {"nome": "Whiplash.net", "url": "https://whiplash.net/", "feeds": ["https://whiplash.net/feed/", "https://whiplash.net/rss/"]},
]

BAD_PATHS = ("/category/","/tag/","/author/","/page/","/search/","/feed/","/wp-json/","/comments/","/sobre","/contato","/contact","/politica","/privacidade","/privacy","/anuncie","/publicidade","/advertising","/login","/cadastro","/register","/sitemap","/robots.txt")
SHARE_DOMAINS = ("pinterest.","reddit.com/submit","facebook.com/sharer","twitter.com/intent","x.com/intent","whatsapp.com/","t.me/share","linkedin.com/share")
VIDEO_HOSTS = ("youtube.com/embed/","youtube.com/watch","youtube-nocookie.com/embed/","youtu.be/","player.vimeo.com","vimeo.com/video","facebook.com/plugins/video","web.facebook.com/plugins/video","instagram.com/p/","instagram.com/reel/","instagram.com/tv/","dailymotion.com/embed","twitch.tv/","streamable.com/e/","rumble.com/embed")

s = requests.Session()
s.headers.update({"User-Agent": "Mozilla/5.0 (compatible; RockBackFMBot/3.2)"})

gemini_calls = 0
gemini_quota_hit = False
_ai_config_logged = False

# ===== IMAGENS PADRÃO =====
IMAGENS_PADRAO = [f"https://raw.githubusercontent.com/Cassinaojk/radiorockbackfmbot/main/bot/imagens/Imagens%20Rock%20Flashback%20({i}).png" for i in range(1, 11)]
COUNTER_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image_counter.txt")

def ler_contador_imagem():
    try:
        with open(COUNTER_FILE, "r") as f:
            valor = int(f.read().strip())
            if valor < 1 or valor > len(IMAGENS_PADRAO): return 1
            return valor
    except Exception: return 1

def salvar_contador_imagem(valor):
    try:
        with open(COUNTER_FILE, "w") as f: f.write(str(valor))
    except Exception as e: print(f"⚠ Imagem: erro ao salvar contador: {e}")

# ===== FUNÇÕES BÁSICAS =====
def normalize_url(u):
    if not u: return ""
    return u.strip().split("#")[0].rstrip("/")

def bad_url(u):
    u = normalize_url(u).lower()
    if not u.startswith(("http://", "https://")): return True
    if any(x in u for x in SHARE_DOMAINS): return True
    path = urlparse(u).path
    if any(x in path for x in BAD_PATHS): return True
    if re.search(r"\.(pdf|jpg|jpeg|png|gif|webp|svg|xml|zip)$", path): return True
    return False

def soup(url, xml=False):
    try:
        r = s.get(url, timeout=TIMEOUT)
        if r.status_code != 200: return None
        if xml:
            try: return BeautifulSoup(r.text, "xml")
            except Exception: pass
        return BeautifulSoup(r.text, "html.parser")
    except Exception: return None

def date_parse(v):
    if not v: return None
    value = str(v).strip()
    formats = ("%Y-%m-%dT%H:%M:%S%z","%Y-%m-%dT%H:%M:%S.%f%z","%Y-%m-%dT%H:%M:%S","%Y-%m-%d","%d/%m/%Y")
    for f in formats:
        try:
            d = datetime.strptime(value[:32], f)
            return d.replace(tzinfo=None) if d.tzinfo else d
        except Exception: pass
    return None

def article_date(x):
    for sel in ('meta[property="article:published_time"]','meta[property="og:published_time"]','meta[name="date"]','meta[name="publish_date"]','meta[itemprop="datePublished"]'):
        n = x.select_one(sel)
        if n:
            d = date_parse(n.get("content",""))
            if d: return d
    for sc in x.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(sc.string or sc.get_text())
            items = data if isinstance(data, list) else [data]
            for item in items:
                if not isinstance(item, dict): continue
                if isinstance(item.get("@graph"), list):
                    for g in item["@graph"]:
                        if isinstance(g, dict):
                            d = date_parse(g.get("datePublished"))
                            if d: return d
                d = date_parse(item.get("datePublished"))
                if d: return d
        except Exception: pass
    for sel in ("time.entry-date","time.published","time",".entry-date",".posted-on"):
        n = x.select_one(sel)
        if n:
            d = date_parse(n.get("datetime") or n.get_text(" ", strip=True))
            if d: return d
    return None

def image_original(x):
    candidates = []
    for sel in ('meta[property="og:image"]','meta[property="og:image:secure_url"]','meta[name="twitter:image"]','meta[name="twitter:image:src"]','meta[itemprop="image"]'):
        n = x.select_one(sel)
        if n:
            u = (n.get("content") or "").strip()
            if u.startswith("//"): u = "https:" + u
            if u.startswith(("http://", "https://")): 
                candidates.append(u)

    for u in candidates:
        if u not in BLOCKED_IMAGES:
            return u
            
    return ""

def videos(x):
    BLOCK = ("doubleclick.net","googlesyndication.com","googleadservices.com","adservice.google","taboola.com","outbrain.com","criteo.","pubmatic.","rubiconproject.","adnxs.com","amazon-adsystem.","facebook.com/plugins/post","instagram.com/embed.js")
    out = []
    for n in x.find_all("iframe"):
        u = (n.get("src") or n.get("data-src") or "").strip()
        if u.startswith("//"): u = "https:" + u
        if not u.startswith(("http://", "https://")): continue
        ul = u.lower()
        if any(b in ul for b in BLOCK): continue
        if not any(h in ul for h in VIDEO_HOSTS): continue
        st = (n.get("style") or "").lower().replace(" ","")
        if any(z in st for z in ("display:none","visibility:hidden","opacity:0","width:0","height:0")): continue
        try:
            w = int(re.sub(r"[^\d]","",(n.get("width") or "") or "0"))
            h = int(re.sub(r"[^\d]","",(n.get("height") or "") or "0"))
            if (w and w < 100) or (h and h < 100): continue
        except Exception: pass
        if n.find_parent(style=re.compile(r"display\s*:\s*none|visibility\s*:\s*hidden", re.I)): continue
        if u not in out: out.append(u)
    return out[:3]

# ===== ARTIGO =====
def get_article(url):
    x = soup(url)
    if not x: return None
    n = x.find("h1") or x.find("title")
    title = re.sub(r"\s+", " ", n.get_text(" ", strip=True) if n else "").strip()
    if not title: return None

    title_norm = _rock_norm(title)
    if any(term in title_norm for term in TITLE_BLOCK_TERMS): return None
    if title.lower() in {"lançamentos","notícias","noticias","home","início","inicio","últimas notícias","ultimas noticias","404"}: return None

    d = article_date(x)
    if d:
        age = (datetime.now() - d).total_seconds() / 86400
        if age > MAX_AGE_DAYS:
            print(f"⚠ Notícia antiga (publicada em {d.strftime('%d/%m/%Y')}). Pulando.")
            return None
    else:
        print("Data não identificada. Aceitando para análise.")
        d = datetime.now()

    img = image_original(x) or ""
    box = x.find("article") or x.find("main") or x
    paragraphs = []
    for p in box.find_all("p"):
        t = re.sub(r"\s+", " ", p.get_text(" ", strip=True))
        if len(t) >= 35: paragraphs.append(t)
    text = "\n\n".join(paragraphs)
    
    if len(text) < MIN_SOURCE_CHARS or len(paragraphs) < MIN_SOURCE_PARAGRAPHS: return None
    
    vv = videos(x)
    inline_imgs = [{"url": img, "after_paragraph": 2, "is_main": True}] if img else []
    return {"url": normalize_url(url), "title": title, "date": d, "image": img, "text": text[:16000], "videos": vv, "inline_images": inline_imgs}

def links(source):
    out = []; seen = set()
    source_host = urlparse(source["url"]).netloc.lower()
    
    def host_matches(u):
        h = urlparse(u).netloc.lower()
        if h == source_host: return True
        if h.endswith("." + source_host): return True
        hn = h.replace("www.","",1); sn = source_host.replace("www.","",1)
        return hn == sn or hn.endswith("." + sn)
        
    rss_found = 0
    for feed in source["feeds"]:
        x = soup(feed, True)
        if not x: continue
        for item in x.find_all(["item", "entry"]):
            n = item.find("link")
            if not n: continue
            u = normalize_url(n.get("href") or n.get_text(strip=True) or "")
            if not u or bad_url(u) or not host_matches(u): continue
            if u not in seen: seen.add(u); out.append(u); rss_found += 1
            
    html_found = 0
    x = soup(source["url"])
    if x:
        for a in x.find_all("a", href=True):
            u = normalize_url(urljoin(source["url"], a["href"]))
            if bad_url(u) or not host_matches(u): continue
            path = urlparse(u).path.strip("/")
            if path.count("/") >= 1 and len(path) > 10:
                if u not in seen: seen.add(u); out.append(u); html_found += 1
                
    print(f"Links em {source['nome']}: {len(out)} (RSS: {rss_found}, HTML: {html_found})")
    return out[:MAX_LINKS_PER_SOURCE]

def blogger():
    creds = Credentials(None, refresh_token=BLOGGER_REFRESH_TOKEN, token_uri="https://oauth2.googleapis.com/token",
                        client_id=GOOGLE_CLIENT_ID, client_secret=GOOGLE_CLIENT_SECRET,
                        scopes=["https://www.googleapis.com/auth/blogger"])
    return build("blogger", "v3", credentials=creds, cache_discovery=False)

# ===== BUSCA NO BLOGGER E ANTI-DUPLICIDADE =====
def get_all_existing_data(api):
    blog_urls, source_urls = set(), set()
    existing_posts = []
    token = None
    try:
        while True:
            kw = {"blogId": BLOGGER_BLOG_ID, "maxResults": 500, "fetchBodies": True}
            if token: kw["pageToken"] = token
            data = api.posts().list(**kw).execute()
            for post in data.get("items", []):
                post_url = normalize_url(post.get("url",""))
                if post_url: blog_urls.add(post_url)
                
                content = post.get("content","") or ""
                title = post.get("title","") or ""
                
                for m in re.findall(r'href=["\'](https?://[^"\']+)["\']', content, flags=re.I):
                    source_urls.add(normalize_url(m))
                for m in re.findall(r'RADIO_ROCKBACK_FM_SOURCE_URL:\s*(https?://[^\s]+?)\s*-->', content, flags=re.I):
                    source_urls.add(normalize_url(m))
                
                clean = re.sub(r"\s+", " ", BeautifulSoup(content, "html.parser").get_text(" ", strip=True)).strip()
                if clean and len(clean) > 100:
                    existing_posts.append({"title": title, "text": clean})
            token = data.get("nextPageToken")
            if not token: break
    except Exception as e: print("Erro ao consultar Blogger:", e)
    print(f"Posts existentes verificados: {len(existing_posts)}")
    return blog_urls, source_urls, existing_posts

def extract_meaningful_words(text):
    norm = _rock_norm(text)
    words = set(re.findall(r"\b[a-z]{4,}\b", norm))
    stopwords = {"a","o","e","de","da","do","das","dos","em","no","na","que","se","para","por","com","um","uma","mais","como","sobre","mas","sua","seu","pelo","pela","guia","pratico","completo","essenciais","ferramentas","tutorial"}
    return words - stopwords

def check_content_duplicate(article, existing_posts):
    new_title_words = extract_meaningful_words(article["title"])
    new_text_words = extract_meaningful_words(article["text"])
    for old in existing_posts:
        old_title_words = extract_meaningful_words(old["title"])
        old_text_words = extract_meaningful_words(old["text"])
        
        title_overlap = new_title_words & old_title_words
        if len(title_overlap) >= 2:
            return True, f"Título similar: {old['title'][:50]}"
            
        if new_text_words and old_text_words:
            intersection = new_text_words & old_text_words
            union = new_text_words | old_text_words
            jaccard = len(intersection) / len(union)
            if jaccard > 0.40:
                return True, f"Conteúdo similar ({jaccard*100:.0f}%): {old['title'][:50]}"
    return False, ""

# ===== CHECAGEM DE LIMITE DIÁRIO =====
def check_published_today(api):
    try:
        now_utc = datetime.now(timezone.utc)
        br_tz = timezone(timedelta(hours=-3))
        today_br = now_utc.astimezone(br_tz).strftime('%Y-%m-%d')
        
        response = api.posts().list(
            blogId=BLOGGER_BLOG_ID,
            maxResults=10,
            fetchBodies=False,
            orderBy="PUBLISHED"
        ).execute()
        
        for post in response.get("items", []):
            pub_date = post.get("published", "")
            if pub_date.startswith(today_br):
                return True, post.get("title", "")
    except Exception as e:
        print(f"⚠ Aviso: erro ao checar limite diário: {e}")
    return False, ""

# ===== IA =====
def is_transient_gemini_error(exc):
    m = str(exc).upper()
    return any(c in m for c in ("503","UNAVAILABLE","429","RESOURCE_EXHAUSTED","500","502","504","TIMEOUT"))

def gemini_request(client, model, prompt):
    last = None
    for attempt in range(1, GEMINI_MAX_RETRIES + 1):
        try:
            with contextlib.redirect_stderr(io.StringIO()):
                return client.models.generate_content(model=model, contents=prompt, config={"response_mime_type": "application/json"})
        except Exception as e:
            last = e; m = str(e).upper()
            if "429" in m or "RESOURCE_EXHAUSTED" in m: raise
            if not is_transient_gemini_error(e) or attempt >= GEMINI_MAX_RETRIES: raise
            time.sleep(GEMINI_RETRY_BASE_SECONDS * (2 ** (attempt-1)) + random.uniform(0,2))
    raise last

def norm_words(text):
    text = unicodedata.normalize("NFKD", text or "")
    text = "".join(c for c in text if not unicodedata.combining(c)).lower()
    return re.findall(r"[a-z0-9]+", text)

def originality_check(source_text, generated_text):
    src = norm_words(source_text); out = norm_words(generated_text)
    if len(out) < 100: return False, "matéria curta"
    src8 = {" ".join(src[i:i+8]) for i in range(max(0, len(src)-7))}
    out8 = {" ".join(out[i:i+8]) for i in range(max(0, len(out)-7))}
    overlap = len(src8 & out8) / max(1, min(len(src8), len(out8)))
    if overlap > 0.12: return False, f"sobreposição ({overlap:.3f})"
    return True, "OK"

def _provider_text(provider, response):
    if provider.startswith("gemini"): return (getattr(response, "text", None) or "").strip()
    ch = response.get("choices") or []
    if not ch: return ""
    msg = ch[0].get("message") or {}
    c = msg.get("content") or ""
    if isinstance(c, list): c = "".join(str(i.get("text") or "") for i in c if isinstance(i, dict) and i.get("type") == "text")
    return str(c).strip()

def _provider_request(provider, api_key, model, prompt):
    if provider.startswith("gemini"):
        return gemini_request(genai.Client(api_key=api_key), model, prompt)
    endpoint = {"groq":"https://api.groq.com/openai/v1/chat/completions","mistral":"https://api.mistral.ai/v1/chat/completions"}.get(provider)
    payload = {"model": model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.2, "max_tokens": 5000, "response_format": {"type": "json_object"}}
    if provider == "groq": payload["include_reasoning"] = False
    r = requests.post(endpoint, headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}, json=payload, timeout=90)
    if r.status_code >= 400: raise RuntimeError(f"HTTP_{r.status_code}")
    return r.json()

def gemini(article, client=None):
    global gemini_calls, gemini_quota_hit, _ai_config_logged
    if gemini_calls >= MAX_GEMINI_TEXT_CALLS_PER_RUN: return None
    providers = []
    if GEMINI_API_KEY: providers.append(("gemini", GEMINI_API_KEY, GEMINI_MODEL_TEXT))
    if GEMINI_API_KEY_2: providers.append(("gemini-2", GEMINI_API_KEY_2, GEMINI_FALLBACK_MODEL))
    if GROQ_API_KEY: providers.append(("groq", GROQ_API_KEY, GROQ_MODEL))
    if MISTRAL_API_KEY: providers.append(("mistral", MISTRAL_API_KEY, MISTRAL_MODEL))
    if not providers: return None

    prompt = f"""
Você é jornalista da Rádio RockBack FM. Escreva uma matéria NOVA e ORIGINAL, em pt-BR.
REGRAS:
1. Use SOMENTE fatos do texto-fonte. Não invente.
2. A matéria deve ter 700 a 1200 palavras.
3. Título novo e jornalístico; resumo de 2-3 frases.
4. Se for sobre assunto alheio a rock/metal, marque publicar=false.
5. Retorne SOMENTE JSON válido.

FORMATO:
{{"publicar":true,"titulo":"...","resumo":"...","materia":"...","assunto_principal":"...","palavras_chave":["..."],"categoria_seo":"..."}}

TÍTULO ORIGINAL: {article['title']}
FONTE: {article['url']}
TEXTO-FONTE:
{article['text']}
"""

    exhausted = set(); last_reason = "erro"
    for pass_index in range(2):
        pp = prompt if pass_index == 0 else prompt + "\n\nATENÇÃO: reescreva totalmente."
        for provider, api_key, model in providers:
            if gemini_calls >= MAX_GEMINI_TEXT_CALLS_PER_RUN: break
            if provider in exhausted: continue
            try:
                print(f"IA: tentando {provider} / {model}...")
                resp = _provider_request(provider, api_key, model, pp)
                gemini_calls += 1
                raw = _provider_text(provider, resp)
                if not raw: last_reason = "vazia"; continue
                raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw).strip()
                data = json.loads(raw)
                if data.get("publicar") is False: last_reason = "sem info"; continue
                titulo = str(data.get("titulo","")).strip()
                resumo = str(data.get("resumo","")).strip()
                materia = str(data.get("materia","")).strip()
                if not titulo or not resumo or len(materia) < 700: last_reason = "inválida"; continue
                ok, reason = originality_check(article["text"], titulo + "\n" + resumo + "\n" + materia)
                if not ok: last_reason = "originalidade"; continue
                palavras = data.get("palavras_chave", []) or []
                if isinstance(palavras, str): palavras = [p.strip() for p in palavras.split(",") if p.strip()]
                return {"publicar": True, "titulo": titulo, "resumo": resumo, "materia": materia,
                        "assunto_principal": str(data.get("assunto_principal","")).strip(),
                        "palavras_chave": palavras[:SEO_KEYWORDS_MAX],
                        "categoria_seo": str(data.get("categoria_seo","")).strip()}
            except Exception as exc:
                if any(x in str(exc).upper() for x in ("429","RESOURCE_EXHAUSTED","QUOTA","RATE LIMIT")): exhausted.add(provider); last_reason = "quota"
                else: last_reason = "erro"
    if last_reason == "quota": gemini_quota_hit = True
    return None

# ===== SEO E HTML =====
def _truncate(text, limit):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    if len(text) <= limit: return text
    cut = text[:limit]; sp = cut.rfind(" ")
    if sp > limit * 0.6: cut = cut[:sp]
    return cut.rstrip(" ,;:-") + "..."

def build_seo_payload(article, generated, final_image="", image_origin=""):
    tb = str(generated.get("titulo","")).strip()
    resumo = str(generated.get("resumo","")).strip()
    materia = str(generated.get("materia","")).strip()
    assunto = str(generated.get("assunto_principal","")).strip()
    cat = str(generated.get("categoria_seo","")).strip()
    palavras = list(generated.get("palavras_chave", []) or [])
    title = tb
    if SEO_TITLE_SUFFIX and not title.lower().endswith(SEO_TITLE_SUFFIX.lower()): title = f"{tb}{SEO_TITLE_SUFFIX}"
    description = _truncate(resumo or re.sub(r"\s+", " ", BeautifulSoup(materia, "html.parser").get_text(" ", strip=True))[:SEO_DESCRIPTION_MAX], SEO_DESCRIPTION_MAX)
    kw = []
    if assunto: kw.append(assunto)
    if cat: kw.append(cat)
    for p in palavras:
        p = str(p).strip()
        if p and p.lower() not in {k.lower() for k in kw}: kw.append(p)
    for fb in ("rock","heavy metal","notícias de rock", BLOG_NAME):
        if fb.lower() not in {k.lower() for k in kw}: kw.append(fb)
    keywords = ", ".join(kw[:SEO_KEYWORDS_MAX])
    labels = ["Notícias","Rádio RockBack FM"]
    if is_rock_related(article=article, generated=generated): labels.insert(1, "Rock")
    if cat and cat not in labels: labels.append(cat)
    if assunto and assunto not in labels and len(assunto) <= 40: labels.append(assunto)
    if article.get("date"): labels.append(str(article["date"].year))
    seen = set(); labels_final = []
    for l in labels:
        l = str(l).strip()
        if not l: continue
        k = l.lower()
        if k in seen: continue
        seen.add(k); labels_final.append(l)
    labels_final = labels_final[:10]
    image_url = final_image or article.get("image","")
    canonical = article.get("url","")
    published = (article.get("date") or datetime.now()).isoformat()
    date_modified = datetime.now().isoformat()
    schema = {"@context":"https://schema.org","@type":"NewsArticle","mainEntityOfPage":{"@type":"WebPage","@id":canonical},"headline":tb[:110],"description":description,"image":[image_url] if image_url else [],"datePublished":published,"dateModified":date_modified,"author":{"@type":"Organization","name":BLOG_NAME,"url":BLOG_HOME_URL},"publisher":{"@type":"Organization","name":BLOG_NAME,"url":BLOG_HOME_URL,"logo":{"@type":"ImageObject","url":image_url or f"{BLOG_HOME_URL}/favicon.ico"}},"articleSection":cat or "Rock","keywords":keywords,"inLanguage":"pt-BR","isAccessibleForFree":True,"url":canonical,"sourceOrganization":{"@type":"Organization","name":urlparse(canonical).netloc,"url":canonical}}
    breadcrumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Início","item":BLOG_HOME_URL},{"@type":"ListItem","position":2,"name":"Notícias","item":f"{BLOG_HOME_URL}/search/label/Not%C3%ADcias"},{"@type":"ListItem","position":3,"name":tb[:80],"item":canonical}]}
    st = title.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")
    sd = description.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")
    sk = keywords.replace("&","&amp;").replace('"',"&quot;")
    sc = canonical.replace("&","&amp;").replace('"',"&quot;")
    si = (image_url or "").replace("&","&amp;").replace('"',"&quot;")
    tw = f'<meta name="twitter:site" content="{BLOG_TWITTER}">' if BLOG_TWITTER else ""
    jla = json.dumps(schema, ensure_ascii=False); jlb = json.dumps(breadcrumb, ensure_ascii=False)
    html_head = f"""<!-- ===== SEO RÁDIO ROCKBACK FM ===== -->
<title>{st}</title>
<meta name="description" content="{sd}">
<meta name="keywords" content="{sk}">
<link rel="canonical" href="{sc}">
<meta property="og:type" content="article">
<meta property="og:title" content="{st}">
<meta property="og:description" content="{sd}">
<meta property="og:url" content="{sc}">
{f'<meta property="og:image" content="{si}">' if si else ''}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{st}">
<meta name="twitter:description" content="{sd}">
{f'<meta name="twitter:image" content="{si}">' if si else ''}
{tw}
<script type="application/ld+json">{jla}</script>
<script type="application/ld+json">{jlb}</script>
<!-- ===== FIM SEO ===== -->"""
    return {"title":title,"titulo_base":tb,"description":description,"keywords":keywords,"labels":labels_final,"canonical":canonical,"schema":schema,"breadcrumb":breadcrumb,"html_head":html_head,"source_url":article.get("url",""),"assunto":assunto,"categoria_seo":cat}

def _render_inline_image_html(img_url, alt_text):
    si = (img_url or "").replace("&","&amp;").replace('"',"&quot;")
    sa = (alt_text or "").replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")
    if not si: return ""
    return ('<p style="text-align:center;margin:24px 0;">'
            f'<img src="{si}" alt="{sa}" title="{sa}" '
            'style="max-width:100%;height:auto;border-radius:12px;'
            'box-shadow:0 4px 12px rgba(0,0,0,0.10);display:block;'
            'margin-left:auto;margin-right:auto;"></p>')

def html(article, generated, final_image="", image_origin="", seo=None):
    seo = seo or {}
    tb = seo.get("titulo_base") or generated.get("titulo","")
    st = tb.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")
    iu = final_image or article["image"]
    si = iu.replace("&","&amp;").replace('"',"&quot;")
    ss = article["url"].replace("&","&amp;").replace('"',"&quot;")
    head = seo.get("html_head","")
    content = []
    if head: content.append(head)
    content.extend([f'<p><strong>{generated["resumo"]}</strong></p>', f'<p><img src="{si}" alt="{st}" title="{st}" width="1200" height="630" style="max-width:100%;height:auto;border-radius:12px;"></p>'])
    paras = [p.strip() for p in re.split(r"\n+", generated["materia"]) if p.strip()]
    imgs = list(article.get("inline_images") or [])[:1]
    imgs.sort(key=lambda x: x.get("after_paragraph", 9999))
    parts = []; idx = 0; total = len(paras)
    for im in imgs:
        t = im.get("after_paragraph", 9999)
        try: t = int(t)
        except Exception: t = 9999
        t = max(0, min(t, total))
        while idx < t: parts.append(f"<p>{paras[idx]}</p>"); idx += 1
        r = _render_inline_image_html(im.get("url",""), tb)
        if r: parts.append(r)
    while idx < total: parts.append(f"<p>{paras[idx]}</p>"); idx += 1
    content.extend(parts)
    for vu in article["videos"]:
        content.append('<div style="margin:24px 0;"><div style="position:relative;width:100%;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:12px;">'
                       f'<iframe src="{vu}" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" frameborder="0" allowfullscreen loading="lazy"></iframe>'
                       '</div></div>')
    
    spotify_block = (
        '<div style="max-width:600px;margin:2rem auto;padding:0 1rem;">'
        '<h3 style="text-align:center;color:#1DB954;font-family:Arial,sans-serif;margin-bottom:1rem;">'
        '🎸 Top Rock — Rádio RockBack FM'
        '</h3>'
        '<iframe data-testid="embed-iframe" '
        'style="border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,0.15);" '
        'src="https://open.spotify.com/embed/playlist/2wf6Jmrz6N9aWE4C1d9TtX?utm_source=generator&theme=0&si=c5efcf246bab4f3b" '
        'width="100%" height="352" frameBorder="0" allowfullscreen="" '
        'allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" '
        'loading="lazy" title="Playlist Rock no Spotify"></iframe>'
        '<p style="text-align:center;margin-top:0.8rem;font-size:0.95rem;color:#666;font-family:Arial,sans-serif;">'
        'Ouça a seleção especial da <strong>Rádio RockBack FM</strong> 📻🎸'
        '</p></div>'
    )
    content.append(spotify_block)

    src_marker = f"<!-- RADIO_ROCKBACK_FM_SOURCE_URL: {ss} -->"
    img_marker = f"\n<!-- RADIO_ROCKBACK_FM_IMAGE_SOURCE: {image_origin} -->" if image_origin else ""
    seo_marker = f"\n<!-- RADIO_ROCKBACK_FM_SEO_DESCRIPTION: {seo.get('description','')[:300]} -->\n<!-- RADIO_ROCKBACK_FM_SEO_KEYWORDS: {seo.get('keywords','')[:300]} -->" if seo else ""
    return "\n".join(content) + "\n" + src_marker + img_marker + seo_marker

# ===== MAIN =====
def main():
    print("Fontes: Rock Notícias + Whiplash.net | Anti-Duplicidade Textual | Limite de 1 post por dia")
    print(f"MAX_AGE_DAYS configurado: {MAX_AGE_DAYS}")
    gen_client = genai.Client(api_key=GEMINI_API_KEY)
    api = blogger()
    
    # 1. TRAVA DIÁRIA: Verifica se já postou hoje
    already_published, last_title = check_published_today(api)
    if already_published:
        print(f"⚠ Limite diário: Já foi publicada uma matéria hoje («{last_title[:50]}»). O robô vai aguardar até amanhã.")
        print("RESULTADO")
        print("Publicações: 0")
        print("Ignoradas: 0")
        print("Falhas: 0")
        return

    # 2. Busca dados para anti-duplicidade
    old_blog_urls, old_source_urls, existing_posts = get_all_existing_data(api)

    candidates = []
    candidate_urls = set()
    source_counts = {}
    prefiltered = 0
    pre_dups = 0

    for source in SOURCES:
        sl = links(source)
        source_counts[source["nome"]] = len(sl)
        for url in sl:
            n = normalize_url(url)
            if n in candidate_urls or n in old_blog_urls or n in old_source_urls: continue
            art = get_article(n)
            if art:
                if not is_rock_related(article=art): prefiltered += 1; continue
                passed, reason = quick_rock_prefilter(art)
                if not passed:
                    prefiltered += 1
                    print(f"⚠ Pulada (pré-filtro): {art['title'][:70]} — {reason}")
                    continue

                # Verificação de duplicata Pré-IA
                is_dup_pre, dup_reason_pre = check_content_duplicate(art, existing_posts)
                if is_dup_pre:
                    pre_dups += 1
                    print(f"⚠ Duplicata de assunto (Pré-IA): «{art['title'][:60]}» — {dup_reason_pre}.")
                    continue

                candidate_urls.add(n); candidates.append(art)

    print(f"Fontes encontradas: {' | '.join(f'{k}: {v}' for k, v in source_counts.items())}")
    print(f"Puladas: {prefiltered + pre_dups}")
    if pre_dups: print(f"⚠ Duplicadas por conteúdo (pré-IA): {pre_dups}")

    candidates.sort(key=lambda a: a["date"] or datetime.min, reverse=True)
    print(f"Novas matérias de rock/metal: {len(candidates)}")

    published = 0; failed = 0; ignored = 0; post_dups = 0

    while candidates and published < MAX_POSTS_PER_RUN:
        art = candidates.pop(0)
        n = normalize_url(art["url"])
        if n in old_source_urls: ignored += 1; continue

        if gemini_calls >= MAX_GEMINI_TEXT_CALLS_PER_RUN: break

        gen = gemini(art, gen_client)
        if not gen:
            ignored += 1
            if gemini_quota_hit: break
            continue

        # Verificação de duplicata Pós-IA
        gen_art = {"title": gen.get("titulo", ""), "text": gen.get("materia", "")}
        is_dup_post, dup_reason_post = check_content_duplicate(gen_art, existing_posts)
        if is_dup_post:
            print(f"⚠ Duplicata de assunto (Pós-IA): «{gen.get('titulo','')[:60]}» — {dup_reason_post}.")
            post_dups += 1
            ignored += 1
            continue

        # Imagem Padrão
        contador = ler_contador_imagem()
        final_image = IMAGENS_PADRAO[contador - 1]
        image_origin = f"Imagem padrão do repositório (índice {contador}/10)"
        print(f"✓ Imagem: usando imagem {contador}/10 do repositório")

        seo = build_seo_payload(art, gen, final_image=final_image, image_origin=image_origin)
        print(f"✓ SEO: título = {seo['title'][:90]}")

        try:
            post_body = {"title": seo["title"].strip(), "content": html(art, gen, final_image=final_image, image_origin=image_origin, seo=seo), "labels": seo["labels"], "images": [{"url": final_image}]}
            try: post_body["customMetaData"] = seo["description"]
            except Exception: pass
            resp = api.posts().insert(blogId=BLOGGER_BLOG_ID, body=post_body, isDraft=False).execute()
            published += 1
            old_source_urls.add(n)
            existing_posts.append({"title": seo["title"], "text": gen.get("materia", "")})

            proximo = (contador % len(IMAGENS_PADRAO)) + 1
            salvar_contador_imagem(proximo)

            if resp.get("url"):
                old_blog_urls.add(normalize_url(resp["url"]))
                try:
                    new_url = resp["url"]
                    if new_url != seo["canonical"]:
                        upd = html(art, gen, final_image=final_image, image_origin=image_origin, seo={**seo, "canonical": new_url})
                        api.posts().patch(blogId=BLOGGER_BLOG_ID, postId=resp["id"], body={"content": upd}).execute()
                except Exception as e: print(f"⚠ SEO canonical: {e}")
            print(f"✓ Publicada: {seo['title'].strip()}")
            
            # Como a regra é 1 por dia, se publicou 1, encerra a execução
            break 
            
        except Exception as exc:
            failed += 1
            print(f"⚠ Blogger: falha ({str(exc)[:200]})")

    print("RESULTADO")
    print(f"Publicações: {published}")
    print(f"Ignoradas: {ignored}")
    print(f"Falhas: {failed}")
    if post_dups: print(f"⚠ Duplicadas detectadas após IA: {post_dups}")

print("VERSÃO 3.2 ATIVA: Limite de 1 post/dia | Anti-Duplicidade | Modelo IA 3.5 | Scraping")
main()
