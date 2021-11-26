# -*- coding = utf-8 -*-
# @Time : 2020/12/4 17:04
# @Author : K先生
# @File : begin.py
# @Software : PyCharm
import networkx as nx
import matplotlib.pyplot as plt
import community


G=nx.read_edgelist("facebook_combined.txt",create_using=nx.Graph(),nodetype=int)
# plt.savefig("cora.png")
# nx.write_gexf(G,"cora.gexf")
partition = community.best_partition(G)
pos = nx.spring_layout(G)
values = [partition.get(node) for node in G.nodes()]
nx.draw_networkx(G, pos, cmap=plt.get_cmap('magma'), node_color=values, node_size=50, with_labels=False)
plt.show()
print(nx.info(G))