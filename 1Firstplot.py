#### Notes X-Y plot ####
# from matplotlib import pyplot as plt
# # plt.xkcd()
# x=[1,2,3,4,5,6,7,8,9,10]
# y=[20,34,56,21,3,4,7,9,77,99]
# plt.plot(x,y,"r",label="Random graph")
# plt.legend()
# plt.title("Some graph")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.grid(True)
# # plt.tight_layout()
# plt.show()

from matplotlib import pyplot as plt
# print(plt.style.available)
# plt.style.use("fivethirtyeight")
# plt.xkcd()
dev_age=[25,26,27,28,29,30,31,32,33,34,35]
dev_y=[38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
pydev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
jsdev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(dev_age,dev_y, "k--",label="AllDev")
plt.plot(dev_age,pydev_y,"b",label="PyDev")
plt.plot(dev_age,jsdev_y,"r",label="JsDev")
plt.grid(True)
plt.legend()
plt.xlabel("AGE")
plt.ylabel("Salary of Dev")
plt.title("Median salary by age (INR)")
plt.show()
