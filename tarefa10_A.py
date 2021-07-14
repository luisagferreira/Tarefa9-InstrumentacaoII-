# Luísa Gonçalves Ferreira
import numpy as np
import matplotlib.pyplot as plt

n=np.arange(51)
# Criação do sinal
y=np.cos(0.05*np.pi*n)
array1=np.array(y)
print(array1)
print("     ")
print("PARÂMENTROS PARA O ARRAY:")
parametros=np.array([("Soma:", np.sum(array1)),("Valor máximo: ",np.max(array1)),
                     ("Valor mínimo: ",np.min(array1)),("Média: ",np.mean(array1)),
                     ("Mediana: ",np.median(array1)),("Desvio padrão: ",np.std(array1))])
print(parametros)
plt.plot(y)
plt.show()