#Notei que não havia feito nada sobre a biblioteca Matplotlib, então decidi colocar aqui mesmo.
import matplotlib.pyplot as plt

dias = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
meta = [800,800,800,800,800,800,800,800,800,800,800,800,800,800,800]
producao = [1000,1000,1100,800,820,700,1000,900,700,939,1000,800,820,800,1000]

plt.plot(dias,producao, label="Produção", marker='o')
plt.plot(dias,meta, label="Meta", linestyle='--')

plt.title("Produção x Meta por Dia")
plt.xlabel("Dias da Semana")
plt.ylabel("Quantidade Produzida")
plt.legend()

plt.title('Meu gráfico')

plt.show()