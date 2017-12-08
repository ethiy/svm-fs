
import matplotlib.pyplot as plt
from csv import reader


with open('sample.csv', 'r') as f:
    data = list(reader(f))

with open('bandes.csv', 'r') as f:
    bandes = list(reader(f))

obs = [i[4:14] for i in data[1::]]
legend = [i[3] for i in data[1::]]


for i in range(len(obs)):
	#plt.plot(bandes, obs[i], label=str(legend[i]))
	plt.plot(bandes, obs[i], label=str(i))
plt.legend()

plt.xlabel('? ()')
plt.ylabel('? ()')

#plt.show()
plt.savefig('plot.png')
