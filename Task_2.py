# Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

from matplotlib import pyplot as plt  
import random

housesArea = [random.randint(100, 301) for i in range(0,15)]
housesPrise = [random.randint(3000000, 20000000) for i in range(0,15)]
x = []
oneMetrPrise = []
lowPrise = []
sortedHouses = []

for i in range(0,15):
    x.append(i+1)

for i in range(len(housesArea)):
    oneMetrPrise.append(round(housesPrise[i]/housesArea[i]))


print(housesArea)
print(oneMetrPrise)


for i in range(len(oneMetrPrise)):
    if oneMetrPrise[i] < 50000:
        lowPrise.append(oneMetrPrise[i])
        sortedHouses.append(housesArea[i])

for i in range(len(sortedHouses)-1):
    for j in range(len(sortedHouses)-i-1):
        if sortedHouses[j] > sortedHouses[j+1]:
            lowPrise[j], lowPrise[j+1] = lowPrise[j+1], lowPrise[j]
            sortedHouses[j], sortedHouses[j+1] = sortedHouses[j+1], sortedHouses[j]


print('\nДома, у которых стоимость квадратного метра < 50000 рублей:')
for i in range(len(lowPrise)):
    print(f'Площадь дома - {sortedHouses[i]}, стоимость 1м2 - {lowPrise[i]}')


plt.title('Свод')
plt.xlabel('N дома')    
plt.ylabel('Стоимость 1м2')  
plt.grid(which='major')


plot2 = list(50000 for a in range(1, 16))
plt.plot(x, plot2)
plt.plot(x, oneMetrPrise, 'go')
plt.show()