import os

# Configurações do WordPress puxadas dos Secrets (não usado, mas mantido)
WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")

# Configurações do Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-1.5-flash"

# Configurações de Postagem
WP_POST_STATUS = "draft"
ARTICLES_PER_RUN = 3

# Fontes de notícias de Rock/Metal
RSS_FEEDS = [
    ("Rock Notícias", "https://www.rocknoticias.com.br"),
    ("Whiplash.net", "https://whiplash.net")
]
