#### Notes Bar Chart ####
# from matplotlib import pyplot as plt
# plt.style.use("seaborn")
# x=[1,2,3,4,5,6,7,8,9,10]
# y=[20,34,56,21,3,4,7,9,77,99]
# plt.bar(x,y,label="Random graph")
# plt.legend()
# plt.title("Some graph")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.grid(True)
# # plt.tight_layout()
# plt.show()


# import numpy as np
# from matplotlib import pyplot as plt
# plt.style.use("seaborn")
# width = 0.25
# # plt.xkcd()
# dev_age = [25,26,27,28,29,30,31,32,33,34,35]
# x_index = np.arange(len(dev_age))
# dev_y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
# pydev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
# jsdev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
# plt.bar(x_index-width, dev_y, width=width, label="AllDev")
# plt.bar(x_index, pydev_y, width=width, label="PyDev")
# plt.bar(x_index+width, jsdev_y, width=width, label="JsDev")
# plt.grid(True)
# plt.legend()
# plt.xticks(ticks=x_index, labels=dev_age)
# plt.xlabel("AGE")
# plt.ylabel("Salary of Dev")
# plt.title("Median salary by age (INR)")
# plt.show()


import csv
from collections import Counter
# import numpy as np
from matplotlib import pyplot as plt
plt.style.use("seaborn")
with open("data.csv") as csv_file:
    csv_reader=csv.DictReader(csv_file)
    language_counter=Counter()
    for row in csv_reader:
        language_counter.update(row["LanguagesWorkedWith"].split(";"))
languages=[]
popularity=[]

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
languages.reverse()
popularity.reverse()
plt.barh(languages,popularity)
plt.grid(True)
plt.xlabel("Number of People Who Use")
plt.title("Most popular languages")
plt.show()