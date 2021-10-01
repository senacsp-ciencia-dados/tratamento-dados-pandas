import pandas as pd

dados = {
  "nome": ["Argentina", "Brasil", "França", "Australia"],
  "continente": ["América", "América", "Europa", "Oceania"]
}
siglas = ["ARG", "BRA", "FRA", "AUS"]
paises = pd.DataFrame(dados,index=siglas)
#print(paises)
print(paises.iloc[2])
print(paises.loc["BRA"])