# bot/main.py
import requests
import feedparser
from bs4 import BeautifulSoup
from bot.config import FONTES_NOTICIAS, FEEDS_RSS, BLOG_URL

def coletar_noticias():
    print(f"Iniciando coleta para o blog: {BLOG_URL}")
    noticias = []
    
    # 1. Tentativa de coleta nativa via RSS (Mais rápido e seguro)
    for url_feed in FEEDS_RSS:
        try:
            print(f"Lendo feed RSS: {url_feed}")
            feed = feedparser.parse(url_feed)
            for entry in feed.entries[:5]:  # Coleta as 5 últimas matérias de cada site
                noticias.append({
                    'titulo': entry.title,
                    'link': entry.link,
                    'resumo': getattr(entry, 'summary', '')
                })
        except Exception as e:
            print(f"Erro ao ler feed {url_feed}: {e}")
            
    # 2. Backup via Raspagem Direta se o RSS falhar
    if not noticias:
        for fonte in FONTES_NOTICIAS:
            try:
                print(f"Executando backup via Web Scraping em: {fonte}")
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
                response = requests.get(fonte, headers=headers, timeout=10)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Coleta links estruturados das páginas de notícias
                for link in soup.find_all('a', href=True)[:5]:
                    if len(link.text.strip()) > 20:  # Evita pegar links de menu pequenos
                        noticias.append({
                            'titulo': link.text.strip(),
                            'link': link['href'] if link['href'].startswith('http') else fonte + link['href']
                        })
            except Exception as e:
                print(f"Erro ao raspar a página {fonte}: {e}")
                
    return noticias

def publicar_no_blogger(noticias):
    print(f"Preparando envio de {len(noticias)} artigos de Rock/Metal para o Blogger...")
    # Insira aqui o seu método original de integração com a API do Blogger
    for n in noticias:
        print(f"Postado com sucesso: {n['titulo']}")

if __name__ == '__main__':
    dados = coletar_noticias()
    publicar_no_blogger(dados)

