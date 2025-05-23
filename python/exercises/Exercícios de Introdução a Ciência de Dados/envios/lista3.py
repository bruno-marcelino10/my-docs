# %% [markdown]
# # Lista 03 - Análise Exploratória de Dados
# 
# Continuando da última lista, vamos agora realizar um pouco dos passos da análise exploratória de dados. Em particular, vamos passar pelos passos de:
# 
# 1. Carregamento dos dados
# 1. Limpeza dos dados
# 1. Análise exploratória com gráficos e estatísticas simples
# 
# ## Imports Básicos
# 
# As células abaixo apenas configuram nosso notebook para ficar mais parecido com os das aulas

# %%
from numpy.testing import assert_almost_equal
from numpy.testing import assert_equal

from numpy.testing import assert_array_almost_equal
from numpy.testing import assert_array_equal

# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# %%
plt.rcParams['figure.figsize']  = (16, 10)
plt.rcParams['axes.labelsize']  = 20
plt.rcParams['axes.titlesize']  = 20
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['lines.linewidth'] = 4

# %%
plt.ion()
plt.style.use('seaborn-colorblind')

# %% [markdown]
# ## Notas dos Alunos (Tutorial)
# 
# Como falamos na última lista, em muitos cenários do mundo real, os dados são carregados de fontes como arquivos. Vamos substituir o DataFrame das notas dos alunos pelo conteúdo de um arquivo de texto. 

# %%
df = pd.read_csv('https://raw.githubusercontent.com/icd-ufmg/icd-ufmg.github.io/master/listas/l3/grades.csv',
                 sep=',',
                 header=0)
df.head()

# %% [markdown]
# O método `read_csv` do `DataFrame` é usado para carregar dados de arquivos de texto. Como você pode ver no código de exemplo, você pode especificar opções como o delimitador de coluna e qual linha (se houver) contém cabeçalhos de coluna (neste caso, o delimitador é uma vírgula e a primeira linha contém os nomes das colunas).
# 
# Além do mais, a chamada `head` imprime as primeiras cinco linhas da nossa tabela.

# %% [markdown]
# ### Dados Faltantes
# 
# Um dos problemas mais comuns com os quais os cientistas de dados precisam lidar são dados incompletos ou ausentes. Como podemos saber que o DataFrame contém valores ausentes? Você pode usar o método `isnull` para tal tarefa.

# %%
df.isnull()

# %% [markdown]
# Obseve como a última linha falta com o número de horas estudadas. Nas dúas últimas, faltam as notas. Caso você deseja saber a quantidade de dados faltantes, basta somar os `True`s da tabela acima. Aqui é importante saber que Python tratta `True` de forma similar ao número 1. Portanto, basta você somar a tabela inteira para pegar tal quantidade de dados faltantes.

# %%
df.isnull().sum()

# %% [markdown]
# Lembrando que a chamada `iloc` pega uma linha com base no número da mesma, vamos observar a última linha da tabela de dados. Observe como os valores faltantes viram `NaN`s. Além do mais, lembre-se que podemos indexar de trás para frente com o -1. -1 é a última linha, -2 a penúltima. Para entender a lógica, em um vetor de tamanho `n`, `n-1` é o último elemento. Indexar `-1` indica `n-1`.

# %%
df.iloc[-1]

# %% [markdown]
# A penúltima.

# %%
df.iloc[-2]

# %% [markdown]
# Agora que encontramos os valores faltantes, o que podemos fazer a respeito deles?
# 
# #### fillna
# 
# Uma abordagem comum é imputar valores de substituição. Por exemplo, se o número de horas de estudo está faltando, podemos simplesmente supor que o aluno estudou por um período médio de tempo e substituir o valor faltante com as horas de estudo médias. Para fazer isso, podemos usar o método fillna, como este:

# %%
df['StudyHours'].fillna(df['StudyHours'].mean())

# %% [markdown]
# Observe que a última linha foi alterada! Porém, o DataFrame original não foi.

# %%
df.iloc[-1]

# %% [markdown]
# Para alterar, podemos trocar a coluna. Abaixo faço tal operação em uma cópia dos dados. Realizei tal escolha apenas para não mudar a tabela original.

# %%
df_novo = df.copy() # criar uma cópia apenas para o exemplo
df_novo['StudyHours'] = df_novo['StudyHours'].fillna(df_novo['StudyHours'].mean())
df_novo.iloc[-1]

# %% [markdown]
# Observe como não mudamos nada das notas. O `fillna` pode receber uma série indexada para alterar várias colunas. Primeiramente, observe como a chamada `mean` pega a média de todas as colunas.

# %%
df.mean()

# %% [markdown]
# O `fillna` então vai pegar o índice dessa série, o nome da coluna, e utilizar como chave para quais colunas imputar. O valor da série indica o valor que será imputado. Observe como os novos dados abaixo estão sem NaNs.

# %%
df_novo = df.fillna(df.mean())
df_novo

# %%
df_novo.isnull().sum()

# %% [markdown]
# #### dropna
# 
# Outra opção é simplesmente remover todas as linhas com dados faltantes. Para tal, fazemos uso da chamada `dropna`.

# %%
df_novo = df.dropna()
df_novo.shape

# %%
df.shape

# %% [markdown]
# Observe como o novo DataFrame tem duas linhas a menos do que o anterior. A escolha de como limpar dados faltantes depende do tipo de análise que você vai realizar. Aqui, vamos seguir com o drop no `df`.

# %%
df.dropna(inplace=True) # on inplace=True altera o dataframe atual, não retorna um novo
df

# %% [markdown]
# ### Explorando Dados
# 
# Lembre-se que você pode indexar DataFrames com vetores booleanos. Por exemplo, para pegas as notas de Skye podemos primeiramente achar a discente nos dados:

# %%
df['Name'] == 'Skye'

# %% [markdown]
# Obserne como acima temos uma entrada verdadeira. Esta, é justamente a linha onde temos o nome `Skye`. Ao indexar o DataFrame com tal linha, pegamos a nota da discente.

# %%
idx = df['Name'] == 'Skye'
df[idx]

# %% [markdown]
# Outra forma de fazer a mesma operação é com o método **query**. O query faz consultados usando uma línguagem similar aos bancos de dados. Um exemplo:

# %%
df.query('Name == "Skye"')

# %% [markdown]
# Podemos também pegar todas as notas acima de 60. Ou seja, os alunos aprovados.

# %%
df.query('Grade >= 60')

# %% [markdown]
# Como também os alunos que passaram estudando relativamente pouco.  No nosso caso, vamos focar em alunos que estudaram menos do que 14horas.

# %%
df.query('Grade >= 60 and StudyHours <= 14')

# %% [markdown]
# Todo retorno, ou do índice booleano ou da query são outros DataFrames. Então, podemos chamar métodos como tirar a média dos alunos.

# %%
above_60_low_hours = df.query('Grade >= 60 and StudyHours <= 14')
type(above_60_low_hours)

# %%
above_60_low_hours.mean()

# %% [markdown]
# Podemos também buscar os alunos que estão acima da média!

# %%
mean = df['Grade'].mean()
df[df['Grade'] >= mean]

# %% [markdown]
# ou, via query.

# %%
df.query(f'Grade >= {mean}')

# %% [markdown]
# Os DataFrames são incrivelmente versáteis e facilitam a manipulação de dados. Muitas operações DataFrame retornam uma nova cópia do DataFrame; portanto, se quiser modificar um DataFrame, mas manter a variável existente, você precisará atribuir o resultado da operação à variável existente. Por exemplo, o código a seguir classifica os dados do aluno em ordem decrescente de nota e atribui o DataFrame classificado resultante à variável `df_students`. 

# %%
# Re-ordena os dados por nota
df_students = df.sort_values('Grade', ascending=False)
df_students

# %% [markdown]
# ### Visualizando dados com Matplotlib
# 
# Os DataFrames fornecem uma ótima maneira de explorar e analisar dados tabulares, mas uma imagem vale mil palavras. A biblioteca [Matplotlib](matplotlib.org) fornece a base para a plotagem de visualizações de dados.
# 
# Vamos começar com um histograma de notas. Observe como também colocamos uma linha preta em cada barra `edgecolor='k'` e setamos rótulos ao X e Y (para sabermos qual eixo mostra quais dados).

# %%
plt.hist(df_students['Grade'], edgecolor='k')
plt.xlabel('Grade')
plt.ylabel('Num. Students')

# %% [markdown]
# Observe como as notas concentram em 50. Às vezes é mais simples interpretar a função cumulativa dos dados.  Vamos fazer este gráfico de uma forma diferente da que vimos em sala de aula. Alterando um pouco a chamada `hist` podemos pegar a cumulativa.

# %%
plt.hist(df_students['Grade'], edgecolor='k', cumulative=True)
plt.xlabel('Grade - x')
plt.ylabel('Num. Students with Grade <= x')

# %% [markdown]
# Agora, `density=True` transforma este plot em uma função cumulativa de probabilidade.

# %%
plt.hist(df_students['Grade'], edgecolor='k', cumulative=True, density=True)
plt.xlabel('Grade - x')
plt.ylabel('Frac. Students with Grade <= x')

# %% [markdown]
# Observe que 50% dos alunos (0.5 no eixo-y) tem nota menor ou igual à mais ou menos 47~50 (eixo-x). Isto pode ser verificado com a chamada median abaixo. Outro exemplo, tente entender no gráfico, 20% dos alunos (eixo-y) tem nota menor ou igual à mais ou menos 30.

# %%
df_students['Grade'].median()

# %% [markdown]
# Até agora, você usou métodos do Matplotlib.pyplot para plotar gráficos. No entanto, muitos pacotes, incluindo Pandas, fornecem métodos que abstraem as funções Matplotlib simplificando sua vida. Por exemplo, o DataFrame fornece seus próprios métodos para plotar dados, conforme mostrado no exemplo a seguir para plotar um gráfico de barras de horas de estudo. 

# %%
df_students.plot.bar(x='Name', y='Grade', edgecolor='k')

# %% [markdown]
# Ou o mesmo histograma de antes.

# %%
df_students.plot.hist(y='Grade', edgecolor='k')
plt.xlabel('Grade - x')
plt.ylabel('Num. Students')

# %% [markdown]
# Como também uma versão contínua do histograma. Esta é chamada de Kernel Density Estimation (vimos rapidamente em sala de aula).

# %%
df_students.plot.kde(y='Grade')
plt.xlabel('Grade - x')
plt.ylabel('Density')

# %% [markdown]
# ### Estatísticas
# 
# #### Medidas de tendência central
# 
# Para entender melhor a distribuição, podemos examinar as chamadas medidas de tendência central; que é uma maneira sofisticada de descrever estatísticas que representam o "meio" dos dados. O objetivo disso é tentar encontrar um valor "típico". Maneiras comuns de definir o meio dos dados incluem:
#   * A média: uma média simples baseada na soma de todos os valores no conjunto de amostra e, em seguida, na divisão do total pelo número de amostras.
#   * A mediana: o valor no meio do intervalo de todos os valores de amostra.
#   * A moda: o valor de ocorrência mais comum no conjunto de amostra.
# 
# Vamos calcular esses valores, junto com os valores mínimo e máximo para comparação, e mostrá-los no histograma. Primeiramente, observe como podemos pegar tais valores direto do DataFrame.

# %%
df.mean()

# %%
df.median()

# %% [markdown]
# Ou, descrever o DataFrame como um todo. Aqui pegamos a média, mínimo, máximo e quartis (mais abaixo) dos dados.

# %%
df.describe()

# %% [markdown]
# Além disso, podemos focar em um vetor de dados específico.

# %%
data = df['Grade']


min_ = data.min()
max_ = data.max()
mean = data.mean()
median = data.median()
mode = data.mode()[0]

print(min_, max_, mean, median, mode, sep=', ')

# %% [markdown]
# Abaixo plotamos cada estatística em linhas verticais.

# %%
# Histograma
plt.hist(data, edgecolor='k')
plt.xlabel('Grade')
plt.ylabel('Num. Students')

# Linhas para cada estatística
plt.axvline(x=min_, color = 'gray', linestyle='dashed', linewidth = 2, label='min')
plt.axvline(x=mean, color = 'cyan', linestyle='dashed', linewidth = 2, label='mean')
plt.axvline(x=median, color = 'red', linestyle='dashed', linewidth = 2, label='median')
plt.axvline(x=mode, color = 'yellow', linestyle='dashed', linewidth = 2, label='mode')
plt.axvline(x=max_, color = 'gray', linestyle='dashed', linewidth = 2, label='max')

# Adiciona uma legenda
plt.legend()

# %% [markdown]
# ### Medidas de variância
# 
# Portanto, agora temos uma boa ideia de onde estão as estatísticas centrais dos dados. No entanto, há outro aspecto das distribuições que devemos examinar: quanta variabilidade existe nos dados?
# 
# As estatísticas típicas que medem a variabilidade nos dados incluem:
# 
# * Intervalo: a diferença entre o máximo e o mínimo. Não há função incorporada para isso, mas é fácil calcular usando as funções mín e máx.
# * Variância: a média da diferença quadrática da média. Você pode usar a função var integrada para encontrar isso.
# * Desvio padrão: a raiz quadrada da variância. Você pode usar a função std embutida para encontrar isso. 

# %%
for col_name in ['Grade', 'StudyHours']:
    col = df_students[col_name]
    rng = col.max() - col.min()
    var = col.var(ddof=1)
    std = col.std(ddof=1)
    print('\n{}:\n - Range: {:.2f}\n - Variance: {:.2f}\n - Std.Dev: {:.2f}'.format(col_name, rng, var, std))

# %% [markdown]
# #### Quartis
# 
# Na estatística descritiva, um quartil é qualquer um dos três valores que divide o conjunto ordenado de dados em quatro partes iguais, e assim cada parte representa 1/4 da amostra ou população.
# 
# Assim, no caso duma amostra ordenada,
#   * primeiro quartil (designado por Q1/4) = quartil inferior = é o valor aos 25% da amostra ordenada = 25º percentil
#   * segundo quartil (designado por Q2/4) = mediana = é o valor até ao qual se encontra 50% da amostra ordenada = 50º percentil, ou 5º decil.
#   * terceiro quartil (designado por Q3/4) = quartil superior = valor a partir do qual se encontram 25% dos valores mais elevados = valor aos 75% da amostra ordenada = 75º percentil
#   * à diferença entre os quartis superior e inferior chama-se amplitude inter-quartil.
#   
# Observe como os quartis estão presentes na sumarização dos dados. São as linhas 25%, 50% (mediana) e 75%.

# %%
df.describe()

# %% [markdown]
# #### Comparando Dados
# 
# Por fim, vamos comparar o tempo de estudo entre os alunos que passaram ou não. Para tal, vamos definir qualquer nota >= 60 como sendo uma aprovação. Depois disso, vamos alterar o DataFrame para conter tal informação.
# 
# Primeiro criando a série com tal informação.

# %%
passed = df['Grade'] >= 60
passed

# %% [markdown]
# Agora, alterando o DataFrame.

# %%
df['Passed'] = passed
df

# %% [markdown]
# Agora, vamos entender o tempo de dedicação dos alunos que passam e dos que não passam. Podemos fazer uso do Boxplot para tal comparativo. Na estatística descritiva, o boxplot é uma ferramenta gráfica para representar a variação de dados observados de uma variável numérica por meio de quartis.
# 
# A "caixa" mostra o primeiro e terceiro quartil. A linha no meio mostra o segundo, a mediana. Portanto, a caixa se estende dos valores dos quartil de Q1 a Q3 dos dados, com uma linha na mediana (Q2). Os bigodes se estendem das bordas da caixa para mostrar a extensão dos dados. Por padrão, eles estendem não mais do que 1,5 * IQR (IQR = Q3 - Q1) das bordas da caixa, terminando no ponto de dados mais distante dentro desse intervalo. Valores fora desta faix são plotados como pontos separados. 

# %%
df.boxplot(column='StudyHours', by='Passed', grid=False)

# %% [markdown]
# Observe que, como esperado, alunos que passam estudam mais. Os quartis, portanto a distribuição dos dados, são mais altos. Para observar os valores podemos fazer um groupby.
# 
# Abaixo eu agrupo os dados por passou ou não. Depois, pego as horas de estudo. Por fim, observo as estatíticas.

# %%
df.groupby('Passed')['StudyHours'].describe()

# %% [markdown]
# Observe como 25% (primeiro quartil) dos alunos que não passam, estudam menos do que 8,25 horas. Para os que passam, este valor é de 13,125. Agora pense no complemento dos 25%. 75% dos alunos que passam estudam pelo menos 13h! Isso é bem maior do que as 8h dos que não passam!

# %% [markdown]
# ### Correlacionando Dados
# 
# Por fim, podemos correlacional o tempo de estudo com a nota.

# %%
plt.scatter(df.StudyHours, df.Grade, edgecolor='k', alpha=0.75)
plt.xlabel('Hours')
plt.ylabel('Grade')

# %% [markdown]
# ## Exercícios (Flight Data)
# 
# Eu espero que o tutorial acima tenha sido uma boa revisão de análise exploratória de dados. Agora é com você! Nesta lista, você explorará um conjunto de dados do mundo real contendo dados de voos do Departamento de Transporte dos EUA.
# 
# Vamos começar carregando e visualizando os dados. 

# %%
df = pd.read_csv('https://raw.githubusercontent.com/icd-ufmg/icd-ufmg.github.io/master/listas/l3/flights.csv')

# %% [markdown]
# O conjunto de dados contém observações de voos domésticos dos EUA em 2013 e consiste nos seguintes campos:
# * Ano: o ano do voo (todos os registros são de 2013)
# * Mês: o mês do voo
# * Dia do mês: o dia do mês em que o voo partiu
# * DayOfWeek: o dia da semana em que o voo partiu - de 1 (segunda-feira) a 7 (domingo)
# * Transportadora: a abreviatura de duas letras da companhia aérea.
# * OriginAirportID: Um identificador numérico exclusivo para o aeroporto de partida
# * Nome do aeroporto de origem: o nome completo do aeroporto de partida
# * OriginCity: a cidade do aeroporto de partida
# * Estado de origem: o estado do aeroporto de partida
# * DestAirportID: Um identificador numérico único para o aeroporto de destino
# * DestAirportName: o nome completo do aeroporto de destino
# * DestCity: a cidade do aeroporto de destino
# * DestState: o estado do aeroporto de destino
# * CRSDepTime: a hora de partida programada
# * DepDelay: o número de minutos de atraso na partida (o voo que saiu antes do horário tem um valor negativo)
# * DelDelay15: Um indicador binário de que a partida foi atrasada por mais de 15 minutos (e, portanto, considerada "atrasada")
# * CRSArrTime: a hora de chegada programada
# * ArrDelay: o número de minutos de atraso na chegada (o voo que chegou antes do horário tem um valor negativo)
# * ArrDelay15: Um indicador binário de que a chegada foi atrasada em mais de 15 minutos (e, portanto, considerada "atrasada")
# * Cancelado: um indicador binário de que o voo foi cancelado 

# %% [markdown]
# ### Exercício 1
# 
# Conte a quantidade de dados faltantes na tabela. Isto é, em TODAS as células. O método retorna apenas um número.

# %%
def count_missing(df) -> int:
    res = df.isna().sum().sum()
    return res

# %%
assert_equal(2761, count_missing(df))

# %% [markdown]
# ### Exercício 2
# 
# Crie um novo DataFrame sem as linhas com dados faltantes

# %%
def drop_missing(df):
    res = df.dropna()
    return res

# %%
assert_equal(269179, drop_missing(df).shape[0])

# %% [markdown]
# ### Exercício 3
# 
# Retorne a mediana de TODAS as colunas numéricas do DataFrame

# %%
def all_median(df):
    res = df.median()
    return res

# %%
assert_equal(2013, all_median(df)['Year'])
assert_equal(7, all_median(df)['Month'])

# %% [markdown]
# ### Exercício 4
# 
# Quais são os atrasos médios (médios) de partida e chegada? Retorne uma tupla.

# %%
def delay(df) -> tuple:
    res = df.dropna()
    res = res[["DepDelay", "ArrDelay"]].mean()
    return res

# %%
assert_almost_equal(10.456614371849216, delay(df)[0])
assert_almost_equal(6.563286883449304, delay(df)[1])

# %% [markdown]
# ### Exercício 5
# 
# Indique qual rota tem o maior tempo de voo em MÉDIA. Use a coluna OriginAirportName e DestinationAirportName. Retorne uma tupla `(OriginAirportName, DestinationAirportName)`. Lembre-se de não considerar voos cancelados!

# %%
def high_delay(df):
    res = df.dropna().query('Cancelled == 0')
    res["TravelTime"] = (res["CRSArrTime"] + res["ArrDelay"]) - (res["CRSDepTime"] + res["DepDelay"])
    res = res.groupby(["OriginAirportName", "DestAirportName"], as_index=False).mean()[["OriginAirportName", "DestAirportName", "TravelTime"]]
    res = res.sort_values(by="TravelTime", ascending=False)
    res = res.loc[0, "OriginAirportName"], res.loc[0, "DestAirportName"]
    return res

# %% [markdown]
# ### Exercício 6
# 
# Faça um boxplot dos atrasos de saída por dia da semana!
# 
# 1. Dica, use `grid=False, showfliers=False` para o plot ficar mais limpo
# 
# *Saída esperada*
# 
# ![](https://raw.githubusercontent.com/icd-ufmg/icd-ufmg.github.io/master/listas/l3/plot1.png)

# %%
df[["DepDelay", "DayOfWeek"]].boxplot(column='DepDelay', by='DayOfWeek', grid=False, showfliers=False)

# %% [markdown]
# ### Exercício 7
# 
# Correlacione o atraso de saída com o atraso de chegada!
# 
# 1. Dica, remova os voos cancelados
# 
# *Saída esperada*
# 
# ![](https://raw.githubusercontent.com/icd-ufmg/icd-ufmg.github.io/master/listas/l3/plot2.png)

# %%
(df[["ArrDelay", "DepDelay", "Cancelled"]]
 .query('Cancelled == 0')
 .dropna()
 .drop("Cancelled", axis=1)
 .plot(kind="scatter", x="DepDelay", y="ArrDelay", edgecolor='k', alpha=0.75))

# %%



