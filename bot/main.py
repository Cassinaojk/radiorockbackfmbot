<?xml version="1.0" encoding="UTF-8" ?>
<!-- ============================================================ --><!-- TEMPLATE: RockBack RedLine                                   --><!-- Design: Dark / Vermelho - Blogger Layout Ready               --><!-- Player: Rádio RockBack FM (intacto)                          --><!-- + Barra de Pesquisa + Tradutor (PT/EN/ES)                    --><!-- + Setas de paginação em destaque vermelho                    --><!-- + Data + POR: Rádio RockBack FM em todas as postagens        --><!-- + Lançamentos do Rock: RSS automático (Max 10 itens)         --><!-- ============================================================ --><html xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
<head>
  <!-- Google tag (gtag.js) -->
<script async='async' src='https://www.googletagmanager.com/gtag/js?id=G-9JZP5W8063'/>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag(&#39;js&#39;, new Date());
  gtag(&#39;config&#39;, &#39;G-9JZP5W8063&#39;);
</script>

<meta content='width=device-width, initial-scale=1' name='viewport'/>
<meta charset='UTF-8'/>
<title><data:blog.pageTitle/></title>

<!-- ===== INCLUSÃO NATIVA DO BLOGGER PARA OPEN GRAPH E SEO ===== -->
<b:include data='blog' name='all-head-content'/>
<!-- ============================================================ -->

<b:if cond='data:blog.metaDescription'>
  <meta expr:content='data:blog.metaDescription' name='description'/>
</b:if>
<link href='https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&amp;family=Inter:wght@400;500;600;700&amp;display=swap' rel='stylesheet'/>
<b:skin><![CDATA[
/* ==========================================================
   RockBack RedLine — Stylesheet
   ========================================================== */
:root{
  --bg:#08080a;
  --bg-2:#0f0f12;
  --card:#141418;
  --card-2:#1a1a1f;
  --red:#e2202a;
  --red-2:#ff3a44;
  --red-dark:#a91620;
  --cream:#f0dfb4;
  --text:#f4f2ee;
  --text-2:#a8a5a0;
  --border-red:rgba(226,32,42,.35);
  --border-soft:rgba(240,223,180,.08);
  --font-title:'Oswald','Arial Narrow',sans-serif;
  --font-body:'Inter',-apple-system,Segoe UI,Roboto,sans-serif;
  --max:1240px;
  --radius:14px;
}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{
  margin:0;
  background:var(--bg);
  color:var(--text);
  font-family:var(--font-body);
  font-size:15px;
  line-height:1.65;
  overflow-x:hidden;
  padding-bottom:100px;
  top:0!important;
}
a{color:var(--cream);text-decoration:none;transition:color .2s}
a:hover{color:var(--red)}
img{max-width:100%!important;height:auto!important;display:block}
h1,h2,h3,h4{font-family:var(--font-title);text-transform:uppercase;letter-spacing:.03em;margin:0 0 .5em;color:var(--text)}
::selection{background:var(--red);color:#fff}
.gadget-title{display:none}

/* Esconder barra e tooltips do Google Translate */
.goog-te-banner-frame,
#goog-gt-tt,
.goog-te-balloon-frame,
.goog-tooltip,
.goog-tooltip:hover,
#google_translate_element{display:none!important}
.goog-text-highlight{background:transparent!important;box-shadow:none!important;border:none!important}
iframe.skiptranslate{display:none!important}

/* ==========================================================
   HEADER
   ========================================================== */
.rb-top{
  background:
    radial-gradient(1200px 300px at 50% -120px,rgba(226,32,42,.25),transparent 60%),
    linear-gradient(180deg,#121215 0%,var(--bg) 100%);
  border-bottom:1px solid var(--border-red);
  position:relative;
}
.rb-top::after{
  content:'';
  position:absolute;left:0;right:0;bottom:-1px;height:1px;
  background:linear-gradient(90deg,transparent,var(--red),transparent);
  opacity:.6;
}
.rb-top-inner{
  max-width:var(--max);
  margin:0 auto;
  padding:22px 24px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:20px;
  flex-wrap:wrap;
}
.rb-brand{display:flex;align-items:center;gap:16px;min-width:0}
.rb-brand-bar{
  width:6px;height:56px;border-radius:6px;
  background:linear-gradient(180deg,var(--red),var(--red-dark));
  box-shadow:0 0 20px rgba(226,32,42,.55);
  flex-shrink:0;
}
.rb-brand-logo img{
  max-height:56px;width:auto;
  filter:drop-shadow(0 4px 14px rgba(226,32,42,.35));
}
.rb-brand-txt h1{
  font-size:24px;margin:0;line-height:1.1;color:var(--cream);
}
.rb-brand-txt h1 a{color:var(--cream)}
.rb-brand-txt p{
  margin:2px 0 0;font-size:12px;color:var(--text-2);max-width:520px;
}
.rb-live{
  display:inline-flex;align-items:center;gap:7px;
  background:rgba(226,32,42,.14);
  border:1px solid var(--border-red);
  color:var(--red);
  padding:5px 12px;border-radius:30px;
  font-size:10px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;
  margin-bottom:6px;
}
.rb-live .dot{
  width:7px;height:7px;border-radius:50%;background:var(--red);
  animation:rbPulse 1.6s infinite;
}
@keyframes rbPulse{0%{box-shadow:0 0 0 0 rgba(226,32,42,.6)}70%{box-shadow:0 0 0 10px rgba(226,32,42,0)}100%{box-shadow:0 0 0 0 rgba(226,32,42,0)}}

/* ==========================================================
   BARRA DE PESQUISA
   ========================================================== */
.rb-search{
  display:flex;
  align-items:center;
  background:rgba(255,255,255,.04);
  border:1px solid var(--border-soft);
  border-radius:26px;
  padding:0 5px 0 18px;
  height:44px;
  width:320px;
  max-width:100%;
  transition:border-color .25s, box-shadow .25s, background .25s;
}
.rb-search:hover{background:rgba(255,255,255,.06)}
.rb-search:focus-within{
  border-color:var(--red);
  box-shadow:0 0 0 3px rgba(226,32,42,.15);
  background:rgba(255,255,255,.07);
}
.rb-search form{
  display:flex;
  width:100%;
  align-items:center;
  gap:8px;
}
.rb-search input[type=text]{
  flex:1;
  background:transparent;
  border:none;
  color:var(--text);
  font-family:var(--font-body);
  font-size:13px;
  outline:none;
  min-width:0;
}
.rb-search input[type=text]::placeholder{
  color:var(--text-2);
}
.rb-search button{
  width:34px;height:34px;
  border-radius:50%;
  background:var(--red);
  border:0;
  display:flex;
  align-items:center;
  justify-content:center;
  cursor:pointer;
  padding:0;
  flex-shrink:0;
  transition:background .2s, transform .2s;
}
.rb-search button:hover{background:var(--red-dark);transform:scale(1.05)}
.rb-search button svg{
  width:16px;height:16px;
  fill:#fff;
}

/* ==========================================================
   ABA OCULTA DE TRADUÇÃO
   ========================================================== */
.rb-translate-toggle{
  position:fixed;
  right:16px;
  top:50%;
  transform:translateY(-50%);
  z-index:9998;
  width:48px;height:48px;
  border-radius:50%;
  background:var(--red);
  border:0;
  cursor:pointer;
  display:flex;
  align-items:center;
  justify-content:center;
  box-shadow:0 6px 20px rgba(226,32,42,.5);
  transition:transform .2s, background .2s, box-shadow .2s;
  padding:0;
}
.rb-translate-toggle:hover{
  transform:translateY(-50%) scale(1.08);
  background:var(--red-dark);
  box-shadow:0 8px 26px rgba(226,32,42,.7);
}
.rb-translate-toggle svg{
  width:22px;height:22px;
  fill:#fff;
}

.rb-translate-panel{
  position:fixed;
  right:74px;
  top:50%;
  transform:translateY(-50%) translateX(20px) scale(.95);
  transform-origin:right center;
  z-index:9998;
  background:rgba(20,20,24,.96);
  backdrop-filter:blur(18px) saturate(180%);
  -webkit-backdrop-filter:blur(18px) saturate(180%);
  border:1px solid var(--border-red);
  border-radius:14px;
  padding:14px;
  min-width:180px;
  opacity:0;
  pointer-events:none;
  transition:opacity .25s, transform .25s;
  box-shadow:0 12px 40px rgba(0,0,0,.7), 0 0 0 1px rgba(226,32,42,.15);
}
.rb-translate-panel.aberto{
  opacity:1;
  pointer-events:auto;
  transform:translateY(-50%) translateX(0) scale(1);
}
.rb-translate-lbl{
  font-family:var(--font-title);
  font-size:10px;
  color:var(--text-2);
  letter-spacing:.16em;
  text-transform:uppercase;
  text-align:center;
  margin-bottom:10px;
  padding-bottom:8px;
  border-bottom:1px solid var(--border-soft);
}
.rb-translate-panel a{
  display:flex;
  align-items:center;
  gap:10px;
  padding:9px 12px;
  border-radius:10px;
  font-size:13px;
  font-weight:500;
  color:var(--text);
  cursor:pointer;
  transition:all .18s;
  white-space:nowrap;
  text-decoration:none;
  border:1px solid transparent;
  margin-bottom:4px;
}
.rb-translate-panel a:last-child{margin-bottom:0}
.rb-translate-panel a:hover{
  background:rgba(226,32,42,.15);
  border-color:var(--border-red);
  color:#fff;
  transform:translateX(2px);
}
.rb-translate-panel a.on{
  background:var(--red);
  color:#fff;
  border-color:var(--red);
  box-shadow:0 4px 14px rgba(226,32,42,.35);
}
.rb-translate-panel .flag{
  font-size:17px;
  line-height:1;
  flex-shrink:0;
}

/* ==========================================================
   MENU
   ========================================================== */
.rb-menu-section{display:block}
.rb-nav{
  background:rgba(10,10,12,.85);
  backdrop-filter:blur(14px);
  -webkit-backdrop-filter:blur(14px);
  border-bottom:1px solid var(--border-soft);
  position:sticky;top:0;z-index:50;
}
.rb-nav-inner{
  max-width:var(--max);margin:0 auto;padding:10px 24px;
  display:flex;align-items:center;justify-content:center;
  gap:6px;flex-wrap:wrap;
}
.rb-nav a{
  font-size:13px;font-weight:500;color:var(--text-2);
  padding:8px 16px;border-radius:8px;
  border:1px solid transparent;
  transition:all .2s;white-space:nowrap;
}
.rb-nav a:hover{
  color:#fff;background:rgba(226,32,42,.12);
  border-color:var(--border-red);
}
.rb-nav a.on{color:#fff;background:var(--red);border-color:var(--red)}

/* ==========================================================
   LAYOUT GERAL
   ========================================================== */
.rb-shell{
  max-width:var(--max);margin:0 auto;
  padding:32px 24px 60px;
  display:grid;
  grid-template-columns:minmax(0,1fr) 320px;
  gap:28px;
  align-items:start;
}
.rb-main{min-width:0}
.rb-sidebar{position:sticky;top:80px}

/* Blocos/seções */
.rb-block{margin-bottom:32px}
.rb-block-head{
  display:flex;align-items:center;justify-content:space-between;
  gap:14px;margin-bottom:18px;padding-bottom:12px;
  border-bottom:1px solid var(--border-soft);position:relative;
}
.rb-block-head::after{
  content:'';position:absolute;left:0;bottom:-1px;
  width:60px;height:2px;background:var(--red);
}
.rb-block-head h3{
  font-size:15px;letter-spacing:.14em;color:var(--cream);margin:0;
}
.rb-block-head .hoje{font-size:11px;color:var(--text-2);letter-spacing:.08em}

/* ==========================================================
   POSTAGENS DO BLOG
   ========================================================== */
.rb-posts-wrap{
  background:linear-gradient(180deg,var(--card) 0%,var(--bg-2) 100%);
  border:1px solid var(--border-soft);
  border-radius:var(--radius);
  padding:26px;
}
.rb-posts-header{
  display:flex;align-items:center;justify-content:space-between;
  gap:14px;margin-bottom:22px;padding-bottom:16px;
  border-bottom:1px solid var(--border-soft);position:relative;
  flex-wrap:wrap;
}
.rb-posts-header::after{
  content:'';position:absolute;left:0;bottom:-1px;
  width:80px;height:2px;background:var(--red);
}
.rb-posts-header h3{
  font-size:16px;letter-spacing:.14em;color:var(--cream);margin:0;
}

/* ==========================================================
   BOTÃO "LANÇAMENTOS DO ROCK" (no header de posts)
   ========================================================== */
.rb-releases-btn{
  background:rgba(226,32,42,.12);
  border:1px solid var(--border-red);
  color:var(--red);
  padding:9px 18px;
  border-radius:30px;
  font-family:var(--font-title);
  font-size:11px;
  letter-spacing:.14em;
  text-transform:uppercase;
  font-weight:700;
  cursor:pointer;
  transition:all .22s ease;
  display:inline-flex;
  align-items:center;
  gap:8px;
  line-height:1;
  white-space:nowrap;
}
.rb-releases-btn:hover{
  background:var(--red);
  color:#fff;
  border-color:var(--red);
  box-shadow:0 4px 14px rgba(226,32,42,.35);
  transform:translateY(-1px);
}
.rb-releases-btn .rb-arrow{
  display:inline-block;
  font-size:14px;
  transition:transform .25s ease;
  line-height:1;
}
.rb-releases-btn.aberto{
  background:var(--red);
  color:#fff;
  border-color:var(--red);
}
.rb-releases-btn.aberto .rb-arrow{
  transform:rotate(180deg);
}

/* ==========================================================
   PAINEL EXPANSÍVEL DE LANÇAMENTOS
   ========================================================== */
#rb-rock-releases{
  max-height:0;
  overflow:hidden;
  opacity:0;
  margin:0 0 0 0;
  padding:0 18px;
  background:rgba(20,20,24,.55);
  border:1px solid transparent;
  border-radius:var(--radius);
  transition:max-height .45s ease, opacity .3s ease, margin .3s ease, padding .3s ease, border-color .3s ease;
}
#rb-rock-releases.aberto{
  max-height:1200px;
  opacity:1;
  margin:0 0 24px 0;
  padding:18px;
  border-color:var(--border-red);
}
#rb-rock-releases-title{
  font-family:var(--font-title);
  font-size:12px;
  letter-spacing:.16em;
  color:var(--cream);
  text-transform:uppercase;
  margin:0 0 12px;
  padding-bottom:8px;
  border-bottom:1px dashed var(--border-soft);
  display:flex;align-items:center;gap:8px;
}
#rb-rock-releases-title::before{
  content:'';
  display:inline-block;
  width:8px;height:8px;border-radius:50%;
  background:var(--red);
  box-shadow:0 0 8px rgba(226,32,42,.8);
}
#rb-releases-list{
  display:grid;
  gap:6px;
}
#rb-releases-list > div{
  padding:8px;
  border-bottom:1px solid var(--border-soft);
  transition:background .2s;
  border-radius:8px;
}
#rb-releases-list > div:last-child{border-bottom:none}
#rb-releases-list > div:hover{background:rgba(226,32,42,.08)}
#rb-releases-list a:hover{color:var(--red-2)!important}
#rb-releases-loading{
  color:var(--text-2);
  font-size:13px;
  text-align:center;
  padding:8px 0;
  margin:0;
}

/* Grid de posts */
.blog-posts{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(290px,1fr));
  gap:22px;
}
body.item .blog-posts{display:block}

/* CARD DE POST - destaque vermelho no contorno */
.post{
  background:var(--bg-2);
  border:1px solid var(--border-red);
  border-radius:var(--radius);
  overflow:hidden;
  display:flex;flex-direction:column;
  position:relative;
  transition:transform .28s,border-color .28s,box-shadow .28s;
}
.post::before{
  content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:linear-gradient(90deg,var(--red),var(--red-dark));
  opacity:.85;transition:opacity .25s;
}
.post:hover{
  transform:translateY(-5px);
  border-color:var(--red);
  box-shadow:0 16px 36px rgba(226,32,42,.22),0 0 0 1px rgba(226,32,42,.4);
}
.post:hover::before{opacity:1}
.post-thumb{
  width:100%;aspect-ratio:16/9;overflow:hidden;background:var(--card-2);
  border-bottom:1px solid var(--border-soft);
  position:relative;
}
.post-thumb img{
  width:100%!important;height:100%!important;object-fit:cover;
  transition:transform .5s;
}
.post:hover .post-thumb img{transform:scale(1.06)}
.post-conteudo{padding:20px;flex:1;display:flex;flex-direction:column}
.post-title{font-size:18px;margin-bottom:10px;line-height:1.3}
.post-title a{color:var(--text)}
.post-title a:hover{color:var(--red-2)}
.post-meta{
  font-size:11px;color:var(--text-2);text-transform:uppercase;
  letter-spacing:.08em;margin-bottom:14px;padding-bottom:12px;
  border-bottom:1px dashed var(--border-soft);
  display:flex;align-items:center;flex-wrap:wrap;gap:6px;
}
.post-meta .post-date{
  color:var(--cream);
  font-weight:500;
  letter-spacing:.06em;
}
.post-meta .post-author{
  color:var(--red);
  font-weight:600;
  letter-spacing:.06em;
}
.post-featured .post-meta .post-date{color:var(--cream)}
.post-featured .post-meta .post-author{color:var(--red-2)}
.post-body{color:var(--text);font-size:14px;flex:1}
.post-body p{margin:0 0 1em}
.post-footer{
  margin-top:16px;padding-top:14px;
  border-top:1px solid var(--border-soft);
  display:flex;justify-content:space-between;flex-wrap:wrap;
  gap:8px;font-size:12px;color:var(--text-2);
}
.post-footer a{color:var(--text-2)}
.post-footer a:hover{color:var(--red)}
.jump-link a{
  display:inline-block;margin-top:14px;
  font-family:var(--font-title);font-size:12px;
  letter-spacing:.1em;color:var(--red);
  border-bottom:1px solid transparent;
}
.jump-link a:hover{border-bottom-color:var(--red)}

/* ==========================================================
   POST EM DESTAQUE (primeira postagem)
   ========================================================== */
.post-featured{
  grid-column:1/-1;
  display:grid;
  grid-template-columns:1.15fr 1fr;
  align-items:stretch;
  min-height:340px;
  border-color:var(--red);
  box-shadow:0 10px 30px rgba(226,32,42,.18);
}
.post-featured::before{
  height:4px;
  opacity:1;
}
.post-featured:hover{
  transform:translateY(-6px);
  box-shadow:0 20px 44px rgba(226,32,42,.32),0 0 0 1px var(--red);
}
.post-featured .post-thumb{
  aspect-ratio:auto;
  height:100%;
  min-height:300px;
  border-bottom:none;
  border-right:1px solid var(--border-red);
}
.post-featured .post-thumb img{
  height:100%!important;
}
.post-featured .post-conteudo{
  padding:34px 32px;
  justify-content:center;
}
.post-featured .post-title{
  font-size:28px;
  line-height:1.2;
  margin-bottom:14px;
  letter-spacing:.02em;
}
.post-featured .post-title a{color:var(--cream)}
.post-featured .post-title a:hover{color:var(--red-2)}
.post-featured .post-meta{
  font-size:12px;
  margin-bottom:16px;
}
.post-featured .post-body{
  font-size:15px;
  line-height:1.75;
}
.post-featured .jump-link a{
  font-size:13px;
  letter-spacing:.12em;
}
.post-featured-badge{
  position:absolute;
  top:16px;left:16px;
  background:var(--red);
  color:#fff;
  padding:6px 14px;
  border-radius:20px;
  font-family:var(--font-title);
  font-size:11px;
  letter-spacing:.18em;
  text-transform:uppercase;
  font-weight:700;
  box-shadow:0 6px 18px rgba(226,32,42,.55);
  z-index:3;
}

body.item .post{display:block}
body.item .post::before{height:4px}
body.item .post-thumb{aspect-ratio:auto;max-height:440px}
body.item .post-thumb img{height:auto!important}

/* ==========================================================
   PAGINAÇÃO — SETAS DESTACADAS
   ========================================================== */
.blog-pager{
  display:flex;
  justify-content:space-between;
  align-items:center;
  margin:30px 0 0;
  padding-top:24px;
  border-top:1px solid var(--border-soft);
  font-family:var(--font-title);
  font-size:13px;
  letter-spacing:.08em;
  gap:12px;
  flex-wrap:wrap;
}
.blog-pager a{
  color:var(--cream);
  display:inline-flex;
  align-items:center;
  gap:10px;
  padding:4px 6px;
  border-radius:10px;
  transition:color .2s;
}
.blog-pager a:hover{color:var(--red-2)}

.blog-pager .arrow{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  width:44px;
  height:44px;
  border-radius:50%;
  border:2px solid var(--red);
  color:var(--red);
  font-size:26px;
  font-weight:700;
  line-height:1;
  text-align:center;
  background:rgba(226,32,42,.06);
  transition:all .22s ease;
  flex-shrink:0;
  font-family:'Oswald','Arial Narrow',sans-serif;
  padding-bottom:4px;
}
.blog-pager a:hover .arrow{
  background:var(--red);
  color:#fff;
  border-color:var(--red-2);
  transform:scale(1.12);
  box-shadow:0 0 0 5px rgba(226,32,42,.18), 0 6px 20px rgba(226,32,42,.5);
}

/* ==========================================================
   WIDGETS (sidebar, footer)
   ========================================================== */
.widget-box{
  background:var(--card);
  border:1px solid var(--border-soft);
  border-radius:var(--radius);
  padding:20px;margin-bottom:20px;
  position:relative;
  transition:border-color .2s;
}
.widget-box:hover{border-color:var(--border-red)}
.widget-box::before{
  content:'';position:absolute;top:0;left:0;
  width:44px;height:2px;background:var(--red);
}
.widget-box h2,
.widget-box .title{
  font-family:var(--font-title);font-size:13px;
  text-transform:uppercase;letter-spacing:.14em;
  color:var(--cream);margin:0 0 14px;padding-bottom:10px;
  border-bottom:1px solid var(--border-soft);
}
.widget-box ul{list-style:none;margin:0;padding:0}
.widget-box li{margin-bottom:8px;font-size:14px}
.widget-box li a{color:var(--text-2)}
.widget-box li a:hover{color:var(--red)}
.label-list{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0;margin:0}
.label-list li a{
  display:inline-block;border:1px solid var(--border-soft);
  border-radius:20px;padding:6px 14px;
  font-size:12px;color:var(--text-2);
}
.label-list li a:hover{border-color:var(--red);color:var(--red)}
#BlogSearch1 form{display:flex;gap:8px}
#BlogSearch1 input[type=text]{
  flex:1;background:var(--bg-2);border:1px solid var(--border-soft);
  border-radius:10px;padding:10px 14px;color:var(--text);
  font-family:var(--font-body);
}
#BlogSearch1 input[type=text]:focus{
  outline:none;border-color:var(--red);
}
#BlogSearch1 input[type=submit]{
  background:var(--red);color:#fff;border:none;border-radius:10px;
  padding:0 18px;font-family:var(--font-title);text-transform:uppercase;
  font-size:12px;letter-spacing:.06em;cursor:pointer;
  transition:background .2s;
}
#BlogSearch1 input[type=submit]:hover{background:var(--red-dark)}

/* ==========================================================
   PLAYER FLUTUANTE
   ========================================================== */
.rb-floating-player{
  position:fixed;
  bottom:0;left:0;right:0;
  z-index:9999;
  background:rgba(20,20,24,0.78);
  backdrop-filter:blur(22px) saturate(180%);
  -webkit-backdrop-filter:blur(22px) saturate(180%);
  border-top:1px solid rgba(240,223,180,0.15);
  border-radius:20px 20px 0 0;
  box-shadow:0 -12px 40px rgba(0,0,0,0.65);
  padding:14px 24px;
  display:flex;
  align-items:center;
  gap:16px;
}
.rb-fp-cover{
  width:56px;height:56px;
  border-radius:10px;
  overflow:hidden;
  flex-shrink:0;
  background:var(--card-2);
  border:1px solid rgba(240,223,180,0.15);
}
.rb-fp-cover img{
  width:100%!important;
  height:100%!important;
  object-fit:cover!important;
}
.rb-fp-info{flex:1;min-width:0}
.rb-fp-status{
  display:flex;
  align-items:center;
  gap:6px;
  font-size:9px;
  font-weight:700;
  letter-spacing:.15em;
  text-transform:uppercase;
  color:var(--red);
  margin-bottom:2px;
}
.rb-fp-dot{
  width:7px;height:7px;
  border-radius:50%;
  background:var(--red);
  animation:rbPulse 1.6s infinite;
}
.rb-fp-title{
  font-family:var(--font-title);
  font-size:15px;
  font-weight:700;
  color:var(--cream);
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
  line-height:1.2;
}
.rb-fp-artist{
  font-size:12px;
  color:var(--text-2);
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
  margin-top:1px;
}
.rb-fp-time{
  font-size:11px;
  color:var(--text-2);
  font-family:var(--font-title);
  letter-spacing:.05em;
  min-width:45px;
  text-align:right;
  flex-shrink:0;
}
.rb-fp-controls{
  display:flex;
  align-items:center;
  gap:10px;
  flex-shrink:0;
}
.rb-fp-btn{
  width:40px;height:40px;
  border-radius:50%;
  background:rgba(255,255,255,0.08);
  border:1px solid rgba(240,223,180,0.12);
  display:flex;
  align-items:center;
  justify-content:center;
  cursor:pointer;
  transition:all .2s;
  padding:0;
}
.rb-fp-btn:hover{background:rgba(226,32,42,0.25);border-color:var(--red)}
.rb-fp-btn svg{width:18px;height:18px;fill:var(--text-2)}
.rb-fp-btn:hover svg{fill:var(--cream)}
.rb-fp-play{
  width:52px;height:52px;
  border-radius:50%;
  background:var(--red);
  border:0;
  display:flex;
  align-items:center;
  justify-content:center;
  cursor:pointer;
  transition:all .2s;
  box-shadow:0 6px 20px rgba(226,32,42,.4);
  padding:0;
}
.rb-fp-play:hover{background:var(--red-dark);transform:scale(1.05)}
.rb-fp-play svg{width:20px;height:20px;fill:#fff}
.rb-fp-play svg.icon-pause{display:none}
.rb-fp-play.tocando svg.icon-play{display:none}
.rb-fp-play.tocando svg.icon-pause{display:block}
.rb-fp-progress{
  position:absolute;
  bottom:0;left:0;right:0;
  height:3px;
  background:rgba(255,255,255,0.08);
  border-radius:0 0 20px 20px;
  overflow:hidden;
}
.rb-fp-progress-bar{
  position:absolute;
  top:0;
  left:0;
  height:100%;
  width:45%;
  background:linear-gradient(90deg,
    transparent 0%,
    var(--red) 25%,
    var(--cream) 50%,
    var(--red) 75%,
    transparent 100%);
  border-radius:2px;
  opacity:0;
  transition:opacity .3s ease;
  will-change:left;
  pointer-events:none;
}
.rb-floating-player.tocando .rb-fp-progress-bar{
  opacity:1;
  animation:rbLoadingBar 1.1s linear infinite;
}
@keyframes rbLoadingBar{
  0%   { left:-45%; }
  100% { left:100%; }
}

/* ==========================================================
   FOOTER
   ========================================================== */
#footer-wrapper{
  border-top:1px solid var(--border-red);
  padding:28px 0 24px;
  font-size:12px;
  color:var(--text-2);
  background:
    radial-gradient(800px 200px at 50% 120%,rgba(226,32,42,.12),transparent 60%),
    var(--bg-2);
}
.footer-inner{
  max-width:var(--max);
  margin:0 auto;padding:0 24px;
  display:flex;justify-content:space-between;align-items:center;
  flex-wrap:wrap;gap:16px;
}
.footer-inner a{color:var(--cream)}
.footer-inner a:hover{color:var(--red)}

/* ==========================================================
   RESPONSIVO
   ========================================================== */
@media(max-width:1024px){
  .rb-shell{grid-template-columns:1fr}
  .rb-sidebar{position:static}
}
@media(max-width:900px){
  .post-featured{
    grid-template-columns:1fr;
    min-height:0;
  }
  .post-featured .post-thumb{
    aspect-ratio:16/9;
    min-height:0;
    border-right:none;
    border-bottom:1px solid var(--border-red);
  }
  .post-featured .post-conteudo{
    padding:22px 20px;
  }
  .post-featured .post-title{
    font-size:21px;
  }
  .post-featured .post-body{
    font-size:14px;
  }
}
@media(max-width:768px){
  .rb-top-inner{padding:18px 16px;flex-direction:column;text-align:center;gap:14px}
  .rb-brand{flex-direction:column;text-align:center}
  .rb-brand-bar{width:48px;height:4px}
  .rb-brand-txt h1{font-size:22px}
  .rb-search{width:100%}
  .rb-nav-inner{padding:8px 14px}
  .rb-nav a{font-size:12px;padding:6px 12px}
  .rb-shell{padding:20px 16px 40px}
  .rb-posts-wrap{padding:18px}
  .rb-floating-player{padding:10px 14px;gap:10px}
  .rb-fp-cover{width:46px;height:46px}
  .rb-fp-title{font-size:13px}
  .rb-fp-artist{font-size:11px}
  .rb-fp-play{width:44px;height:44px}
  .rb-fp-btn{width:34px;height:34px}
  .rb-fp-time{display:none}
  body{padding-bottom:90px}
  .footer-inner{flex-direction:column;text-align:center}
  .rb-translate-toggle{right:10px;width:44px;height:44px}
  .rb-translate-panel{right:62px;min-width:160px}
  .blog-pager .arrow{width:38px;height:38px;font-size:22px}
  #rb-rock-releases.aberto{padding:14px}
  .rb-posts-header{justify-content:center}
  .rb-releases-btn{font-size:10px;padding:8px 14px}
}
@media(max-width:480px){
  .rb-fp-cover{display:none}
  .rb-brand-txt h1{font-size:20px}
  .post-title{font-size:16px}
  .post-featured .post-title{font-size:18px}
  .post-featured .post-conteudo{padding:18px 16px}
  .rb-translate-panel{right:58px;padding:10px;min-width:150px}
  .rb-translate-panel a{padding:8px 10px;font-size:12px}
  .blog-pager{font-size:12px}
  .blog-pager a{gap:8px}
  .blog-pager .arrow{width:34px;height:34px;font-size:20px;border-width:2px}
  .rb-releases-btn{font-size:10px;padding:7px 12px;letter-spacing:.1em}
}
]]></b:skin>
</head>
<body>

<!-- ============================================================ -->
<!-- HEADER (com barra de pesquisa)                               -->
<!-- ============================================================ -->
<header class='rb-top'>
  <div class='rb-top-inner'>
    <div class='rb-brand'>
      <div class='rb-brand-bar'/>
      <div class='rb-brand-logo'>
        <img alt='Rádio RockBack FM' src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVtXqb5bwqXrPTeXWIkzASDRo6DKJTc3mjUEet2fVy9Lo4rQ15fDP9Vn8dQ8wX9yC840f5fSuqmfEuH5a9ecnaiIsJjheXJvrQdf4iCRw2NdnYYRRZSPxsIA3h1MUscQM2RiV8bdAwprjmbUDYMmA5a2kPxY8oyKbQeV1jn2hWxjGbxHYAfuEUCDGSNxQ/s400/R%C3%A1dio%20RockBack%20FM%20Logo%20Trasparente.png'/>
      </div>
      <div class='rb-brand-txt'>
        <div class='rb-live'><span class='dot'/> AO VIVO</div>
        <h1><a expr:href='data:blog.homepageUrl'><data:blog.title/></a></h1>
        <p><data:blog.description/></p>
      </div>
    </div>

    <!-- BARRA DE PESQUISA -->
    <div class='rb-search'>
      <form expr:action='data:blog.searchUrl' method='get' role='search'>
        <input autocomplete='off' maxlength='255' name='q' placeholder='Pesquisar no blog...' type='text'/>
        <button aria-label='Pesquisar' type='submit'>
          <svg viewBox='0 0 24 24'><path d='M15.5 14h-.79l-.28-.27a6.5 6.5 0 1 0-.7.7l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0A4.5 4.5 0 1 1 14 9.5 4.5 4.5 0 0 1 9.5 14z'/></svg>
        </button>
      </form>
    </div>
  </div>
</header>

<!-- ============================================================ -->
<!-- MENU &#8212; EDITÁVEL NO LAYOUT                                    -->
<!-- ============================================================ -->
<b:section class='rb-menu-section' id='menu' maxwidgets='3' showaddelement='yes'>
  <b:widget id='LinkList1' locked='false' title='Menu Principal' type='LinkList' version='2' visible='true'>
    <b:widget-settings>
      <b:widget-setting name='link-3'>https://radio-rockback-fm.br.uptodown.com/android</b:widget-setting>
      <b:widget-setting name='sorting'>NONE</b:widget-setting>
      <b:widget-setting name='link-4'>https://github.com/Cassinaojk/C-digo-do-Player-da-R-dio-RockBack-FM.git</b:widget-setting>
      <b:widget-setting name='text-1'>Contato</b:widget-setting>
      <b:widget-setting name='link-1'>https://radiorockbackfm.blogspot.com/search/label/Contato</b:widget-setting>
      <b:widget-setting name='text-0'>Início</b:widget-setting>
      <b:widget-setting name='link-2'>https://radiorockbackfm.blogspot.com/2024/10/blog-post.html</b:widget-setting>
      <b:widget-setting name='text-3'>App da Rádio</b:widget-setting>
      <b:widget-setting name='link-0'>/</b:widget-setting>
      <b:widget-setting name='text-2'>Sobre-Nós</b:widget-setting>
      <b:widget-setting name='text-4'>Código do Player</b:widget-setting>
    </b:widget-settings>
    <b:includable id='main'>
      <nav class='rb-nav'>
        <div class='rb-nav-inner'>
          <b:loop values='data:links' var='link'>
            <a expr:href='data:link.target'><data:link.name/></a>
          </b:loop>
        </div>
      </nav>
    </b:includable>
    <b:includable id='content'>
      <div class='widget-content'>
        <ul>
          <b:loop values='data:links' var='link'>
            <li><a expr:href='data:link.target'><data:link.name/></a></li>
          </b:loop>
        </ul>
      </div>
    </b:includable>
  </b:widget>
  <b:widget id='BlogSearch1' locked='false' title='Pesquisar' type='BlogSearch' version='2' visible='false'>
    <b:includable id='main'>
      <div class='widget-box'><h2><data:title/></h2>
      <form expr:action='data:blog.homepageUrl + &quot;search&quot;' method='get' role='search'>
        <input maxlength='255' name='q' type='text'/>
        <input type='submit' value='Buscar'/>
      </form></div>
    </b:includable>
    <b:includable id='content'>
      <div class='widget-content' role='search'>
        <b:include name='searchForm'/>
      </div>
    </b:includable>
    <b:includable id='searchForm'>
      <form expr:action='data:blog.searchUrl'>
        <b:attr cond='not data:view.isPreview' name='target' value='_top'/>
        <b:include name='urlParamsAsFormInput'/>
        <div class='search-input'>
          <input autocomplete='off' expr:aria-label='data:messages.searchThisBlog' expr:placeholder='data:messages.searchThisBlog' expr:value='data:view.isSearch ? data:view.search.query.escaped : &quot;&quot;' name='q'/>
        </div>
        <b:include name='searchSubmit'/>
      </form>
    </b:includable>
    <b:includable id='searchSubmit'>
      <input class='search-action' expr:value='data:messages.search.escaped' type='submit'/>
    </b:includable>
  </b:widget>
</b:section>

<!-- ============================================================ -->
<!-- SHELL: MAIN + SIDEBAR                                        -->
<!-- ============================================================ -->
<div class='rb-shell'>

  <div class='rb-main'>

    <b:section class='rb-posts-wrap' id='main' maxwidgets='1' showaddelement='no'>
      <b:widget id='Blog1' locked='false' title='Postagens no blog' type='Blog' version='2' visible='true'>
        <b:widget-settings>
          <b:widget-setting name='showDateHeader'>false</b:widget-setting>
          <b:widget-setting name='showShareButtons'>true</b:widget-setting>
          <b:widget-setting name='showCommentLink'>true</b:widget-setting>
          <b:widget-setting name='showAuthor'>false</b:widget-setting>
          <b:widget-setting name='style.unittype'>TextAndImage</b:widget-setting>
          <b:widget-setting name='timestampLabel'/>
          <b:widget-setting name='reactionsLabel'/>
          <b:widget-setting name='showAuthorProfile'>false</b:widget-setting>
          <b:widget-setting name='style.layout'>1x1</b:widget-setting>
          <b:widget-setting name='showLabels'>true</b:widget-setting>
          <b:widget-setting name='showLocation'>true</b:widget-setting>
          <b:widget-setting name='postLabelsLabel'/>
          <b:widget-setting name='showTimestamp'>true</b:widget-setting>
          <b:widget-setting name='postsPerAd'>1</b:widget-setting>
          <b:widget-setting name='showBacklinks'>false</b:widget-setting>
          <b:widget-setting name='showInlineAds'>false</b:widget-setting>
          <b:widget-setting name='showReactions'>false</b:widget-setting>
        </b:widget-settings>
        <b:includable id='main' var='top'>
          <div class='rb-posts-header'>
            <h3>Últimas Postagens</h3>
            <b:if cond='data:blog.pageType != &quot;item&quot;'>
              <button aria-controls='rb-rock-releases' aria-expanded='false' class='rb-releases-btn' id='rb-releases-toggle' type='button'>
                <span>🎸 Lançamentos do Rock</span>
                <span class='rb-arrow'>&#9662;</span>
              </button>
            </b:if>
          </div>
          <b:if cond='data:blog.pageType != &quot;item&quot;'>
            <div id='rb-rock-releases'>
              <h4 id='rb-rock-releases-title'>🎸 Lançamentos do Rock</h4>
              <div id='rb-releases-list'/>
              <p id='rb-releases-loading'>Carregando lançamentos...</p>
            </div>
          </b:if>
          <div class='blog-posts hfeed'>
            <b:loop index='i' values='data:top.posts' var='post'>
              <article class='post hentry'>
                <b:class cond='data:i == 0 and data:blog.pageType != &quot;item&quot; and data:post.featuredImage' name='post-featured'/>
                <b:if cond='data:post.featuredImage'>
                  <div class='post-thumb'>
                    <b:if cond='data:i == 0 and data:blog.pageType != &quot;item&quot;'>
                      <span class='post-featured-badge'>&#9733; Destaque</span>
                    </b:if>
                    <a expr:href='data:post.url'><img expr:alt='data:post.title' expr:src='data:post.featuredImage'/></a>
                  </div>
                </b:if>
                <div class='post-conteudo'>
                  <b:if cond='data:post.title'>
                    <h2 class='post-title entry-title'>
                      <a expr:href='data:post.url'><data:post.title/></a>
                    </h2>
                  </b:if>
                  <div class='post-meta'>
                    <span class='post-date'>📅 <b:eval expr='data:post.date format &quot;dd/MM/yyyy&quot;'/></span>
                    <span class='post-author'>&#160;&#183;&#160;POR: Rádio RockBack FM</span>
                  </div>
                  <div class='post-body entry-content'>
                    <b:if cond='data:blog.pageType == &quot;item&quot;'><data:post.body/><b:else/><data:post.snippet/></b:if>
                  </div>
                  <b:if cond='data:blog.pageType != &quot;item&quot;'>
                    <div class='jump-link'><a expr:href='data:post.url'>Continuar lendo &#187;</a></div>
                  </b:if>
                  <div class='post-footer'>
                    <b:if cond='data:post.labels'>
                      <span class='post-labels'>
                        <b:loop values='data:post.labels' var='label'>
                          <a expr:href='data:label.url'><data:label.name/></a>
                          <b:if cond='data:label.isLast != true'>, </b:if>
                        </b:loop>
                      </span>
                    </b:if>
                  </div>
                </div>
              </article>
            </b:loop>
          </div>
          <b:include name='nextprev'/>
        </b:includable>
        <b:includable id='aboutPostAuthor'>
          <div class='author-name'>
            <a class='g-profile' expr:href='data:post.author.profileUrl' rel='author' title='author profile'>
              <span><data:post.author.name/></span>
            </a>
          </div>
          <div>
            <span class='author-desc'><data:post.author.aboutMe/></span>
          </div>
        </b:includable>
        <b:includable id='addComments'>
          <a expr:href='data:post.commentsUrl' expr:onclick='data:post.commentsUrlOnclick'>
            <b:message name='messages.postAComment'/>
          </a>
        </b:includable>
        <b:includable id='commentAuthorAvatar'>
          <div class='avatar-image-container'>
            <img class='author-avatar' expr:src='data:comment.authorAvatarSrc' height='35' width='35'/>
          </div>
        </b:includable>
        <b:includable id='commentDeleteIcon' var='comment'>
          <span expr:class='&quot;item-control &quot; + data:comment.adminClass'>
            <b:if cond='data:showCmtPopup'>
              <div class='goog-toggle-button'>
                <div class='goog-inline-block comment-action-icon'/>
              </div>
            <b:else/>
              <a class='comment-delete' expr:href='data:comment.deleteUrl' expr:title='data:messages.deleteComment'>
                <img src='https://resources.blogblog.com/img/icon_delete13.gif'/>
              </a>
            </b:if>
          </span>
        </b:includable>
        <b:includable id='commentForm' var='post'>
          <div class='comment-form'>
            <a name='comment-form'/>
            <h4 id='comment-post-message'><data:messages.postAComment/></h4>
            <b:if cond='data:this.messages.blogComment != &quot;&quot;'>
              <p><data:this.messages.blogComment/></p>
            </b:if>
            <b:include data='post' name='commentFormIframeSrc'/>
            <iframe allowtransparency='allowtransparency' class='blogger-iframe-colorize blogger-comment-from-post' expr:height='data:cmtIframeInitialHeight ?: &quot;90px&quot;' frameborder='0' id='comment-editor' name='comment-editor' src='' width='100%'/>
            <data:post.cmtfpIframe/>
            <script type='text/javascript'>
              BLOG_CMT_createIframe(&#39;<data:post.appRpcRelayPath/>&#39;);
            </script>
          </div>
        </b:includable>
        <b:includable id='commentFormIframeSrc' var='post'>
          <a expr:href='data:post.commentFormIframeSrc' id='comment-editor-src'/>
        </b:includable>
        <b:includable id='commentItem' var='comment'>
          <div class='comment' expr:id='&quot;c&quot; + data:comment.id'>
            <b:include cond='data:blog.enabledCommentProfileImages' name='commentAuthorAvatar'/>
            <div class='comment-block'>
              <div class='comment-author'>
                <b:if cond='data:comment.authorUrl'>
                  <b:message name='messages.authorSaidWithLink'>
                    <b:param expr:value='data:comment.author' name='authorName'/>
                    <b:param expr:value='data:comment.authorUrl' name='authorUrl'/>
                  </b:message>
                <b:else/>
                  <b:message name='messages.authorSaid'>
                    <b:param expr:value='data:comment.author' name='authorName'/>
                  </b:message>
                </b:if>
              </div>
              <div expr:class='&quot;comment-body&quot; + (data:comment.isDeleted ? &quot; deleted&quot; : &quot;&quot;)'>
                <data:comment.body/>
              </div>
              <div class='comment-footer'>
                <span class='comment-timestamp'>
                  <a expr:href='data:comment.url' title='comment permalink'>
                    <data:comment.timestamp/>
                  </a>
                  <b:include data='comment' name='commentDeleteIcon'/>
                </span>
              </div>
            </div>
          </div>
        </b:includable>
        <b:includable id='commentList' var='comments'>
          <div id='comments-block'>
            <b:loop values='data:comments' var='comment'>
              <b:include data='comment' name='commentItem'/>
            </b:loop>
          </div>
        </b:includable>
        <b:includable id='commentPicker' var='post'>
          <b:if cond='data:post.showThreadedComments'>
            <b:include data='post' name='threadedComments'/>
          <b:else/>
            <b:include data='post' name='comments'/>
          </b:if>
        </b:includable>
        <b:includable id='comments' var='post'>
          <section expr:class='&quot;comments&quot; + (data:post.embedCommentForm ? &quot; embed&quot; : &quot;&quot;)' expr:data-num-comments='data:post.numberOfComments' id='comments'>
            <a name='comments'/>
            <b:if cond='data:post.allowComments'>
              <b:include name='commentsTitle'/>
              <div expr:id='data:widget.instanceId + &quot;_comments-block-wrapper&quot;'>
                <b:include cond='data:post.comments' data='post.comments' name='commentList'/>
              </div>
              <b:if cond='data:post.commentPagingRequired'>
                <div class='paging-control-container'>
                  <b:if cond='data:post.hasOlderLinks'>
                    <a expr:class='data:post.oldLinkClass' expr:href='data:post.oldestLinkUrl'>
                      <data:messages.oldest/>
                    </a>
                    <a expr:class='data:post.oldLinkClass' expr:href='data:post.olderLinkUrl'>
                      <data:messages.older/>
                    </a>
                  </b:if>
                  <span class='comment-range-text'><data:post.commentRangeText/></span>
                  <b:if cond='data:post.hasNewerLinks'>
                    <a expr:class='data:post.newLinkClass' expr:href='data:post.newerLinkUrl'>
                      <data:messages.newer/>
                    </a>
                    <a expr:class='data:post.newLinkClass' expr:href='data:post.newestLinkUrl'>
                      <data:messages.newest/>
                    </a>
                  </b:if>
                </div>
              </b:if>
              <div class='footer'>
                <b:if cond='data:post.embedCommentForm'>
                  <b:if cond='data:post.allowNewComments'>
                    <b:include data='post' name='commentForm'/>
                  <b:else/>
                    <data:post.noNewCommentsText/>
                  </b:if>
                <b:else/>
                  <b:if cond='data:post.allowComments'>
                    <b:include data='post' name='addComments'/>
                  </b:if>
                </b:if>
              </div>
            </b:if>
            <b:if cond='data:showCmtPopup'>
              <div id='comment-popup'>
                <iframe allowtransparency='allowtransparency' frameborder='0' id='comment-actions' name='comment-actions' scrolling='no'>
                </iframe>
              </div>
            </b:if>
          </section>
        </b:includable>
        <b:includable id='commentsTitle'>
          <h3 class='title'><data:messages.comments/></h3>
        </b:includable>
        <b:includable id='feedLinks'>
          <b:if cond='!data:view.isPost'>
            <b:if cond='data:feedLinks'>
              <div class='blog-feeds'>
                <b:include data='feedLinks' name='feedLinksBody'/>
              </div>
            </b:if>
          <b:else/>
            <div class='post-feeds'>
              <b:loop values='data:posts' var='post'>
                <b:if cond='data:post.allowComments and data:post.feedLinks'>
                  <b:include data='post.feedLinks' name='feedLinksBody'/>
                </b:if>
              </b:loop>
            </div>
          </b:if>
        </b:includable>
        <b:includable id='feedLinksBody' var='links'>
          <div class='feed-links'>
            <data:messages.subscribeTo/>
            <b:loop values='data:links' var='f'>
              <a class='feed-link' expr:href='data:f.url' expr:type='data:f.mimeType' target='_blank'><data:f.name/> (<data:f.feedType/>)</a>
            </b:loop>
          </div>
        </b:includable>
        <b:includable id='homePageLink'>
          <a class='home-link' expr:href='data:blog.homepageUrl'><data:messages.home/></a>
        </b:includable>
        <b:includable id='iframeComments' var='post'/>
        <b:includable id='inlineAd' var='post'>
          <b:if cond='!data:view.isPreview'>
            <b:if cond='data:this.adCode or data:this.adClientId or data:blog.adsenseClientId'>
              <div class='inline-ad'>
                <b:if cond='data:this.adCode != &quot;&quot;'>
                  <data:this.adCode/>
                <b:else/>
                  <b:include cond='data:this.adClientId or data:blog.adsenseClientId' name='defaultAdUnit'/>
                </b:if>
              </div>
            </b:if>
          <b:else/>
            <div class='inline-ad'>
              <div class='inline-ad-placeholder'>
                <span><b:message name='messages.adsGoHere'/></span>
              </div>
            </div>
          </b:if>
        </b:includable>
        <b:includable id='nextPageLink'>
          <a class='blog-pager-older-link' expr:href='data:olderPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-older-link&quot;' expr:title='data:messages.olderPosts'>
            <data:messages.olderPosts/>
          </a>
        </b:includable>
        <b:includable id='nextprev'>
          <div class='blog-pager'>
            <span><b:if cond='data:olderPageUrl'><a expr:href='data:olderPageUrl'><span class='arrow'>&#171;</span> <data:olderPageTitle/></a></b:if></span>
            <span><b:if cond='data:newerPageUrl'><a expr:href='data:newerPageUrl'><data:newerPageTitle/> <span class='arrow'>&#187;</span></a></b:if></span>
          </div>
        </b:includable>
        <b:includable id='post' var='post'>
          <div class='post'>
            <b:include data='post' name='postMeta'/>
            <b:include data='post' name='postTitle'/>
            <b:include name='headerByline'/>
            <b:if cond='data:view.isSingleItem'>
              <b:include data='post' name='postBody'/>
            <b:else/>
              <b:include data='post' name='postBodySnippet'/>
              <b:include data='post' name='postJumpLink'/>
            </b:if>
            <b:include data='post' name='postFooter'/>
          </div>
        </b:includable>
        <b:includable id='postBody' var='post'>
          <div class='post-body entry-content float-container' expr:id='&quot;post-body-&quot; + data:post.id'>
            <data:post.body/>
          </div>
        </b:includable>
        <b:includable id='postBodySnippet' var='post'>
          <b:include data='post' name='postBody'/>
        </b:includable>
        <b:includable id='postCommentsAndAd' var='post'>
          <article class='post-outer-container'>
            <div class='post-outer'>
              <b:include data='post' name='post'/>
            </div>
            <b:include cond='data:view.isSingleItem' data='post' name='commentPicker'/>
            <b:include cond='data:view.isSingleItem and data:post.includeAd' data='post' name='inlineAd'/>
          </article>
          <b:include cond='data:view.isMultipleItems and data:post.includeAd' data='post' name='inlineAd'/>
        </b:includable>
        <b:includable id='postCommentsLink'>
          <b:if cond='data:view.isMultipleItems'>
            <span class='byline post-comment-link container'>
              <b:include cond='data:post.commentSource != 1' name='commentsLink'/>
            </span>
          </b:if>
        </b:includable>
        <b:includable id='postFooter' var='post'>
          <div class='post-footer'>
            <b:include name='footerBylines'/>
            <b:include data='post' name='postFooterAuthorProfile'/>
          </div>
        </b:includable>
        <b:includable id='postFooterAuthorProfile' var='post'>
          <b:if cond='data:post.author.aboutMe and data:view.isPost'>
            <div class='author-profile'>
              <b:if cond='data:post.author.authorPhoto.url'>
                <img class='author-image' expr:src='data:post.author.authorPhoto.url' width='50px'/>
                <div class='author-about'>
                  <b:include data='post' name='aboutPostAuthor'/>
                </div>
              <b:else/>
                <b:include data='post' name='aboutPostAuthor'/>
              </b:if>
            </div>
          </b:if>
        </b:includable>
        <b:includable id='postHeader' var='post'>
          <b:include name='headerByline'/>
        </b:includable>
        <b:includable id='postMeta' var='post'>
          <b:include data='post' name='postMetadataJSON'/>
        </b:includable>
        <b:includable id='postPagination'>
          <div class='blog-pager container' id='blog-pager'>
            <b:include cond='data:newerPageUrl' name='previousPageLink'/>
            <b:include cond='data:olderPageUrl' name='nextPageLink'/>
            <b:include cond='data:view.url != data:blog.homepageUrl' name='homePageLink'/>
          </div>
        </b:includable>
        <b:includable id='postTitle' var='post'>
          <a expr:name='data:post.id'/>
          <b:if cond='data:post.title != &quot;&quot;'>
            <h3 class='post-title entry-title'>
              <b:if cond='data:post.link or (data:post.url and data:view.url != data:post.url)'>
                <a expr:href='data:post.link ?: data:post.url'><data:post.title/></a>
              <b:else/>
                <data:post.title/>
              </b:if>
            </h3>
          </b:if>
        </b:includable>
        <b:includable id='previousPageLink'>
          <a class='blog-pager-newer-link' expr:href='data:newerPageUrl' expr:id='data:widget.instanceId + &quot;_blog-pager-newer-link&quot;' expr:title='data:messages.newerPosts'>
            <data:messages.newerPosts/>
          </a>
        </b:includable>
        <b:includable id='threadedCommentForm' var='post'>
          <div class='comment-form'>
            <a name='comment-form'/>
            <h4 id='comment-post-message'><data:messages.postAComment/></h4>
            <b:if cond='data:this.messages.blogComment != &quot;&quot;'>
              <p><data:this.messages.blogComment/></p>
            </b:if>
            <b:include data='post' name='commentFormIframeSrc'/>
            <iframe allowtransparency='allowtransparency' class='blogger-iframe-colorize blogger-comment-from-post' expr:height='data:cmtIframeInitialHeight ?: &quot;90px&quot;' frameborder='0' id='comment-editor' name='comment-editor' src='' width='100%'/>
            <data:post.cmtfpIframe/>
            <script type='text/javascript'>
              BLOG_CMT_createIframe(&#39;<data:post.appRpcRelayPath/>&#39;);
            </script>
          </div>
        </b:includable>
        <b:includable id='threadedCommentJs' var='post'>
          <script async='async' expr:src='data:post.commentSrc' type='text/javascript'/>
          <b:template-script inline='true' name='threaded_comments'/>
          <script type='text/javascript'>
            blogger.widgets.blog.initThreadedComments(
                <data:post.commentJso/>,
                <data:post.commentMsgs/>,
                <data:post.commentConfig/>);
          </script>
        </b:includable>
        <b:includable id='threadedComments' var='post'>
          <section class='comments threaded' expr:data-embed='data:post.embedCommentForm' expr:data-num-comments='data:post.numberOfComments' id='comments'>
            <a name='comments'/>
            <b:include name='commentsTitle'/>
            <div class='comments-content'>
              <b:if cond='data:post.embedCommentForm'>
                <b:include data='post' name='threadedCommentJs'/>
              </b:if>
              <div id='comment-holder'><data:post.commentHtml/></div>
            </div>
            <p class='comment-footer'>
              <b:if cond='data:post.allowNewComments'>
                <b:include data='post' name='threadedCommentForm'/>
              <b:else/>
                <data:post.noNewCommentsText/>
              </b:if>
              <b:if cond='data:post.showManageComments'>
                <b:include data='post' name='manageComments'/>
              </b:if>
            </p>
            <b:if cond='data:showCmtPopup'>
              <div id='comment-popup'>
                <iframe allowtransparency='allowtransparency' frameborder='0' id='comment-actions' name='comment-actions' scrolling='no'>
                </iframe>
              </div>
            </b:if>
          </section>
        </b:includable>
        <b:includable id='tooltipCss'>
          <style>
            .post-body a.b-tooltip-container { position: relative; display: inline-block; }
            .post-body a.b-tooltip-container .b-tooltip { display: block !important; position: absolute; top: 100%; left: 50%; transform: translate(-20%, 1px); visibility: hidden; opacity: 0; z-index: 1; transition: opacity 0.2s ease-in-out; }
            .post-body a.b-tooltip-container .b-tooltip iframe { width: 200px; height: 198px; max-width: none; border: none; border-radius: 20px; box-shadow: 1px 1px 3px 1px rgba(0, 0, 0, 0.2); }
            @media (hover: hover) { .post-body a.b-tooltip-container:hover .b-tooltip { visibility: visible; opacity: 1; } }
          </style>
        </b:includable>
      </b:widget>
      <b:widget id='Header1' locked='false' title='Rádio RockBack FM (Cabeçalho)' type='Header' version='2' visible='false'>
        <b:widget-settings>
          <b:widget-setting name='displayUrl'/>
          <b:widget-setting name='displayHeight'>0</b:widget-setting>
          <b:widget-setting name='sectionWidth'>-1</b:widget-setting>
          <b:widget-setting name='useImage'>false</b:widget-setting>
          <b:widget-setting name='shrinkToFit'>false</b:widget-setting>
          <b:widget-setting name='imagePlacement'>BEHIND</b:widget-setting>
          <b:widget-setting name='displayWidth'>0</b:widget-setting>
        </b:widget-settings>
        <b:includable id='main'>
          <div class='Header'>
            <b:if cond='data:blogTitle'>
              <b:if cond='data:sourceUrl'>
                <a expr:href='data:blog.homepageUrl'><img expr:alt='data:blogTitle' expr:src='data:sourceUrl'/></a>
              </b:if>
              <h1><a expr:href='data:blog.homepageUrl'><data:blogTitle/></a></h1>
              <b:if cond='data:blogDescription'><p class='description'><data:blogDescription/></p></b:if>
            </b:if>
          </div>
        </b:includable>
        <b:includable id='behindImageStyle'>
          <b:if cond='data:sourceUrl'>
            <b:include cond='data:this.image' data='{ image: data:this.image, selector: &quot;.header-widget&quot; }' name='responsiveImageStyle'/>
            <style type='text/css'>
              .header-widget { background-position: <data:blog.locale.languageAlignment/>; background-repeat: no-repeat; background-size: cover; }
            </style>
          </b:if>
        </b:includable>
        <b:includable id='description'><p><data:this.description/></p></b:includable>
        <b:includable id='image'>
          <a class='header-image-wrapper' expr:href='data:blog.homepageUrl'>
            <b:include data='{ image: data:image, altText: data:blog.title.escaped, originalWidth: data:width, originalHeight: data:height }' name='responsiveImage'/>
          </a>
        </b:includable>
        <b:includable id='shrinkToFitStyle'>
    <style type='text/css'>
      .header-widget-img-shrink-to-fit {
        max-width: 100%;
        height: auto;
        object-fit: scale-down;
      }
    </style>
  </b:includable>
        <b:includable id='title'>
          <h1>
            <b:tag cond='data:view.url != data:blog.homepageUrl' expr:href='data:blog.homepageUrl' name='a'>
              <data:title/>
            </b:tag>
          </h1>
        </b:includable>
      </b:widget>
    </b:section>

  </div><!-- /rb-main -->

  <aside class='rb-sidebar'>
    <b:section class='rb-extra-widgets' id='extra' showaddelement='yes'>
      <b:widget id='Image1' locked='false' title='' type='Image'>
        <b:widget-settings>
          <b:widget-setting name='displayUrl'>https://blogger.googleusercontent.com/img/a/AVvXsEgqRzr9ZEB5Kx3a1n3PP_LXgQtV2RVQIM32W3S-L11iJDJ4kx-jP-NTwId-Cn8sTeMmYDaWiAzL1GwVm8SXDZ9KTE6qAaoHoheZKk6zSNsHmEme8gwJSJM_r4kHaIPi9FlfAF8Dmo2PiMHKm0Pse9vh55TZIJ_G7JvzBQt4faQ_rg33EMEJGNVDMMn_9Mlp=s1600</b:widget-setting>
          <b:widget-setting name='displayHeight'>837</b:widget-setting>
          <b:widget-setting name='sectionWidth'>150</b:widget-setting>
          <b:widget-setting name='shrinkToFit'>false</b:widget-setting>
          <b:widget-setting name='displayWidth'>1600</b:widget-setting>
          <b:widget-setting name='link'><![CDATA[https://www.ton.com.br/renda-ton/?utm_partner_id=c138c5b9-d81f-4d0d-a07e-f2988d9777ee&utm_source=indique_um_parceiro_nov22&utm_term=c138c5b9-d81f-4d0d-a07e-f2988d9777ee]]></b:widget-setting>
          <b:widget-setting name='caption'/>
        </b:widget-settings>
        <b:includable id='main'>
    <b:if cond='data:title != &quot;&quot;'>
      <h2><data:title/></h2>
    </b:if>
    <div class='widget-content'>
      <b:tag cond='data:link' expr:href='data:link' name='a'>
        <img expr:alt='data:title' expr:height='data:height' expr:id='data:widget.instanceId + &quot;_img&quot;' expr:src='data:sourceUrl' expr:width='data:width'>
          <b:attr cond='data:sourceSet' expr:value='data:sourceSet' name='srcset'/>
          <b:attr cond='data:sourceSet' name='sizes' value='auto, 100vw'/>
          <b:attr cond='data:sourceSet' name='loading' value='lazy'/>
          <b:attr cond='data:shrinkToFit' name='class' value='image-widget-shrink-to-fit'/>
        </img>
      </b:tag>
      <br/>
      <b:if cond='data:caption'>
        <span class='caption'><data:caption/></span>
      </b:if>
    </div>
    <b:include name='quickedit'/>
    <b:include cond='data:shrinkToFit' name='shrinkToFitStyle'/>
  </b:includable>
        <b:includable id='shrinkToFitStyle'>
    <style type='text/css'>
      .image-widget-shrink-to-fit {
        max-width: 100%;
        height: auto;
        object-fit: scale-down;
      }
    </style>
  </b:includable>
      </b:widget>
      <b:widget id='BlogArchive1' locked='false' title='Arquivo' type='BlogArchive' version='2' visible='false'>
        <b:widget-settings>
          <b:widget-setting name='showStyle'>FLAT</b:widget-setting>
          <b:widget-setting name='yearPattern'>yyyy</b:widget-setting>
          <b:widget-setting name='showWeekEnd'>true</b:widget-setting>
          <b:widget-setting name='monthPattern'>MMMM yyyy</b:widget-setting>
          <b:widget-setting name='dayPattern'>MMM dd</b:widget-setting>
          <b:widget-setting name='weekPattern'>MM/dd</b:widget-setting>
          <b:widget-setting name='chronological'>false</b:widget-setting>
          <b:widget-setting name='showPosts'>false</b:widget-setting>
          <b:widget-setting name='frequency'>MONTHLY</b:widget-setting>
        </b:widget-settings>
        <b:includable id='main'>
          <div class='widget-box'><h2><data:title/></h2><div class='BlogArchive'><b:include data='data' name='flat'/></div></div>
        </b:includable>
        <b:includable id='content'>
          <div class='widget-content'>
            <div id='ArchiveList'>
              <div expr:id='data:widget.instanceId + &quot;_ArchiveList&quot;'>
                <b:include cond='data:this.style == &quot;HIERARCHY&quot;' name='hierarchy'/>
                <b:include cond='data:this.style in {&quot;FLAT&quot;, &quot;MENU&quot;}' name='flat'/>
              </div>
            </div>
          </div>
        </b:includable>
        <b:includable id='flat'>
          <ul>
            <b:loop values='data:data' var='i'>
              <li><a expr:href='data:i.url'><data:i.name/></a> (<data:i.post-count/>)</li>
            </b:loop>
          </ul>
        </b:includable>
        <b:includable id='hierarchy'>
          <b:include data='data' name='interval'/>
        </b:includable>
        <b:includable id='interval' var='intervals'>
          <ul class='hierarchy'>
            <b:loop values='data:intervals' var='interval'>
              <li class='archivedate'>
                <div class='hierarchy-title'>
                  <a class='post-count-link' expr:href='data:interval.url'>
                    <data:interval.name/>
                    <span class='post-count'><data:interval.post-count/></span>
                  </a>
                </div>
                <div class='hierarchy-content'>
                  <b:include cond='data:interval.data' data='interval.data' name='interval'/>
                  <b:include cond='data:interval.posts' data='interval.posts' name='posts'/>
                </div>
              </li>
            </b:loop>
          </ul>
        </b:includable>
        <b:includable id='posts' var='posts'>
          <ul class='posts hierarchy'>
            <b:loop values='data:posts' var='post'>
              <li>
                <a expr:href='data:post.url'><data:post.title/></a>
              </li>
            </b:loop>
          </ul>
        </b:includable>
      </b:widget>
      <b:widget id='HTML1' locked='false' title='' type='HTML'>
        <b:widget-settings>
          <b:widget-setting name='content'><![CDATA[<iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/playlist/2wf6Jmrz6N9aWE4C1d9TtX?utm_source=generator&theme=0&si=c5efcf246bab4f3b" width="100%" height="352" frameborder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>]]></b:widget-setting>
        </b:widget-settings>
        <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
      </b:widget>
      <b:widget id='Label1' locked='false' title='Marcadores' type='Label' version='2' visible='true'>
        <b:widget-settings>
          <b:widget-setting name='sorting'>ALPHA</b:widget-setting>
          <b:widget-setting name='display'>LIST</b:widget-setting>
          <b:widget-setting name='selectedLabelsList'/>
          <b:widget-setting name='showType'>ALL</b:widget-setting>
          <b:widget-setting name='showFreqNumbers'>false</b:widget-setting>
        </b:widget-settings>
        <b:includable id='main'>
          <div class='widget-box'><h2><data:title/></h2><ul class='label-list'>
            <b:loop values='data:labels' var='label'><li><a expr:href='data:label.url'><data:label.name/></a></li></b:loop>
          </ul></div>
        </b:includable>
        <b:includable id='cloud'>
          <b:loop values='data:labels' var='label'>
            <span class='label-size'>
              <b:class expr:name='&quot;label-size-&quot; + data:label.cssSize'/>
              <a class='label-name' expr:href='data:label.url'>
                <data:label.name/>
                <b:if cond='data:this.showFreqNumbers'>
                  <span class='label-count'><data:label.count/></span>
                </b:if>
              </a>
            </span>
          </b:loop>
        </b:includable>
        <b:includable id='content'>
          <div class='widget-content'>
            <b:class expr:name='data:this.display + &quot;-label-widget-content&quot;'/>
            <b:include cond='data:this.display == &quot;list&quot;' name='list'/>
            <b:include cond='data:this.display == &quot;cloud&quot;' name='cloud'/>
          </div>
        </b:includable>
        <b:includable id='list'>
          <ul>
            <b:loop values='data:labels' var='label'>
              <li>
                <a class='label-name' expr:href='data:label.url'>
                  <data:label.name/>
                  <b:if cond='data:this.showFreqNumbers'>
                    <span class='label-count'><data:label.count/></span>
                  </b:if>
                </a>
              </li>
            </b:loop>
          </ul>
        </b:includable>
      </b:widget>
    </b:section>
  </aside>

</div><!-- /rb-shell -->

<!-- ============================================================ -->
<!-- FOOTER &#8212; EDITÁVEL NO LAYOUT                                  -->
<!-- ============================================================ -->
<div id='footer-wrapper'>
  <b:section class='rb-footer-section' id='footer' maxwidgets='5' showaddelement='yes'>
    <b:widget id='HTML3' locked='false' title='' type='HTML' version='1'>
      <b:widget-settings>
        <b:widget-setting name='content'><![CDATA[<script>
//<![CDATA[
(function(){
  var s=document.createElement('style');
  s.textContent='#cx-ov{position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:999998;opacity:0;pointer-events:none;transition:.3s}#cx-ov.on{opacity:1;pointer-events:auto}#cx-pp{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%) scale(.85);width:360px;max-width:calc(100vw - 32px);background:#fff;border-radius:22px;box-shadow:0 24px 60px rgba(0,0,0,.4);z-index:999999;overflow:hidden;font-family:Arial,sans-serif;opacity:0;pointer-events:none;transition:.35s}#cx-pp.on{opacity:1;pointer-events:auto;transform:translate(-50%,-50%) scale(1)}#cx-pp .h{color:#fff;padding:16px 46px 16px 20px;font-weight:700;font-size:15px;line-height:1.3;position:relative}#cx-pp .x{position:absolute;top:10px;right:12px;width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,.22);border:0;color:#fff;font-size:18px;font-weight:700;cursor:pointer;line-height:1}#cx-pp .b{padding:16px 20px 4px;text-align:center}#cx-pp .b img{width:100%;max-width:260px;height:180px;object-fit:cover;border-radius:16px;display:block;margin:0 auto 12px}#cx-pp .t{font-size:13.5px;color:#333;line-height:1.4}#cx-pp .t b{display:block;font-size:15px;color:#111;margin-bottom:6px}#cx-pp .p{display:inline-block;margin-top:8px;padding:4px 10px;border-radius:99px;font-weight:700;font-size:11.5px}#cx-pp .c{display:block;margin:14px 20px 18px;padding:13px 16px;border-radius:14px;color:#fff!important;text-align:center;font-weight:700;font-size:14.5px;text-decoration:none}#cx-pp .f{font-size:10.5px;color:#999;text-align:center;padding:0 20px 14px}@media(max-width:420px){#cx-pp{width:calc(100vw - 24px)}#cx-pp .b img{height:150px}}';
  document.documentElement.appendChild(s);
  var AMP=String.fromCharCode(38);

  var LAST_SHOW_KEY = 'rb_popup_last_show';
  var INTERVAL_MS   = 10 * 60 * 1000;
  var now = Date.now();
  var last = parseInt(localStorage.getItem(LAST_SHOW_KEY) || '0', 10);
  if (now - last < INTERVAL_MS) return;
  localStorage.setItem(LAST_SHOW_KEY, String(now));

  var ADS=[
    {
      header:'💰 Seja Revendedor da Maquininha Ton',
      headline:'Ganhe mais de R$ 10.000/mês',
      desc:'Revendendo a maquininha que mais cresce no Brasil.',
      badge:'Renda extra',
      cta:'👉 Quero ser Revendedor Ton',
      img:'https://blogger.googleusercontent.com/img/a/AVvXsEgqRzr9ZEB5Kx3a1n3PP_LXgQtV2RVQIM32W3S-L11iJDJ4kx-jP-NTwId-Cn8sTeMmYDaWiAzL1GwVm8SXDZ9KTE6qAaoHoheZKk6zSNsHmEme8gwJSJM_r4kHaIPi9FlfAF8Dmo2PiMHKm0Pse9vh55TZIJ_G7JvzBQt4faQ_rg33EMEJGNVDMMn_9Mlp=s1600',
      link:'https://www.ton.com.br/renda-ton/?utm_partner_id=c138c5b9-d81f-4d0d-a07e-f2988d9777ee'+AMP+'utm_source=indique_um_parceiro_nov22'+AMP+'utm_term=c138c5b9-d81f-4d0d-a07e-f2988d9777ee',
      grad:'linear-gradient(135deg,#00a651,#007a3d)',
      badgeBg:'#e6f7ee',badgeColor:'#007a3d',shadow:'0 6px 16px rgba(0,166,81,.4)'
    },
    {
      header:'🎓 Cursos e Graduação na Estácio',
      headline:'Estude com bolsa e mensalidade que cabe no bolso',
      desc:'Graduação, pós e cursos livres com desconto exclusivo.',
      badge:'Bolsa de estudo',
      cta:'👉 Ver cursos e bolsas',
      img:'https://blogger.googleusercontent.com/img/a/AVvXsEiSO8sJG93yrujuiyIXwfFu1X8_UmKwpYBtXFHoGEHW-uIiYHAz_DzY08cAlOEpT1KlW5MsXOsGyEGnqrQu8w0PgXKtPGrPLZf5j_YE4HjqbGDKohKD45euDomLlR1GRIyvdmUyaZWnVbgI_HFRo54MW4brpWcM0j9KiCzb7mqS9HcaMkhZMYr8ipDJbBLb=s1600',
      link:'https://estacio.br/selecao?cod_agente=14369444'+AMP+'u=723918'+AMP+'end=1',
      grad:'linear-gradient(135deg,#0066cc,#003d80)',
      badgeBg:'#e6f0ff',badgeColor:'#003d80',shadow:'0 6px 16px rgba(0,102,204,.4)'
    }
  ];

  var NEXT_KEY = 'pp_next_ad';
  var lastIdx = parseInt(localStorage.getItem(NEXT_KEY)||'-1',10);
  var idx = (lastIdx+1)%ADS.length;
  localStorage.setItem(NEXT_KEY, String(idx));
  var ad = ADS[idx];

  var ov = document.createElement('div');
  ov.id='cx-ov';
  var d = document.createElement('div');
  d.id='cx-pp';
  d.innerHTML='<div class="h" style="background:'+ad.grad+'">'+ad.header+'<button class="x" aria-label="Fechar">×</button></div><div class="b"><img src="'+ad.img+'" alt="" loading="lazy" onerror="this.style.display=\'none\'"><div class="t"><b>'+ad.headline+'</b>'+ad.desc+'<span class="p" style="background:'+ad.badgeBg+';color:'+ad.badgeColor+'">'+ad.badge+'</span></div></div><a class="c" style="background:'+ad.grad+';box-shadow:'+ad.shadow+'" href="'+ad.link+'" target="_blank" rel="noopener sponsored">'+ad.cta+'</a><div class="f">Publicidade · Rádio RockBack FM</div>';
  document.documentElement.appendChild(ov);
  document.documentElement.appendChild(d);

  function close(){
    d.classList.remove('on');
    ov.classList.remove('on');
    d.remove();
    ov.remove();
  }
  d.querySelector('.x').onclick=close;
  ov.addEventListener('click',close);

  setTimeout(function(){
    ov.classList.add('on');
    d.classList.add('on');
  }, 2000);
})();
//]]]]><![CDATA[>
</script>]]></b:widget-setting>
      </b:widget-settings>
      <b:includable id='main'>
          <b:if cond='data:title != &quot;&quot;'>
            <h2 class='title'><data:title/></h2>
          </b:if>
          <div class='widget-content'>
            <data:content/>
          </div>
          <b:include name='quickedit'/>
        </b:includable>
    </b:widget>
    <b:widget id='HTML4' locked='false' title='' type='HTML'>
      <b:widget-settings>
        <b:widget-setting name='content'><![CDATA[<script>
//<![CDATA[
(function(){
  var s=document.createElement('style');
  s.textContent='#ton-pp{position:fixed;right:20px;bottom:110px;width:320px;max-width:calc(100vw - 40px);background:#fff;border-radius:18px;box-shadow:0 12px 32px rgba(0,0,0,.25);z-index:9998;overflow:hidden;font-family:Arial,sans-serif;transform:translateY(30px);opacity:0;transition:.35s}#ton-pp.on{transform:none;opacity:1}#ton-pp .h{color:#fff;padding:14px 40px 14px 16px;font-weight:700;font-size:14px;position:relative}#ton-pp .x{position:absolute;top:8px;right:10px;width:26px;height:26px;border-radius:50%;background:rgba(255,255,255,.2);border:0;color:#fff;font-size:16px;font-weight:700;cursor:pointer;line-height:1}#ton-pp .b{display:flex;gap:10px;padding:12px 14px;align-items:center}#ton-pp .b img{width:88px;height:88px;object-fit:cover;border-radius:14px;flex-shrink:0;background:#f2f2f2}#ton-pp .t{font-size:12.5px;color:#333;line-height:1.35}#ton-pp .t b{display:block;font-size:13.5px;color:#111;margin-bottom:4px}#ton-pp .p{display:inline-block;margin-top:6px;padding:3px 8px;border-radius:99px;font-weight:700;font-size:11px}#ton-pp .c{display:block;margin:6px 14px 14px;padding:11px 14px;border-radius:12px;color:#fff!important;text-align:center;font-weight:700;font-size:13.5px;text-decoration:none}#ton-pp .f{font-size:10px;color:#999;text-align:center;padding:0 14px 10px}@media(max-width:480px){#ton-pp{right:10px;left:10px;bottom:100px;width:auto}}';
  document.documentElement.appendChild(s);
  var AMP=String.fromCharCode(38);
  var ADS=[
    {
      header:'💰 Seja Revendedor da Maquininha Ton',
      headline:'Ganhe mais de R$ 10.000/mês',
      desc:'Revendendo a maquininha que mais cresce no Brasil.',
      badge:'Renda extra',
      cta:'👉 Quero ser Revendedor Ton',
      img:'https://blogger.googleusercontent.com/img/a/AVvXsEgqRzr9ZEB5Kx3a1n3PP_LXgQtV2RVQIM32W3S-L11iJDJ4kx-jP-NTwId-Cn8sTeMmYDaWiAzL1GwVm8SXDZ9KTE6qAaoHoheZKk6zSNsHmEme8gwJSJM_r4kHaIPi9FlfAF8Dmo2PiMHKm0Pse9vh55TZIJ_G7JvzBQt4faQ_rg33EMEJGNVDMMn_9Mlp=s1600',
      link:'https://www.ton.com.br/renda-ton/?utm_partner_id=c138c5b9-d81f-4d0d-a07e-f2988d9777ee'+AMP+'utm_source=indique_um_parceiro_nov22'+AMP+'utm_term=c138c5b9-d81f-4d0d-a07e-f2988d9777ee',
      grad:'linear-gradient(135deg,#00a651,#007a3d)',
      badgeBg:'#e6f7ee',badgeColor:'#007a3d',shadow:'0 4px 12px rgba(0,166,81,.35)'
    },
    {
      header:'🎓 Cursos e Graduação na Estácio',
      headline:'Estude com bolsa e mensalidade que cabe no bolso',
      desc:'Graduação, pós e cursos livres com desconto exclusivo.',
      badge:'Bolsa de estudo',
      cta:'👉 Ver cursos e bolsas',
      img:'https://blogger.googleusercontent.com/img/a/AVvXsEiSO8sJG93yrujuiyIXwfFu1X8_UmKwpYBtXFHoGEHW-uIiYHAz_DzY08cAlOEpT1KlW5MsXOsGyEGnqrQu8w0PgXKtPGrPLZf5j_YE4HjqbGDKohKD45euDomLlR1GRIyvdmUyaZWnVbgI_HFRo54MW4brpWcM0j9KiCzb7mqS9HcaMkhZMYr8ipDJbBLb=s1600',
      link:'https://estacio.br/selecao?cod_agente=14369444'+AMP+'u=723918'+AMP+'end=1',
      grad:'linear-gradient(135deg,#0066cc,#003d80)',
      badgeBg:'#e6f0ff',badgeColor:'#003d80',shadow:'0 4px 12px rgba(0,102,204,.35)'
    },
    {
      header:'🛍️ Ofertas imperdíveis na Shopee',
      headline:'Frete grátis e cupons todos os dias',
      desc:'Milhares de produtos com desconto no app.',
      badge:'Cupons',
      cta:'👉 Ver ofertas na Shopee',
      img:'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhltJR5XgSc9eGTaEKenDmpQMo-P2STu6uZ4CC1-QN5BEmhbWpt6qE8MG_Ss0yybPJIhM2Xw-pJ_0qC-VNi1ZPpzG2R0l45eW7sXnk4CtPefH8fxcDEfSd1u1xCBpqlAcoHLJTz-Tv_ReblfkIBAkhgH3bS69YeGOfIRJw3iR7I7wlnKzsg11AcWEU11Qs/s320/shopee.jpg',
      link:'https://s.shopee.com.br/6AlGawPZyL',
      grad:'linear-gradient(135deg,#ee4d2d,#b8391f)',
      badgeBg:'#ffe9e2',badgeColor:'#b8391f',shadow:'0 4px 12px rgba(238,77,45,.35)'
    },
    {
      header:'💸 Cashback no Méliuz',
      headline:'Ganhe dinheiro de volta em suas compras',
      desc:'Cashback em lojas como Amazon, Magalu e muito mais.',
      badge:'Cashback',
      cta:'👉 Cadastre-se no Méliuz',
      img:'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhs3iGunR7TeivWeuZonpcAPhZk7xLgWsNWUB7FY_rqwQ607a-Ck2IvZZD6SKD2rqz4KKEnMqSvj5y0RGM7r1gxmXqxXOZBT4OrAlZKEUPumx6TVIjV95-UFJMcIK5QT4a3JrGXmkrbDFKMHMFtKS_KibgwuFwOS0kM8tsPqdldK2p5-yNTssuynf5fe-I/s320/meliuz.png',
      link:'https://www.meliuz.com.br/i/ref_755524e5?ref_source=82',
      grad:'linear-gradient(135deg,#e64a19,#b23400)',
      badgeBg:'#ffe6dd',badgeColor:'#b23400',shadow:'0 4px 12px rgba(230,74,25,.35)'
    },
    {
      header:'💳 Mercado Pago sem tarifas',
      headline:'Sua conta digital gratuita e rendendo',
      desc:'Pix, cartão e rendimento automático todos os dias.',
      badge:'Conta digital',
      cta:'👉 Abrir conta no Mercado Pago',
      img:'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPl9cl8B73CnBMBXJOuMWOCxFvGLv_dzTLW9kqNxHcetItrcqq_TCesIQhgKBc5JpCcsnSdmlEhFNLNdXPGHpadO6kHxL4w6t9AHpUzRtcbj-qVCQQ7PVLWUOLxypmTCg1uQtumU56Fz58wR3HNTotFzTX0N5zG3mk1G5oButkkYVQkNhYH3q4XFjAxtQ/s320/pago.jpg',
      link:'https://mpago.li/2Q15dvf',
      grad:'linear-gradient(135deg,#ffcc00,#c79a00)',
      badgeBg:'#fff7d6',badgeColor:'#8a6b00',shadow:'0 4px 12px rgba(255,204,0,.4)',
      textColor:'#1a1a1a'
    },
    {
      header:'🛒 Magazine Você — Gnomo Shop',
      headline:'As melhores ofertas em um só lugar',
      desc:'Eletrônicos, casa, moda e muito mais com desconto.',
      badge:'Ofertas',
      cta:'👉 Visitar a Magazine Você',
      img:'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQSMTwbFMjQCjhhKeyIcmOg61q3Yx5OhkyzidiTQKZRa_NbbfFRmeWJMvr3iP4WeFsPLd9B7c5Xqcb0DHBYKP9a2O9OdaxL7XEFFdhaWwZh23vNcYtsc7L3q9AgBSU04TCAiURX5Roh7nFOBrKcUedfCflaYPBeT59ySshWAZa0t9p6iYwziVhOXsTEwo/s320/magalu.jpg',
      link:'https://www.magazinevoce.com.br/magazinegnomoshop',
      grad:'linear-gradient(135deg,#0066cc,#003a75)',
      badgeBg:'#e6f0ff',badgeColor:'#003a75',shadow:'0 4px 12px rgba(0,102,204,.35)'
    },
    {
      header:'📻 Baixe o App da Rádio RockBack FM',
      headline:'Ouça 24h de rock no seu Android',
      desc:'Aplicativo oficial da Rádio RockBack FM no Uptodown.',
      badge:'App grátis',
      cta:'👉 Baixar o App Android',
      img:'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6QItYNY4p7EMU2CUIJXcSfPuWSMzkW7Mm-ap3KdNDEON3pCY-gnKbJDAeYb7USF_adsR0NkJsGiRoGpabEhVbfqxeml0cjf09cs9N_YszNj_AkEu3ufE0lG1UsiVNQEjkqop0YdS0ObWh87elHuLq0KakSUSPdePJxPXLHHkKmdaYujhyphenhyphenbOF23dPFi8c/s320/uptodown.png',
      link:'https://radio-rockback-fm.br.uptodown.com/android',
      grad:'linear-gradient(135deg,#e2202a,#a91620)',
      badgeBg:'#ffe6e7',badgeColor:'#a91620',shadow:'0 4px 12px rgba(226,32,42,.45)'
    }
  ];
  var ad=ADS[Math.floor(Math.random()*ADS.length)];
  var txtColor=ad.textColor||'#fff';
  var d=document.createElement('div');
  d.id='ton-pp';
  d.innerHTML='<div class="h" style="background:'+ad.grad+';color:'+txtColor+'">'+ad.header+'<button class="x" aria-label="Fechar" style="color:'+txtColor+'">×</button></div><div class="b"><img src="'+ad.img+'" alt="" loading="lazy" onerror="this.style.display=\'none\'"><div class="t"><b>'+ad.headline+'</b>'+ad.desc+'<span class="p" style="background:'+ad.badgeBg+';color:'+ad.badgeColor+'">'+ad.badge+'</span></div></div><a class="c" style="background:'+ad.grad+';box-shadow:'+ad.shadow+';color:'+txtColor+'!important" href="'+ad.link+'" target="_blank" rel="noopener sponsored">'+ad.cta+'</a><div class="f">Publicidade · Rádio RockBack FM</div>';
  document.documentElement.appendChild(d);
  d.querySelector('.x').onclick=function(){d.remove()};
  setTimeout(function(){d.classList.add('on')},3000);
})();
//]]]]><![CDATA[>
</script>]]></b:widget-setting>
      </b:widget-settings>
      <b:includable id='main'>
  <!-- only display title if it's non-empty -->
  <b:if cond='data:title != &quot;&quot;'>
    <h2 class='title'><data:title/></h2>
  </b:if>
  <div class='widget-content'>
    <data:content/>
  </div>

  <b:include name='quickedit'/>
</b:includable>
    </b:widget>
    <b:widget id='HTML2' locked='false' title='Redes Sociais' type='HTML' version='2' visible='true'>
      <b:widget-settings>
        <b:widget-setting name='content'>&#169; Rádio RockBack FM &#8212; Todos os direitos reservados. Rock 24 horas por dia.</b:widget-setting>
      </b:widget-settings>
      <b:includable id='main'>
        <div class='footer-inner'>
          <div class='widget-content'><data:content/></div>
        </div>
      </b:includable>
    </b:widget>
  </b:section>
</div>

<!-- ============================================================ -->
<!-- PLAYER FLUTUANTE &#8212; COM EFEITO DE LOADING                     -->
<!-- ============================================================ -->
<div class='rb-floating-player' id='rbFloatingPlayer'>
  <div class='rb-fp-cover'>
    <img alt='RockBack FM' src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVtXqb5bwqXrPTeXWIkzASDRo6DKJTc3mjUEet2fVy9Lo4rQ15fDP9Vn8dQ8wX9yC840f5fSuqmfEuH5a9ecnaiIsJjheXJvrQdf4iCRw2NdnYYRRZSPxsIA3h1MUscQM2RiV8bdAwprjmbUDYMmA5a2kPxY8oyKbQeV1jn2hWxjGbxHYAfuEUCDGSNxQ/s200/R%C3%A1dio%20RockBack%20FM%20Logo%20Trasparente.png'/>
  </div>
  <div class='rb-fp-info'>
    <div class='rb-fp-status'>
      <span class='rb-fp-dot'/> AO VIVO
    </div>
    <div class='rb-fp-title' id='rbFpTitle'>Rádio RockBack FM</div>
    <div class='rb-fp-artist' id='rbFpArtist'>Ao Vivo</div>
  </div>
  <div class='rb-fp-time' id='rbFpTime'>00:00</div>
  <div class='rb-fp-controls'>
    <button aria-label='Volume' class='rb-fp-btn' type='button'>
      <svg viewBox='0 0 24 24'><path d='M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z'/></svg>
    </button>
    <button aria-label='Play/Pause' class='rb-fp-play' id='rbFpPlay' type='button'>
      <svg class='icon-play' viewBox='0 0 24 24'><path d='M8 5v14l11-7z'/></svg>
      <svg class='icon-pause' viewBox='0 0 24 24'><path d='M6 19h4V5H6v14zm8-14v14h4V5h-4z'/></svg>
    </button>
    <button aria-label='Curtir' class='rb-fp-btn' type='button'>
      <svg viewBox='0 0 24 24'><path d='M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z'/></svg>
    </button>
  </div>
  <div class='rb-fp-progress'><div class='rb-fp-progress-bar' id='rbFpProgressBar'/></div>
</div>

<!-- ============================================================ -->
<!-- ABA OCULTA DE TRADUÇÃO                                       -->
<!-- ============================================================ -->
<button aria-label='Traduzir página' class='rb-translate-toggle' id='rbTranslateToggle' type='button'>
  <svg viewBox='0 0 24 24'><path d='M12.87 15.07l-2.54-2.51.03-.03c1.74-1.94 2.98-4.17 3.71-6.53H17V4h-7V2H8v2H1v1.99h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11.76-2.04zM18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2l-4.5-12zm-2.62 7l1.62-4.33L19.12 17h-3.24z'/></svg>
</button>

<div class='rb-translate-panel' id='rbTranslatePanel'>
  <div class='rb-translate-lbl'>🌐 Traduzir página</div>
  <a data-lang='pt' href='#' onclick='rbSetLang(&quot;pt&quot;);return false;'>
    <span class='flag'>🇧🇷</span> Português
  </a>
  <a data-lang='en' href='#' onclick='rbSetLang(&quot;en&quot;);return false;'>
    <span class='flag'>🇺🇸</span> English
  </a>
  <a data-lang='es' href='#' onclick='rbSetLang(&quot;es&quot;);return false;'>
    <span class='flag'>🇪🇸</span> Español
  </a>
</div>

<!-- Elemento escondido do Google Translate -->
<div id='google_translate_element'/>

<!-- ============================================================ -->
<!-- SCRIPTS                                                       -->
<!-- ============================================================ -->

<script type='text/javascript'>
//<![CDATA[
function googleTranslateElementInit() {
  new google.translate.TranslateElement({
    pageLanguage: 'pt',
    includedLanguages: 'en,es',
    autoDisplay: false
  }, 'google_translate_element');
}
//]]>
</script>
<script async='async' src='//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit' type='text/javascript'/>

<script type='text/javascript'>
//<![CDATA[
(function(){
  var API = 'https://api.zeno.fm/mounts/metadata/subscribe/bl80vqtgsemuv';
  var rbFpPlay = document.getElementById('rbFpPlay');
  var rbFpTitle = document.getElementById('rbFpTitle');
  var rbFpArtist = document.getElementById('rbFpArtist');
  var rbFpTime = document.getElementById('rbFpTime');
  var rbFpProgressBar = document.getElementById('rbFpProgressBar');
  var rbFloatingPlayer = document.getElementById('rbFloatingPlayer');

  var audio = document.createElement('audio');
  audio.id = 'rbAudioStream';
  audio.src = 'https://stream.zeno.fm/bl80vqtgsemuv';
  audio.preload = 'none';
  audio.crossOrigin = 'anonymous';
  document.body.appendChild(audio);

  function atualizarBotoes(){
    if (!audio.paused){
      if (rbFpPlay) rbFpPlay.classList.add('tocando');
      if (rbFloatingPlayer) rbFloatingPlayer.classList.add('tocando');
    } else {
      if (rbFpPlay) rbFpPlay.classList.remove('tocando');
      if (rbFloatingPlayer) rbFloatingPlayer.classList.remove('tocando');
    }
  }

  function togglePlay(){
    if (audio.paused){ audio.play().catch(function(){}); }
    else { audio.pause(); }
  }

  if (rbFpPlay) rbFpPlay.addEventListener('click', togglePlay);
  audio.addEventListener('play', atualizarBotoes);
  audio.addEventListener('pause', atualizarBotoes);

  var startTime = Date.now();
  setInterval(function(){
    if (audio.paused) return;
    var elapsed = Math.floor((Date.now() - startTime) / 1000);
    var m = Math.floor(elapsed / 60);
    var s = elapsed % 60;
    if (rbFpTime) rbFpTime.textContent = (m < 10 ? '0' + m : m) + ':' + (s < 10 ? '0' + s : s);
  }, 1000);

  function limpar(t){
    return String(t||'').replace(/\.(mp3|m4a|aac|ogg|wav)$/i,'').trim();
  }
  function atualizarNP(){
    fetch(API, {cache:'no-store'})
      .then(function(r){ return r.json(); })
      .then(function(d){
        var a = limpar(d.currentArtist||'');
        var m = limpar(d.currentSong||'');
        if (!a && !m && d.title){
          var p = d.title.split(' - ');
          if (p.length >= 2){ a = p[0]; m = p.slice(1).join(' - '); }
          else { m = d.title; }
        }
        if (a && m){
          if (rbFpTitle) rbFpTitle.textContent = m;
          if (rbFpArtist) rbFpArtist.textContent = a;
        } else if (m){
          if (rbFpTitle) rbFpTitle.textContent = m;
          if (rbFpArtist) rbFpArtist.textContent = 'RockBack FM';
        } else {
          if (rbFpTitle) rbFpTitle.textContent = 'Rádio RockBack FM';
          if (rbFpArtist) rbFpArtist.textContent = 'Ao Vivo';
        }
      })
      .catch(function(){
        if (rbFpTitle) rbFpTitle.textContent = 'Rádio RockBack FM';
        if (rbFpArtist) rbFpArtist.textContent = 'Ao Vivo';
      });
  }
  atualizarNP();
  setInterval(atualizarNP, 8000);

  window.rbSetLang = function(lang){
    var host = window.location.hostname;
    var expirado = 'expires=Thu, 01 Jan 1970 00:00:00 GMT';
    document.cookie = 'googtrans=;path=/;' + expirado;
    document.cookie = 'googtrans=;path=/;domain=.' + host + ';' + expirado;
    document.cookie = 'googtrans=;path=/;domain=' + host + ';' + expirado;

    if (lang && lang !== 'pt'){
      document.cookie = 'googtrans=/pt/' + lang + ';path=/';
      document.cookie = 'googtrans=/pt/' + lang + ';path=/;domain=.' + host;
      document.cookie = 'googtrans=/pt/' + lang + ';path=/;domain=' + host;
    }
    window.location.reload();
  };

  (function(){
    var m = document.cookie.match(/googtrans=\/pt\/([a-z]{2})/i);
    var lang = m ? m[1].toLowerCase() : 'pt';
    var links = document.querySelectorAll('.rb-translate-panel a');
    for (var i = 0; i < links.length; i++){
      var l = links[i].getAttribute('data-lang');
      if (l === lang) links[i].classList.add('on');
    }
  })();

  var toggle = document.getElementById('rbTranslateToggle');
  var panel = document.getElementById('rbTranslatePanel');
  if (toggle && panel){
    toggle.addEventListener('click', function(e){
      e.stopPropagation();
      panel.classList.toggle('aberto');
    });
    document.addEventListener('click', function(){
      panel.classList.remove('aberto');
    });
    panel.addEventListener('click', function(e){
      e.stopPropagation();
    });
  }
})();
//]]>
</script>

<!-- ============================================================ -->
<!-- LANÇAMENTOS DO ROCK - AUTOMÁTICO VIA RSS (LIMITE DE 10 ITENS)-->
<!-- ============================================================ -->
<script type='text/javascript'>
//<![CDATA[
(function(){
  var container = document.getElementById('rb-releases-list');
  var loadingEl = document.getElementById('rb-releases-loading');
  var panel = document.getElementById('rb-rock-releases');
  var toggleBtn = document.getElementById('rb-releases-toggle');
  
  if (!container || !panel || !toggleBtn) return;

  // URL do Feed RSS de notícias (Wikimetal) e Proxy para evitar erro de CORS
  var RSS_URL = 'https://www.wikimetal.com.br/feed/';
  var PROXY_URL = 'https://api.allorigins.win/get?url=' + encodeURIComponent(RSS_URL);
  
  var loaded = false;
  var loading = false;

  function formatarData(dataStr) {
    if (!dataStr) return '';
    try {
      var d = new Date(dataStr);
      return d.toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit', year: 'numeric' });
    } catch(e) { return ''; }
  }

  function extrairArtistaAlbum(titulo) {
    // Remove prefixos comuns de notícias
    var limpo = titulo.replace(/^(Rock and metal releases of the week:|Lançamentos de rock e metal da semana:|Novo álbum:|Novo disco:|Resenha:)\s*/i, '').trim();
    
    // Tenta separar por " – " ou " - "
    var partes = limpo.split(/\s[-–]\s/);
    
    if (partes.length >= 2) {
      return { artista: partes[0].trim(), album: partes[1].trim() };
    }
    
    // Fallback caso não tenha o separador claro
    return { artista: limpo, album: 'Lançamento' };
  }

  function renderReleases(items) {
    container.innerHTML = '';
    
    if (!items || items.length === 0) {
      if (loadingEl) {
        loadingEl.style.display = 'block';
        loadingEl.textContent = 'Nenhum lançamento recente encontrado.';
      }
      return;
    }

    if (loadingEl) loadingEl.style.display = 'none';

    // Limita a 10 itens
    var displayItems = items.slice(0, 10);

    displayItems.forEach(function(item) {
      var div = document.createElement('div');
      div.style.cssText = 'padding:10px 0; border-bottom:1px dashed var(--border-soft); font-size:13.5px; line-height:1.5;';

      var dataFormatada = formatarData(item.pubDate);
      var link = item.link || '#';
      var info = extrairArtistaAlbum(item.title);

      // Formato: Artista – Álbum (Data)
      div.innerHTML = '<strong style="color:var(--red); font-weight:600;">' + info.artista + '</strong> – ' +
                      '<a href="' + link + '" target="_blank" rel="noopener" style="color:var(--cream); text-decoration:none; font-style:italic;">' + info.album + '</a> ' +
                      '<span style="color:var(--text-2); font-size:11px;">(' + dataFormatada + ')</span>';

      container.appendChild(div);
    });
  }

  function fetchReleases() {
    if (loadingEl) {
      loadingEl.style.display = 'block';
      loadingEl.textContent = 'Buscando lançamentos...';
    }

    fetch(PROXY_URL)
      .then(function(response) { return response.json(); })
      .then(function(data) {
        loaded = true;
        loading = false;
        
        if (!data || !data.contents) throw new Error('Feed vazio');

        var parser = new DOMParser();
        var xmlDoc = parser.parseFromString(data.contents, 'text/xml');
        var items = xmlDoc.querySelectorAll('item');
        
        var releases = [];
        
        // Filtra as notícias para pegar apenas o que parece ser lançamento
        for (var i = 0; i < items.length; i++) {
          var title = items[i].querySelector('title').textContent;
          var pubDate = items[i].querySelector('pubDate') ? items[i].querySelector('pubDate').textContent : '';
          var link = items[i].querySelector('link').textContent;

          var tLower = title.toLowerCase();
          if (tLower.indexOf('lançamento') !== -1 || 
              tLower.indexOf('álbum') !== -1 || 
              tLower.indexOf('releases') !== -1 ||
              tLower.indexOf('disco') !== -1) {
            
            releases.push({ title: title, pubDate: pubDate, link: link });
          }
        }

        renderReleases(releases);
      })
      .catch(function(error) {
        loaded = false;
        loading = false;
        console.error('Erro no RSS:', error);
        if (loadingEl) {
          loadingEl.style.display = 'block';
          loadingEl.textContent = 'Não foi possível carregar os lançamentos agora.';
        }
      });
  }

  window.rbLoadReleases = function() {
    if (loaded || loading) return;
    loading = true;
    fetchReleases();
  };

  toggleBtn.addEventListener('click', function() {
    var isOpen = panel.classList.contains('aberto');
    if (isOpen) {
      panel.classList.remove('aberto');
      toggleBtn.classList.remove('aberto');
      toggleBtn.setAttribute('aria-expanded', 'false');
    } else {
      panel.classList.add('aberto');
      toggleBtn.classList.add('aberto');
      toggleBtn.setAttribute('aria-expanded', 'true');
      window.rbLoadReleases();
    }
  });

})();
//]]>
</script>

</body>
</html>
