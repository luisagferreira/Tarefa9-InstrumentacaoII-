# Luísa Gonçalves Ferreira
import numpy as np
import matplotlib.pyplot as plt

n=np.arange(51)
y=np.cos(0.05*np.pi*n)
array1=np.array(y)
noise = np.random.normal(np.mean(array1),np.std(array1),51)
ruido=array1+noise
plt.figure(figsize=(10, 6), dpi=80)
plt.title("Sinal com e sem ruído")
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.plot(array1,label="Sinal Original")
plt.plot(ruido,label="Sinal com ruído")
plt.legend(loc=3)
plt.show()

