import networkx as nx
import matplotlib.pyplot as plt
import matplotlib #用于显示中文字符
import pandas as pd

filename = "facebook_combined.txt"
G = nx.Graph()  # 一个空的无向图G
with open(filename) as file:
    for line in file:
        head, tail = [int(x) for x in line.split()]
        G.add_edge(head, tail)
#描述图的属性(节点数、边数、直径、平均最短路径、度分布、聚类系数)
#print("所有节点的度:",nx.degree(G))#返回所有节点的度
#print("所有节点的度分布序列:",nx.degree_histogram(G))#返回图中所有节点的度分布序列（从1至最大度的出现频次）
degree = nx.degree_histogram(G)#返回图中所有节点的度分布序列
#度分布p(d)定义为度数为d的节点数目除以节点总数
#print(sum(degree)) #总的度数
plt.style.use('classic')
plt.rcParams['legend.framealpha'] = 0  # 图例框完全透明
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
config1 = {
    "font.family": 'sans-serif',
    "font.size": 16,
}
plt.rcParams.update(config1)
x = range(len(degree))#生成X轴序列，从1到最大度
y = [z/sum(degree) for z in degree]#将度频数转化为频率
#print(y) #查看频率值，与上面度频数对应
#图表内设置中文字符格式
matplotlib.rcParams['font.family'] = 'SimHei' #中文黑体
matplotlib.rcParams['font.size'] = 16         #字号
matplotlib.rcParams['font.style'] = 'italic'  #斜体
p0=plt.figure()
p1=plt.subplot(121)
p1.scatter(x, y, color="blue", marker="x", s=28, linewidth=0.5)#绘制度分布散点图，s是点的大小
plt.xlabel("各节点度数x")
plt.ylabel("节点的度数对应频率y")
plt.title("度分布散点图")
p2=plt.subplot(122)
p2.loglog(x, y, color="blue", marker="x", markersize=5, linewidth=0.5)
plt.ylim([1e-3, 0.035]) #设置双对数图y轴范围让数据分布更直观
plt.xlabel("log(x)")
plt.ylabel("log(y)")
plt.title("双对数——度分布图")
plt.tight_layout()
average_length = nx.average_shortest_path_length(G)#平均最短路径
print('平均路径', average_length)
diameter = nx.diameter(G)#直径
#print(nx.diameter(G))
Nodes = nx.number_of_nodes(G)#图的节点总数
#print(Nodes)
Edges = nx.number_of_edges(G)#图的总边数
#print(Edges)
subplot_Number = nx.number_connected_components(G)#连通子图数
#print(subplot_Number)
#clustering=nx.clustering(G)#局部聚类系数
average_clustering = nx.average_clustering(G)#平均聚类系数
'''max_clustering=max(clustering.values())#最大局部聚类系数
for key,value in clustering.items():
    if(value == max(clustering.values())): #找出聚类系数字典中最大value和对应的key
        print (key,value)'''
values1 = {"节点总数": [float(Nodes)], "    总边数": [float(Edges)], "    连通子图数": [float(subplot_Number)]}
values2 = {"平均最短路径长度":[float(average_length)], " 直径":[float(diameter)],
         "     平均聚类系数":[float(average_clustering)], '平均路径长度':[float(average_length)]}
frame1 = pd.DataFrame(values1, index=["基本信息"], columns=["节点总数", "    总边数", "    连通子图数"])
frame2 = pd.DataFrame(values2, index=["图的属性"], columns=["平均最短路径长度", " 直径", "     平均聚类系数"])
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 100)# 设置打印宽度
print(frame1)
print(frame2)
plt.show()


