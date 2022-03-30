import json
import math


def checkCollision(a, b, c, x, y, radius, entr1, entr2):

    dist = (abs(a * x + b * y + c)) / math.sqrt(a * a + b * b)

    if radius == dist:
        touch.append(1)
        entrylst.append([entr1[0], entr2[0]])
    elif radius > dist:
        inter.append(1)
        entrylst.append([entr1, entr2])
    else:
        outside.append(1)


with open("headings.json", "r") as h:
    headdict = json.load(h)

inter = []
touch = []
outside = []
entrylst = []


# subdict = headdict["1"][:]
# print(len(subdict))
RADIUS = 0.001


for heading in range(1, len(headdict) + 1):

    for i in range(0, len(headdict[str(heading)])):
        x = headdict[str(heading)][i][4]
        y = headdict[str(heading)][i][3]
        entr1 = headdict[str(heading)][i]

        for k in range(0, len(headdict[str(heading)])):
            a = headdict[str(heading)][k][1]
            b = -1
            c = headdict[str(heading)][k][2]
            entr2 = headdict[str(heading)][k]

            checkCollision(a, b, c, x, y, RADIUS, entr1, entr2)


print(f"touch:{len(touch)}\ninter:{len(inter)}\noutside:{len(outside)}")

endlist = []
enddict = {}


for i in entrylst:
    if i[0] != i[1]:
        endlist.append(i)

for i in endlist:
    enddict[i[0][5]] = []

for i in endlist:
    enddict[i[0][5]].append(i)

print(enddict)

with open("intersecting.json", "w") as l:
    json.dump(enddict, l)
