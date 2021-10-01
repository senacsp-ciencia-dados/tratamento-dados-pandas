import pandas as pd

# r = pd.DataFrame({
#   "a": [1, 2],
#   "b": [6, 7]
# })
# s = pd.DataFrame({
#   "a": [4, 5],
#   "c": [8, 6]
# })
# juncao = pd.merge(r,s)
# print(juncao)

r = pd.DataFrame({
  "id": ["13", "15", "18"],
  "nome": ["Celso", "Ana", "Otavio"]
})
s = pd.DataFrame({
  "idfunc": ["13", "18"],
  "departamento": ["TI", "Marketing"]
})
juncao = pd.merge(r,s, left_on="id", right_on="idfunc")
print(juncao)