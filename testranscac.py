from skimage.measure import LineModelND, ransac
import open3d as o3d
import numpy as np

oriwirePt = o3d.io.read_point_cloud("xxx.ply")
oriwirePt = np.asarray(oriwirePt.points)
wirePt = oriwirePt[:,[0,1]]
#only choose x,y
towera = np.array([266375.6976745561,3288816.6450710064,24.45288757396449])
towerb = np.array([266389.8695983147,3288812.5578876445,23.616480337078652])
# rotate such that the x-axis is the line between the towers
rotWirePts = wirePt[:, [0, 1]] - towera[[0, 1]]
towerb = towerb[[0, 1]] - towera[[0, 1]]
angle = np.arctan2(towerb[1], towerb[0])
rotmat = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
rotWirePts = rotWirePts @ rotmat 
towerb = towerb @ rotmat
model, _ = ransac(rotWirePts, LineModelND, min_samples=2,
                  residual_threshold=0.1, max_trials=2000)
v1, v2 = model.params[1]
theta = np.arctan2(v1, v2)
theta2 = np.arctan2(v2, v1)
distance = np.abs((np.pi / 2) - np.abs(theta))

#test points:
oriwirePt[:,[0]]=rotWirePts[:,[0]]
oriwirePt[:,[1]]=rotWirePts[:,[1]]
spanpcd = o3d.geometry.PointCloud()
spanpcd.points = o3d.utility.Vector3dVector(oriwirePt)
o3d.io.write_point_cloud("result.ply", spanpcd)