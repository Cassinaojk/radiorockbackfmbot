# Rádio RockBack FM — Robô de Notícias 1.0

Robô GitHub Actions para coletar notícias de fontes de rock/metal, gerar matérias originais em português do Brasil com IA e publicar no Blogger.

## Fontes ativas (2)

| Fonte | URL base | Feed principal |
|---|---|---|
| Rock Notícias | https://www.rocknoticias.com.br/ | `feed/` |
| Whiplash.net | https://whiplash.net/ | `feed/` |

## IA (provedores em ordem de fallback)
1. **Gemini** — modelo principal `gemini-3.5-flash-lite`
2. **Gemini-2** — modelo fallback `gemini-3.6-flash`
3. **Groq** — modelo `openai/gpt-oss-20b`
4. **Mistral** — modelo `mistral-small-latest`

- Até **6 chamadas de texto por execução** (`MAX_GEMINI_TEXT_CALLS_PER_RUN=6`).
- Ao detectar quota/limite em um provedor, o robô passa automaticamente para o próximo.
- Se todos os provedores atingirem quota, a execução para e o restante fica para a próxima.

## Publicação
- Até **1 matéria por execução** (`MAX_POSTS_PER_RUN=1`).
- Deduplicação por URL da fonte e por URL do blog.
- A imagem do post é a **imagem original** extraída da notícia da fonte.
- Vídeos incorporados (YouTube, Vimeo, etc.) são extraídos automaticamente da fonte.
- A fonte fica registrada em comentário HTML invisível (`RADIO_ROCKBACK_FM_SOURCE_URL`).
- Spotify embed aparece após a matéria.

## Filtro de Rock/Metal
O robô usa uma lista de **termos fortes** (`rock`, `metal`, `heavy metal`, `hard rock`, `punk`, `grunge`, `indie`, `alternativo`, `progressivo`, `glam`, `new metal`, etc.) e **termos de suporte** (`cantor`, `banda`, `guitarrista`, `baixista`, `baterista`, `gravadora`, `compositor`, etc.) para decidir se uma notícia é de rock/metal.
- Se houver dúvida, a regra é **publicar**.
- Posts de rock recebem a label `Rock`; os demais ficam apenas com `Notícias` e `Rádio RockBack FM`.

## Originalidade
A verificação bloqueia apenas sinais fortes de reprodução literal:
- sequência de **15 palavras ou mais** idênticas à fonte;
- sobreposição de **8-grams acima de 12%**.

## Secrets necessários
- `BLOGGER_BLOG_ID`
- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `BLOGGER_REFRESH_TOKEN`
- `GEMINI_API_KEY`

### Secrets opcionais
- `GEMINI_API_KEY_2` (segunda chave Gemini)
- `GROQ_API_KEY`
- `MISTRAL_API_KEY`

## Variáveis de ambiente opcionais
- `VERBOSE_LOG=true` — ativa log detalhado
- `MAX_POSTS_PER_RUN` — padrão `1`
- `MAX_GEMINI_TEXT_CALLS_PER_RUN` — padrão `6`
- `GEMINI_MODEL` / `GEMINI_FALLBACK_MODEL`
- `GROQ_MODEL` / `MISTRAL_MODEL`
