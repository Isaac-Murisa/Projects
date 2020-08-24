import csv
import datetime
import matplotlib.pyplot as plt

projectList = []
wslist = []
countWorkshopFirst = 0
totalfound = 0

with open('../Week6/allWS.csv', newline='') as file:
    data = csv.reader(file)
    for row in data:
        year = int(row[4][0:4])
        month = int(row[4][5:7])
        day = int(row[4][8:10])
        d = datetime.date(year, month, day)
        temp = [ row[0], row[1], row[2], int(row[3]), d ]
        wslist.append(temp)

with open('../Week6/projectdates.csv', newline='') as file:
    data2 = csv.reader(file)
    for row2 in data2:
        year = int(row2[4][0:4])
        month = int(row2[4][5:7])
        day = int(row2[4][8:10])
        d = datetime.date(year, month, day)
        temp2 = [ row2[0], row2[1], row2[2], int(row2[3]), d ]
        projectList.append(temp2)


def checkName(i):
    global countWorkshopFirst
    tempProject = projectList[i]
    found = False
    for e in wslist:
        if (e[0].lower() == tempProject[0].lower() and e[1].lower() == tempProject[1].lower()):
            if (tempProject[4] > e[4]):
                countWorkshopFirst = countWorkshopFirst + 1
            found = True
    return found

def checkNumber(i):
    global countWorkshopFirst
    tempProject = projectList[i]
    found = False
    for e in wslist:
        if (e[3] == tempProject[3]):
            if (tempProject[4] > e[4]):
                countWorkshopFirst = countWorkshopFirst + 1
            found = True
    return found

def checkEmail(i):
    global countWorkshopFirst
    tempProject = projectList[i]
    found = False
    for e in wslist:
        if (e[2] == tempProject[2]):
            if (tempProject[4] > e[4]):
                countWorkshopFirst = countWorkshopFirst + 1
            found = True
    return found


for index in range(len(projectList)):

    if (checkNumber(index)):
        totalfound = totalfound + 1
        print("found a person with student number")
    elif (checkEmail(index)):
        totalfound = totalfound + 1
        print("found a person with email")
    elif (checkName(index)):
        totalfound = totalfound + 1
        print("found a peron with name")

print("Number of people who booked a meeting after attending a workshop: ", countWorkshopFirst)
print("number of people who attended a workshop after booking a meeting: ", totalfound-countWorkshopFirst)
print("Number of people who booked a meeting and never attended a workshop: ")


labels = 'Attended a WS before booking a meeting','Booked a meeting and then attended a WS','Booked a meeting but never attended a WS'
sizes = [countWorkshopFirst, (totalfound-countWorkshopFirst), len(projectList)-totalfound]

plt.pie(sizes, labels=labels, startangle=90, autopct='%.0f%%')
plt.axis('equal')
plt.show()
