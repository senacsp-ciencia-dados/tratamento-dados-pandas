import pandas as pd
import numpy as np

# alunos = ["Caio", "Maria", "José"]
# id_alunos = ["10", "21", "35"]
# notas = pd.Series([8, 9, 4])

# # # Series - Vetor
# alunos = pd.Series(alunos, index=id_alunos)
# # # indices de aprovados
# ids_aprovados = notas[notas >= 6].index
# print(alunos[ids_aprovados])

# s1 = pd.Series([1, 2, 3])
# s2 = pd.Series([7, 8, 9])
# print(s1 + s2)
# print(s1 * s2)
# print(s1 * 5)
# print(np.sqrt(s1))

dias = ["10/01/2021", "11/01/2021", "12/01/2021"]
temp = [31, 32, 34]
serie = pd.Series(temp, index=dias)

serie.index = pd.to_datetime(serie.index, format="%d/%m/%Y")
print(serie)