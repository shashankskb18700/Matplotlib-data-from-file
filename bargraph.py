x=[1,2,3,4,5,6]
y=[3,4,7,6,5,4]
x2=[4,3,2,5,6,1]
y2=[5,3,6,8,7,9]
#x3=[4,3,6,4,2,7]
#y3=[7,8,9,4,1,3]
plt.bar(x,y,label='first line',color='r')#,marker='*',markersize='20')

plt.bar(x2,y2,label='second line',color='c')#,marker='.',markersize='20')
#plt.bar(x3,y3,label='third line',color='gold',marker='+',markersize='20',markerfacecolor='g')
plt.title('intresting graph')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
