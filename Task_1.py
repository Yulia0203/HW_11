# Задача 1. Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

from matplotlib import pyplot as plt   
from matplotlib import style

style.use('ggplot')
   
x = []
y = []
for i in range(-30,30):
    x.append(i)

for i in range(len(x)):
    y.append(5 * x[i] * x[i] + 10 * x[i] - 30)
   
plt.plot(x,y)   
   
plt.title('Epic Info') 
# fig = plt.figure()
plt.ylabel('Y axis')    
plt.xlabel('X axis')    
plt.show()   

print('При следующих значениях х функция отрицательная: 1, 0, -1, -2, -3')