import pandas as pd
import matplotlib.pyplot as plt
#Lê o arquivo CSV
#O encoding é o "tradutor" entre o que está salvo no arquivo e o que o Python entende.
"""
utf-8  É o mais usado no mundo todo, funciona bem com vários idiomas. Mas nem sempre funciona com arquivos feitos no Windows/Excel BR.

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
"""
groupby('Data') => agrupa por data.
"""

#DESCOBRE O DIA COM MAIS VENDAS 

#Agrupando os dados por data e soma os totais de cada dia
total_por_dia = df.groupby('Data')['Total'].sum()

#Descobre qual foi o dia com mais vendas 
dia_mais_vendas = total_por_dia.idxmax()
"""
idxmax() => pega o índice do maior valor (nesse caso, a data).
"""

#Descobre o valor total vendido nesse dia
valor_mais_vendas = total_por_dia.max()
"""
.max() => pega o maior valor da tabela.
"""

#Exibindo na tela
print("\n===Dia com mais vendas===")
print(f"Dia com mais vendas: {dia_mais_vendas} - Total: R${valor_mais_vendas}")
"""
f"" permite colocar variáveis dentro da string com {}.
"""

#Parte 3  doscobrindo qual foi o produto mais vendido em quantidade

#Agrupa por produto e soma a quantidade total vendida de cada dia 
quantidade_produto = df.groupby('Produto')['Quantidade'].sum()

"""
Queremos saber qual produto vendeu mais unidades, tipo:
Mouse: 47
Teclado: 15
"""

#Decobre o produto com mais unidade vendidas
produto_mais_vendido = quantidade_produto.idxmax()
qtd_mais_vendida = quantidade_produto.max()

"""
.idxmax() => vai mostrar o nome do produto com mais unidades

.max() => vai mostrar quantas unidades foram vendidas
"""

print("\n===Produto mais vendido===")
print(f"produto mais vendido: {produto_mais_vendido} - Quantidade: {qtd_mais_vendida}")

#Salvando o arquivo CSV em Xlsx
df.to_excel("Produtos_convertido.xlsx", index=False, engine="openpyxl")

"""
Entendendo o index
index=True (padrão): Salva a coluna com os números da linha.

index=False: Remove essa coluna na hora de salvar. Fica mais limpo.

"""

#Dados para grafico
produtos = list(total_por_produto.index) # cria uma Lista com os nomes dos produtos
valores = list(total_por_produto.values) # cria uma lista com o total vendido de cada produto  

#criando o grafico 
plt.figure(figsize=(8, 5)) #Define o tamanho da imagem 
plt.bar(produtos, valores, color = 'skyblue')

#Criando o grafico em pizza
plt.figure(figsize=(8, 8)) #Deixa o grafico quadrado

plt.pie(
    valores,
    labels = produtos,
    autopct='%1.1f%%',  #Mostra as porcentagens com 1 casa decimal
    startangle= 90,  #começa o grafico a partir do topo 
    shadow= True #adiciona uma sombra 
)
plt.savefig("Participação nas Vendas por Produto")
plt.tight_layout() #ajusta pra não cortar o texto 


#Personalizando
plt.title('Total Vendido por Produto') #Titulo
plt.xlabel('Produto')  #Nome do eixo x
plt.ylabel('Total em R$') #nome do eixo y
plt.xticks(rotation= 90)  # gira os nomes 90 graus

#Salvando como PNG antes de exibir 
plt.savefig("Grafico_vendas.png", dpi= 300, bbox_inches='tight')
plt.savefig("Grafico_vendas_pizza.png", dpi=300, bbox_inches='tight')
"""
- 'grafico_vendas.png': nome do arquivo.
- dpi=300: qualidade boa pra impressão.
- bbox_inches='tight': ajusta o corte do gráfico pra não sair cortado.
"""
#Exibindo o grafico na tela 
plt.show()

print("Arquivo convertido com sucesso!")