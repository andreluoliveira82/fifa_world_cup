import pandas as pd

# carregar os dados do csv para um dataframe
df = pd.read_csv('fifa_world_cup_matches.csv')

print(df.head())

print(df.columns)

# Limpeza e Preparação dos Dados
# Primeiro, precisamos dividir a coluna score em duas colunas separadas para os gols dos times da casa e visitantes.

# Dividir a coluna 'score' em 'home_goals' e 'away_goals'
df[["home_goals", "away_goals"]] = df["score"].str.split("–", expand=True).reset_index()
df["home_goals"] = df["home_goals"].str.extract("(\\d+)")
df["away_goals"] = df["away_goals"].str.extract("(\\d+)")

# ajustar os tipos de dados das colunas:
df["home_goals"] = df["home_goals"].astype(int)
df["away_goals"] = df["away_goals"].astype(int)

df.info()

df["home_goals"].describe()
df["away_goals"].describe()

df["away_goals"].head()
df["away_goals"].tail()

df["home_goals"].head()
df["home_goals"].tail()

df.tail()
df.head()