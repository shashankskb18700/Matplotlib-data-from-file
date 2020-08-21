import csv


'''first.txt=
0,1
1,2
2,3
3,4
4,5'''



x=[]
y=[] 
with open('first.txt','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
plt.plot(x,y,label='loaded from file',color='orange')
plt.xlabel('x')
plt.ylabel('y')
plt.title('intresting graph')
plt.legend()
