# BBC AI Vocabulary Agent

Agente de IA local que acessa a seção Technology da BBC e extrai automaticamente novas palavras em inglês utilizando um modelo LLM executando localmente.

O sistema evita palavras repetidas utilizando SQLite.

---

## Funcionalidades

- Scraping da BBC Technology
- Extração automática de 10 palavras
- Tradução para português
- Frase de exemplo
- Persistência local com SQLite
- IA local com Ollama + Llama 3
- Sem APIs pagas

---

## Tecnologias

- Python
- Requests
- BeautifulSoup
- SQLite
- Ollama
- Llama 3

---

## Instalação

Clone o projeto:

```bash
git clone https://github.com/SEU_USUARIO/bbc_ai_agent.git

cd bbc_ai_agent
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Instale o Ollama:

https://ollama.com

Baixe o modelo:

```bash
ollama run llama3
```

---

## Execução

Inicie o Ollama:

```bash
ollama run llama3
```

Execute o agente:

```bash
python main.py
```

---

## Exemplo de saída

```bash
Palavra: breakthrough
Tradução: avanço
Exemplo: The company announced a major breakthrough.
```

---

## Estrutura

```bash
bbc_ai_agent/
│
├── main.py
├── scraper.py
├── ai_processor.py
├── database.py
├── config.py
├── requirements.txt
└── words.json
```

---

## Melhorias Futuras

- Interface desktop
- Flashcards
- Integração com Anki
- Exportação CSV
- Automação diária
- Quiz de vocabulário