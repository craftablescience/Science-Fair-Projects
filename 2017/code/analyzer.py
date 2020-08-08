# made by me to help analyze data

import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in("pythonprogrammr2", "0kb4o15kqy")

folder = str(raw_input("What folder? [/data/] "))
if folder == "":
    folder = "/data/"
days = int(input("How many days? "))
files_n = []
files_y = []
data_n = []
data_y = []

try:
    for i in range(1,days+1):
        files_n.append(open("..%s%i_n.txt"%(folder,i)))
        files_y.append(open("..%s%i_y.txt"%(folder,i)))
    for file_n in files_n:
        data_n.append(file_n.readlines())
    for file_y in files_y:
        data_y.append(file_y.readlines())
finally:
    for files in files_n:
        files.close()
    for files in files_y:
        files.close()

data_n = [data.replace("\n", "").split('|') for i in range(len(data_n)) for data in data_n[i]]
data_y = [data.replace("\n", "").split('|') for i in range(len(data_y)) for data in data_y[i]]

times_n = {}
times_y = {}

meters_n = {}
meters_y = {}

for i in data_n:
    if i[2] not in times_n.iterkeys():
        times_n[i[2]] = [i[3]]
    else:
        times_n[i[2]].append(i[3])

for i in data_y:
    if i[2] not in times_y.iterkeys():
        times_y[i[2]] = [i[3]]
    else:
        times_y[i[2]].append(i[3])

for i in data_n:
    if i[2] not in meters_n.iterkeys():
        meters_n[i[2]] = [i[4]]
    else:
        meters_n[i[2]].append(i[4])

for i in data_y:
    if i[2] not in meters_y.iterkeys():
        meters_y[i[2]] = [i[4]]
    else:
        meters_y[i[2]].append(i[4])

averages_n = {}
averages_y = {}
average = 0
count = 0

mavg_n = {}
mavg_y = {}

for i in times_n.iterkeys():
    for j in times_n[i]:
        average += float(j)
        count += 1
    averages_n[i] = average / count;

average = 0
count = 0

for i in times_y.iterkeys():
    for j in times_y[i]:
        average += float(j)
        count += 1
    averages_y[i] = average / count;

average = 0
count = 0

for i in meters_n.iterkeys():
    for j in meters_n[i]:
        average += float(j)
        count += 1
    mavg_n[i] = average / count;

average = 0
count = 0

for i in meters_y.iterkeys():
    for j in meters_y[i]:
        average += float(j)
        count += 1
    mavg_y[i] = average / count;

choice = str(raw_input("Calculate time or meters? ([t]/m) "))

if choice == "t" or choice == "T" or choice == "":
    bars1 = go.Bar(
                   x = [_ for _ in averages_n],
                   y = [averages_n[_] for _ in averages_n],
                   name = "No texting"
    )

    bars2 = go.Bar(
                   x = [_ for _ in averages_y],
                   y = [averages_y[_] for _ in averages_y],
                   name = "Texting"
    )

    data = [bars1, bars2]
    layout = go.Layout(barmode = "group")
    fig = go.Figure(data = data, layout = layout)
elif choice == "m" or choice == "M":
    bars1 = go.Bar(
                   x = [_ for _ in mavg_n],
                   y = [mavg_n[_] for _ in mavg_n],
                   name = "No texting"
    )

    bars2 = go.Bar(
                   x = [_ for _ in mavg_y],
                   y = [mavg_y[_] for _ in mavg_y],
                   name = "Texting"
    )

    data = [bars1, bars2]
    layout = go.Layout(barmode = "group")
    fig = go.Figure(data = data, layout = layout)    

inp = str(raw_input("Do you want to upload to plot.ly? ([y]/n) "))
if inp == "" or inp == "y" or inp == "Y":
    print "Saving to plot.ly ..."
    py.plot(fig, filename = "Science Fair 2016: Times")
else:
    print "Not saving to plot.ly"

inp = str(raw_input("Do you want to save to data folder as data.png? ([y]/n) "))
if inp == "" or inp == "y" or inp == "Y":
    print "Saving as data.png ..."
    py.image.save_as(fig, filename = "../data/data.png")
else:
    print "Not saving as data.png"
