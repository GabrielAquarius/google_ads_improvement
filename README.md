# README: Projeto de Automação de Palavras-Chave e Personas para AdWords

## Visão Geral do Projeto
Este projeto tem como objetivo automatizar a geração de personas, sugestões de palavras-chave e campanhas relevantes no AdWords para otimizar o direcionamento de anúncios do Google. O sistema integra diversos módulos para gerar termos de pesquisa baseados em personas e analisar seu desempenho na conversão de cliques em vendas. Os principais componentes do projeto incluem criação de personas, geração de palavras-chave e automação de campanhas no Google Ads.

### Principais Módulos
1. **Gerador de Personas**:
   - Coleta e gera perfis detalhados de personas.
   - Suporta prompts em línguas diferentes (inglês e português).
   - Salva um arquivo JSON com os dados enriquecidos das personas para uso posterior.

2. **Gerador de Palavras**:
   - Utiliza os perfis de personas para gerar sugestões de palavras-chave relevantes.
   - Usa modelos LLM (como Llama) para criar termos de busca personalizados baseados nas características das personas.

3. **Gerador de Tabelas**:
   - Consulta a API de Pesquisa Personalizada do Google com as palavras-chave geradas.
   - Armazena os resultados da pesquisa em um arquivo Excel para análise.

4. **Gerador de Perfis**:
   - Automatiza interações com o Google (ex.: criação de contas, consumo de conteúdo).
   - Utiliza Selenium para automação web.

### Documentos e Arquivos Suporte
- **How Google Ads Work.txt**: Explica os fundamentos do Google Ads, incluindo Ad Rank e Quality Score.
- **Key Word Automation.txt**: Discute desafios e hipóteses na automação de palavras-chave.
- **prompt_persona.txt**: Fornece descrições detalhadas de personas para teste e ajustes.
- **AdWords Keyword Match Types.jpg**: Guia visual sobre tipos de correspondência de palavras-chave.
- **Google Ads Account Structure.jpg**: Diagrama da estrutura de conta para campanhas.

---

## Pré-Requisitos
Antes de executar o projeto, garanta que as seguintes dependências estejam instaladas:

### Softwares Necessários
- Python 3.8+
- Navegador Google Chrome e ChromeDriver

### Bibliotecas e Módulos
- `pandas`
- `requests`
- `json`
- `re`
- `selenium`
- `ollama`

---

## Instalação
1. Clone o repositório.
2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure os arquivos `GOOGLE_SEARCH_API` e `SEARCH_ENGINE_ID` com as chaves apropriadas.
4. Configure o ChromeDriver para automação com Selenium.

---

## Como Executar

1. **Gerar Personas**:
   ```bash
   python persona_generator.py
   ```

2. **Gerar Palavras-Chave**:
   ```bash
   python word_generator.py
   ```

3. **Criar Tabela de Resultados de Pesquisa**:
   ```bash
   python table_generator.py
   ```

4. **Automatizar Perfil do Google**:
   ```bash
   python profile_generator.py
   ```

---

## Saídas
- `personas.json`: Contém perfis detalhados de personas.
- `table_generated.xlsx`: Arquivo Excel com resultados de pesquisa das palavras-chave geradas.
- `cookies.json`: Armazena dados de sessão para interações automatizadas no Google.

---

## Melhorias Futuras
- Melhorar a relevância das palavras-chave com ajuste avançado de LLM.
- Implementar um mecanismo de scraping mais robusto.
- Adicionar suporte para geração de palavras-chave multilíngues.
- Integrar a API do Google Ads para gerenciamento direto de campanhas.

---

## Autor
Desenvolvido por [Seu Nome ou Nome da Equipe]. Para perguntas ou contribuições, entre em contato pelo e-mail [Seu Endereço de E-mail].
