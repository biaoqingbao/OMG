#分析UPP的路径自相关性
import mdtraj as md  
import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt
from scipy.stats import powerlaw

# 读取轨迹文件,traj为分子体系轨迹,topology为体系拓扑
traj = md.load('prod.xtc', top='6.6.gro')
# 选择目标物质的分子,target为其分子名称


target_atoms = traj.topology.select('resname UPP')  
atom_pairs = np.array([[21783, 3639], [21784, 3639], [21785, 3639],[21786,3639]]) 

# 计算各原子对在每个帧的距离
distances = md.compute_distances(traj, atom_pairs)
lag = 10
# 计算相邻两帧的矩阵
corr = []
for i in range(len(traj)-lag):
    matrix1 = distances[i] 
    matrix2 = distances[i+lag]
    
    # 计算两矩阵之间的相关性系数
    corr.append(np.corrcoef(matrix1, matrix2)[0,1])
#plt.plot(corr)




dists = distances.reshape(1, -1)[0]  

# 使用powerlaw.fit()函数拟合厚尾分布
alpha, loc, beta = powerlaw.fit(dists)  

# 打印结果
print('alpha = ', alpha) 
print('loc = ', loc)
print('beta = ', beta)

with open('power.csv','w') as f:
    f.write(str(alpha)+'\n')
    f.write(str(loc)+'\n')
    f.write(str(beta)+'\n')
'''plt.loglog(dists, dists**-alpha, basex=10)
plt.xlabel('Distance (nm)')
plt.ylabel('P(r) (nm^-alpha)')
plt.margins(0.1, 0.1) 
plt.label=('Alpha = %0.2f loc= %0.2f beta= %0.2f'%( alpha,loc, beta))
plt.savefig("powerlaw.jpg",dpi=600)
plt.show()'''

plt.scatter(dists, np.arange(len(dists)))
#plt.xscale('log')
plt.xlabel('Z-axis Distance (nm)')
plt.ylabel('Count')
plt.title('Scatter plot of distances alpha = %0.2f loc= %0.2f beta= %0.2f' %( alpha,loc, beta))
plt.savefig("distribution.jpg",dpi=600)
#plt.show()
