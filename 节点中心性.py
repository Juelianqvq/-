# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import networkx as nx
import matplotlib.pyplot as plt
import os


filename = "facebook_combined.txt"
G = nx.Graph()  # 建立一个空的无向图G
with open(filename) as file:
    for line in file:
        head, tail = [int(x) for x in line.split()]
        G.add_edge(head,tail)

deg=G.degree()
#度中心性

max_num = deg[0]
max_index = 0
for i in range(len(deg)):
    if deg[i]>max_num:
        max_num = deg[i]
        max_index = i


print("Max degree:", max_num, "Max index:", max_index)
#特征向量中心性
ec = nx.eigenvector_centrality(G)
rank=[]
for node, value in ec.items():
    rank.append(value)
max_num = rank[0]
max_index = 0
for i in range(len(rank)):
    if rank[i]>max_num:
        max_num = rank[i]
        max_index = i



print("Max eigenvector centrality:", max_num, "Max index:", max_index)
#pagerank中心性
pr=nx.pagerank(G,alpha=0.85)
rank=[]
for node, value in pr.items():
    rank.append(value)

max_num = rank[0]

max_index = 0

for i in range(len(rank)):
    if rank[i]>max_num:
        max_num = rank[i]
        max_index = i

print("Max pagerank centrality:", max_num, "Max index:", max_index)
#中介中心性 betweenness centrality
bc = nx.betweenness_centrality(G)
rank=[]
for node, value in bc.items():
    rank.append(value)

max_num = rank[0]

max_index = 0

for i in range(len(rank)):
    if rank[i]>max_num:
        max_num = rank[i]
        max_index = i
print("Max betweenness centrality:", max_num, "Max index:", max_index)



#接近中心性 closeness centrality
cc=nx.closeness_centrality(G)
rank=[]
for node, value in cc.items():
    rank.append(value)

max_num = rank[0]

max_index = 0

for i in range(len(rank)):
    if rank[i]>max_num:
        max_num = rank[i]
        max_index = i
print("Max closeness centrality:", max_num, "Max index:", max_index)
















# See PyCharm help at https://www.jetbrains.com/help/pycharm/
