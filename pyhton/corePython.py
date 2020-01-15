import os
import googlemaps
import sys
from itertools import combinations


# ////////////////////////////////////////////////////////
# kruskal fun
# main class initialize edges and graph///////////////////////////////////

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return (i)
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # main call///////////////////////////////////////////////////
    def KruskalMST(self):

        result = []

        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:

            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        final = []
        count2 = 0
        sumDis = 0
        for u, v, weight in result:
            count2 = count2+1
            sumDis = sumDis + weight
            # print tree////////////////////////////////////////////////////////////
            c1 = mapIdtoKey.get(u)
            c2 = mapIdtoKey.get(v)
            wrt = c1 + ' ' + c2 + ' ' + str(weight/1000)

            final.append(wrt)

        final.append(str(sumDis/1000))
        final.insert(0, count2)
        print(final)
   
        # ///////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////--------------2nd step------------------////////////////////////////////////


def kruskalDriver(edgeInfo, cityIndex):
    # take edges list
    edges = 0
    # edgeInfo = ['mumbai nagpur 841443', 'mumbai delhi 1427123', 'mumbai hyderabad 709138', 'mumbai kanpur 1289029', 'mumbai bangalore 983805', 'mumbai ahmedabad 531273', 'mumbai kolkata 2215939', 'mumbai surat 289691', 'mumbai pune 147778', 'nagpur delhi 1078761', 'nagpur hyderabad 500786', 'nagpur kanpur 736663', 'nagpur bangalore 1092331', 'nagpur ahmedabad 860775', 'nagpur kolkata 1237648', 'nagpur surat 809619', 'nagpur pune 711265', 'delhi hyderabad 1585593', 'delhi kanpur 495521', 'delhi bangalore 2177139', 'delhi ahmedabad 947992', 'delhi kolkata 1491011', 'delhi surat 1154744', 'delhi pune 1426950', 'hyderabad kanpur 1235970', 'hyderabad bangalore 575513', 'hyderabad ahmedabad 1220012', 'hyderabad kolkata 1496488', 'hyderabad surat 978430', 'hyderabad pune 561685', 'kanpur bangalore 1834208', 'kanpur ahmedabad 1066389', 'kanpur kolkata 1002334', 'kanpur surat 1164073', 'kanpur pune 1297798', 'bangalore ahmedabad 1493792', 'bangalore kolkata 1889116', 'bangalore surat 1252210', 'bangalore pune 840560', 'ahmedabad kolkata 2066804', 'ahmedabad surat 262847', 'ahmedabad pune 657145', 'kolkata surat 2043124', 'kolkata pune 2070852', 'surat pune 414093']
    edgeli = []

    for i in edgeInfo:
        edges = edges + 1
        edgeli.append(i.split())

    # dictionary to map city to id///////////////////////////////

    mapIdDict = {}
    noCity = 0
    line = []

    for s in cityIndex:
        noCity = noCity + 1
        line = s.split()
        mapIdtoKey[int(line[0])] = line[1]
        mapIdDict[line[1]] = int(line[0])

    # end dict maping////////////////////////////////////////////////////////

    g = Graph(noCity)
    cnt1 = 0
    while(cnt1 < edges):
    
        c1 = mapIdDict.get(edgeli[cnt1][0])
        c2 = mapIdDict.get(edgeli[cnt1][1])
        weight1 = edgeli[cnt1][2]

        cnt1 = cnt1 + 1
      
        g.addEdge(c1, c2, int(weight1))

    g.KruskalMST()

# ///////////////////////////////////////////////////////-------start here-------////////////////////////////////////////////////////////////
mapIdtoKey = {}

cityList = sys.argv[1].split(',')
edgeList = sys.argv[2].split(',')
# print("aaaaaaaaaaa")
# print(cityList)
# print("aaaaaaaaaaa")
# print(edgeList)

# cityList = ['mumbai', 'nagpur', 'pune']

# /////create city list with index no///
cityIndex = []
for i in range(len(cityList)):
    cityIndex.append(str(i) + " " + cityList[i])

# /////////////////////////////////////////////////////////
# edgeList = list(['pune-mumbai'])


ne = []
rem = []
rem1 = []

for i in edgeList:
    ne = i.split('-')

    rem.append([ne[0], ne[1]])
    rem1.append([ne[1], ne[0]])

# print(rem)
# print(rem1)    

# rem = [['pune', 'hyderabad'], ['pune', 'mumbai']]
# rem1 = [['hyderabad', 'pune'], ['mumbai', 'pune']]

# ///////////////////////////////////////////////////////

cityWeight = []

comb = combinations(cityList, 2)

for i in list(comb):
    i = list(i)
    f = 0
    j = 0
    k = 0
    for j in rem:
        
        if(i == j):
            # print(j)
            rem.remove(i)
            f = 1

    if(f == 0):
        for k in rem1:
            
            if(i == k):
                # print(k)
                rem1.remove(k)
                f = 1
                break

        if(f == 0):
            try:
                gmaps = googlemaps.Client(
                    key='AIzaSyBskGjP5ke_pNJedhqZFTdyqcDIyEsWVlQ')
                my_dist = gmaps.distance_matrix(i[0], i[1])[
                    'rows'][0]['elements'][0]['distance']['value']

                wrt = str(i[0]) + ' ' + str(i[1]) + ' ' + str(my_dist)
                cityWeight.append(wrt)

            except(Exception):
                exception = true

            # print(wrt)        


kruskalDriver(cityWeight, cityIndex)
