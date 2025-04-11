import pandas as pd

#Lê o arquivo CSV
#O encoding é o "tradutor" entre o que está salvo no arquivo e o que o Python entende.
"""
utf-8 → É o mais usado no mundo todo, funciona bem com vários idiomas. Mas nem sempre funciona com arquivos feitos no Windows/Excel BR.

latin1 ou ISO-8859-1 → Muito usado em arquivos salvos no Windows/Excel em português. Ele entende acentos e cedilha tipo: "ação", "coração", "maçã", "peça".
"""
df = pd.read_csv("Produtos.csv", encoding='latin1')

#Mostra os dados 
print("===Dados de Vendas===")
print(df)

#Adiciona um nova coluna 'Total' que é quantidade*preço
df['Total'] = df['Quantidade'] * df['Preço']

#Agrupa por produto e oma os totais
#O pandas tá organizando a tabela por produto.
"""
Exemplo:
Se tiver várias linhas com "Arroz", ele junta tudo isso em um grupo.
Mesma coisa com "Feijão", "Macarrão", etc.
"""

"""
['Total']
Depois de agrupar por produto, a gente fala:
"Agora quero só olhar pra coluna 'Total' de cada grupo."

Ou seja, ele ignora as outras colunas (como data, preço, etc).

"""
"""
Sum() soma os valores da coluna 'Total' que estavam agrupados.
 Exemplo prático: Se "mouse" tem duas vendas:

R$30,00

R$45,00

Ele soma → R$75,00 como total vendido do mouse.
"""
total_por_produto = df.groupby('Produto')['Total'].sum() 
