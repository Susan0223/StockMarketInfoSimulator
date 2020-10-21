import matplotlib.pyplot as plt
import csv

f = open('AAPL.csv')

csv_f = csv.reader(f)

x_points = []
y = []
i = 0

for row in reversed(list(csv_f)):
    x_points.append(row[0])
    y.append(float(row[4]))
    i += 1
    if(i >= 13):
        break

x = x_points[::-1]
y = y[::-1]


for i in range(len(x)):
    x[i] = x[i].replace("-","")
    print(x[i])

# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('AAPL') 
  
# function to show the plot 
plt.show() 
