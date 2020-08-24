import csv
import matplotlib.pyplot as plt

listsrv = []
temp = []
ans = []
d = []

r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0

with open('../Week1/listserv.csv', newline='') as file:
    data = csv.reader(file)
    for r in data:
        temp = [r[0], int(r[1])]
        listsrv.append(temp)

count = 0
with open('../Week1/qns1.csv', newline='') as file:
    data = csv.reader(file)
    for row in data:
        d.append(row[0])
        for entry in listsrv:
            if (row[0] == entry[0]):
                ans.append(row[0])
                if (1 == entry[1]):
                    r1 = r1 + 1
                elif (2 == entry[1]):
                    r2 = r2 + 1
                elif (3 == entry[1]):
                    r3 = r3 + 1
                elif (4 == entry[1]):
                    r4 = r4 + 1
                elif (5 == entry[1]):
                    r5 = r5 + 1
        

print(r5, r4, r3)
print(len(ans))

labels = 'Subscribed to the Email List','Not Subscribed to the Email List'
sizes = [len(ans), len(d)]

labels2 = 'Rating 1','Rating 2','Rating 3','Rating 4','Rating 5'
sizes2 = [r1, r2, r3, r4, r5]

plt.pie(sizes2, labels=labels2, startangle=90, autopct='%.0f%%')
plt.axis('equal')
plt.show()