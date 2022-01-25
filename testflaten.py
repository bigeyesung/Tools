import open3d as o3d
import numpy as np
from sklearn.cluster import KMeans
import os

towerPath = "/"
towera=o3d.io.read_point_cloud(towerPath+"Tower.ply")
pointArr = np.asarray(towera.points)
pointArr[:, 2] /= 1.2
# clusterer.fit(pointArr)
# pointArr[:, 2] *= 5
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(pointArr)
pcdFile = os.path.join(towerPath, "testflatten.ply")
o3d.io.write_point_cloud(pcdFile, pcd)

kmeans = KMeans(6)   #Using kmeans to do first separation on z values
zpoint = pointArr[:, [2]]
kmeansPCs=[]
#normalize
# norm = np.linalg.norm(xzpoint)
# normal_array = an_array/norm
kmeans=kmeans.fit(zpoint)
klabels = kmeans.labels_
klabelNums = klabels.max()
for grpInd in range(0,klabelNums+1):
    wirept = pointArr[klabels==grpInd,:]
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(wirept)
    kmeansPCs.append(wirept)
    pcdFile = os.path.join(towerPath, "Kmeans_wire_"+str(grpInd)+".ply")
    o3d.io.write_point_cloud(pcdFile, pcd)
