# Luísa Gonçalves Ferreira
import numpy as np
import matplotlib.pyplot as plt

n=np.arange(51)
# Criação do sinal
y=np.cos(0.05*np.pi*n)
array1=np.array(y)
print(array1)
print("PARÂMENTROS PARA O ARRAY:")
print("Soma:", np.sum(array1))
print("Valor máximo: ",np.max(array1))
print("Valor mínimo: ",np.min(array1))
print("Média: ",np.mean(array1))
print("Mediana: ",np.median(array1))
print("Tamanho: ",len(array1))
plt.plot(y)
plt.show()