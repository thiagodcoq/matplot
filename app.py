import matplotlib.pyplot as plt

views = [534,689,258,401,724,689,350]
days = range(1,8)

#plt.plot(x,y)
#plt.plot(days,views,label = 'Youtube Views')
#plt.xlabel('Day No.')
#plt.ylabel('Views')
#plt.legend()
#plt.title('Teste')

plt.hist(views,density=True,bins=30)
plt.ylabel('Probability')
plt.xlabel('Data')
plt.title('Histogram')
plt.legend('Teste')
plt.show()
