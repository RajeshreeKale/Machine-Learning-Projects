import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('output.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.bar(x,y, label='Progress Graph')
plt.xlabel('Levels')
plt.ylabel('Number of Points Earned')
plt.title('Prince of Persia')
plt.legend()
plt.show()