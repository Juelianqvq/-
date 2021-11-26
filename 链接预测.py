# -*- coding = utf-8 -*-
# @Time : 2020/12/19 0:12
# @Author : K先生
# @File : exercise.py
# @Software : PyCharm

import networkx as nx
import matplotlib.pyplot as plt
import random
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

G=nx.read_edgelist("cora.cites",create_using=nx.Graph(),nodetype=int)
#plt.savefig("ba.png")
# nx.write_gexf(G,"F.gexf")
# partition = community.best_partition(G)
pos = nx.spring_layout(G)
# values = [partition.get(node) for node in G.nodes()]
# nx.draw_networkx(G, pos, cmap=plt.get_cmap('rainbow'), node_color=values, node_size=50, with_labels=False)
# plt.show()
# print(nx.info(G))

edge_subset = random.sample(G.edges(), int(0.25 * G.number_of_edges()))
# remove some edges
G_train = G.copy()
G_train.remove_edges_from(edge_subset)
plt.figure(figsize=(12,8))
nx.draw(G_train, pos=pos)
plt.show()

edge_subset_size = len(list(edge_subset))
print("Deleted : ", str(edge_subset_size))
print("Remaining : ", str((G.number_of_edges() - edge_subset_size)))
# 先使用Jaccard系数进行预测：
# Make prediction using Jaccard Coefficient
pred_jaccard = list(nx.jaccard_coefficient(G_train))
score_jaccard, label_jaccard = zip(*[(s, (u,v) in edge_subset) for (u,v,s) in pred_jaccard])
# 打印前10组结果
print(pred_jaccard[0:10])
# 预测结果如下，其中第一个是节点，第二个是节点，最后一个是Jaccard分数（用来表示两个节点之间边预测的概率）

# 我们现在计算Adamic-Adar指数和对应的ROC-AUC分数
# Prediction using Adamic Adar
pred_adamic = list(nx.adamic_adar_index(G_train))
score_adamic, label_adamic = zip(*[(s, (u,v) in edge_subset) for (u,v,s) in pred_adamic])
print(pred_adamic[0:10])
# Compute the ROC AUC Score
fpr_adamic, tpr_adamic, _ = roc_curve(label_adamic, score_adamic)
auc_adamic = roc_auc_score(label_adamic, score_adamic)
print(auc_adamic)

# 同样，我们可以计算Preferential Attachment得分和对应的ROC-AUC分数
# Compute the Preferential Attachment
pred_pref = list(nx.preferential_attachment(G_train))
score_pref, label_pref = zip(*[(s, (u,v) in edge_subset) for (u,v,s) in pred_pref])
print(pred_pref[0:10])
fpr_pref, tpr_pref, _ = roc_curve(label_pref, score_pref)
auc_pref = roc_auc_score(label_pref, score_pref)
print(auc_pref)

# 然后我们可以使用ROC-AUC标准来比较不同模型的性能，因为我们既有真实的边（label），也有预测边的概率（score）
# Compute the ROC AUC Score
# 其中，FPR是False Positive Rate， TPR是True Positive Rate
fpr_jaccard, tpr_jaccard, _ = roc_curve(label_jaccard, score_jaccard)
auc_jaccard = roc_auc_score(label_jaccard, score_jaccard)
print(auc_jaccard)

plt.figure(figsize=(12, 8))
plt.plot(fpr_jaccard, tpr_jaccard, label='Jaccard Coefficient - AUC %.2f' % auc_jaccard, linewidth=4)
plt.plot(fpr_adamic, tpr_adamic, label='Adamic-Adar - AUC %.2f' % auc_adamic, linewidth=4)
plt.plot(fpr_pref, tpr_pref, label='Preferential Attachment - AUC %.2f' % auc_pref, linewidth=4)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title("ROC AUC Curve")
plt.legend(loc='lower right')
plt.show()

