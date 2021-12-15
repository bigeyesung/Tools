# %%
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
class Line:
    def __init__(self, vector, point_on_line) -> None:
        self.vector = np.array(vector).reshape(3, 1)
        self.point_on_line = np.array(point_on_line).reshape(3, 1)

    def plot(self, step_size=1):
        points = np.zeros((3, 0))
        for i in np.arange(0, 4, step_size):
            scale = 0.25*i
            points = np.concatenate(
                (points, self.point_on_line + scale * self.vector), axis=1)
        showPoints = points.T

        print(showPoints)
        for pt in showPoints:
            print(pt)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(points[0, :].ravel(),
                   points[1, :].ravel(),
                   points[2, :].ravel(),
                   s=1)
        ax.scatter(*self.point_on_line, "r")
        plt.show()

# pointa = np.array([28134.37655462186, 4685641.667899161, 166.77689075630255])
# pointb = np.array([28222.083070652196, 4685439.620896738, 164.88788043478252])
# dist = np.linalg.norm(pointa-pointb)
# vector = (pointb-pointa)
# point_on_line = [28134.37655462186, 4685641.667899161, 166.77689075630255]
# line = Line(vector, point_on_line)
# line.plot()


#draw network
graph = nx.Graph()
# graph.add_node(0, data="tower0")
# graph.add_node(1, data="tower1")
# graph.add_node(2, data="tower2")
# graph.add_edges_from([(0,2)])
# graph.add_edges_from([(0,1)])
graph.add_edge('A', 'B')
graph.add_edge('B', 'D')
nx.draw(graph, with_labels=True, font_weight='bold')
plt.show()