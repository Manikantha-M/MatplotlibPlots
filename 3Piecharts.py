# from matplotlib import pyplot as plt
# plt.style.use("seaborn")
# slices=[60,15,10,5]
# labels=["sixty","fifteen","ten","five"]
# plt.pie(slices,labels=labels,wedgeprops={"edgecolor":"black"})
# plt.title("Pychart")
# plt.show()


from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode=[0,0,0,0.1,0]

plt.pie(slices,labels=labels,explode=explode,shadow=True,startangle=90,autopct="%1.1f%%",
        wedgeprops={"edgecolor":"black"})
plt.title("Pychart")
plt.show()