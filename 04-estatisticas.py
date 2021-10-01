import pandas as pd
dados = { 
  "nomes": ["Caio", "Maria", "José"],
  "notas": [8, 9, 4]  }
id_alunos = ["10", "21", "35"]

alunos = pd.DataFrame(dados,index=id_alunos)

print("----Estatística----")
print("média: ", alunos["notas"].mean())
print("desvio: ", alunos["notas"].std())
print("mediana: ", alunos["notas"].median())
print("max - min", alunos["notas"].max(), " - ", alunos["notas"].min())
print("----Ordernação----")
ordem_alunos = alunos.sort_values(by="notas", ascending=False)
print(ordem_alunos)