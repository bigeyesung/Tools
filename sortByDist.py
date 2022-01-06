def get_ordered_list(points, x, y, z):
   points.sort(key = lambda p: ((p[0] - x)**2 + (p[1] - y)**2+ (p[2] - z)**2)**0.5)
   return points

points = [[5,0,0],[2,0,0],[10,0,0]]
points = get_ordered_list(points,2,0,0)
print(points)