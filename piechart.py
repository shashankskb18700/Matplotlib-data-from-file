import matplotlib.pyplot as plt
slices=[7,2,13,4]
activities=['sleeping','eating','working','playing']
cols=['c','m','red','k']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0.1,0.1,0))

        
plt.title('pie chart')
