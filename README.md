# Analisador de Arquivo CSV de Vendas

Este projeto tem como objetivo analisar dados de vendas de um arquivo CSV e gerar informações úteis, como:

- Total vendido por produto
- O dia com maior valor em vendas
- O produto mais vendido (em quantidade)
- Exportação do relatório em Excel (.xlsx)

## 📄 Descrição do Projeto

```yaml
project:
  name: Analisador de Arquivo CSV de Vendas
  description: |
    Este projeto visa fornecer uma análise completa dos dados de vendas de um arquivo CSV. A partir dos dados fornecidos, o script realiza cálculos como o total vendido por produto, identifica o dia com mais vendas, e determina o produto mais vendido (em quantidade).
    Além disso, os resultados podem ser exportados para uma planilha Excel (.xlsx) para facilitar a visualização e o armazenamento dos dados.
    
  concepts:
    - Pandas: Manipulação de dados tabulares
    - Leitura e gravação de arquivos CSV e Excel
    - Agrupamento de dados com `groupby`
    - Cálculos e agregações de dados
    - Exportação de dados para planilha (.xlsx) usando `openpyxl`
    - Análise de vendas e geração de relatórios
    
  prerequisites:
    - Python 3.x
    - Ambiente virtual (opcional, mas recomendado)
    - Bibliotecas necessárias: `pandas`, `openpyxl`

  installation:
    steps:
      - Clone o repositório:
        command: git clone 
      - Navegue para o diretório do projeto:
        command: cd Projeto_Analise_arquivos_CSV
      - Crie o ambiente virtual (opcional):
        command: python -m venv .venv
      - Ative o ambiente virtual:
        windows: .\.venv\Scripts\Activate
        linux: source .venv/Scripts/activate
      - Instale as dependências:
        command: pip install -r requirements.txt
      - Execute o script principal:
        command: python Analise_vendas.py
