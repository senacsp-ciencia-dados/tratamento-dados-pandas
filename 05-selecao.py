import pandas as pd

def funcao(valor):
  return valor + "lala"

flags = pd.read_csv("flag.data", header=None)
#print(paises)
oceania = ((flags[1] == 6) & (flags[11] == 1)) # Series de índices
flags_oceania = flags[oceania] # filtragem
flags_oceania[24] = flags_oceania[24].replace([0,1],["presente","ausente"])
flags_oceania[0] = flags_oceania[0].apply(funcao)
print(flags_oceania[[0, 24]])