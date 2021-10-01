import pandas as pd

paises = pd.read_csv("03-paises.csv",index_col="sigla")
print(paises)
paises.to_csv("03-paises-exportacao.csv", sep="\t")