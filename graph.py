import cv2
import numpy as np
from typing import List, Any

class Graph:
    def __init__(self, image_path):
        self.graph = self.create_graph(image_path)

    def create_graph(self, image_path):
        img = cv2.imread(image_path)
        height, width, _ = img.shape
        adjacency_list = {}

        for y in range(height):
            for x in range(width):
                current_color = img[y, x].tolist()
                current_node = (y, x)

                if current_node not in adjacency_list:
                    adjacency_list[current_node] = {"color": current_color, "neighbors": []}

                # Verifica vizinhos na horizontal e vertical
                neighbors = [
                    (y - 1, x),  # acima
                    (y, x - 1),  # à esquerda
                    (y, x + 1),  # à direita
                    (y + 1, x),  # abaixo
                ]

                for neighbor_y, neighbor_x in neighbors:
                    if 0 <= neighbor_y < height and 0 <= neighbor_x < width:
                        neighbor_color = img[neighbor_y, neighbor_x].tolist()
                        neighbor_node = (neighbor_y, neighbor_x)

                        # Restrição: Nós pretos só se ligam a outros nós pretos
                        if current_color == [0, 0, 0] and neighbor_color == [0, 0, 0]:
                            adjacency_list[current_node]["neighbors"].append(neighbor_node)
                        elif current_color != [0, 0, 0] and neighbor_color != [0, 0, 0] and (current_node[0] == neighbor_node[0] or current_node[1] == neighbor_node[1]):
                            # Outros nós se ligam sem criar arestas diagonais
                            adjacency_list[current_node]["neighbors"].append(neighbor_node)

        return adjacency_list

    def get_num_edges(self):
        count = 0
        for neighbors in self.graph.values():
            count += len(neighbors["neighbors"])
        return count // 2

    def print_graph(self):
        for node, attributes in self.graph.items():
            neighbors_str = ', '.join([str(neighbor) for neighbor in attributes['neighbors']])
            print(f"Node: {node} | Color: {attributes['color']} | Neighbors: {neighbors_str}")

    def bfs_path(self, start_color: List[int], end_color: List[int]) -> List[Any]:
        """
        Perform Breadth-First Search (BFS) from the source node with the specified color
        to the destination node with the specified color, avoiding nodes with another color.

        Parameters:
        - start_color: The color of the source node.
        - end_color: The color of the destination node.

        Returns:
        A list representing the path from the source to the destination, avoiding nodes with another color.
        """
        start_node = None
        end_node = None

        # Find the nodes with the specified colors
        for node, attributes in self.graph.items():
            if attributes["color"] == start_color:
                start_node = node
            elif attributes["color"] == end_color:
                end_node = node

        if start_node is None or end_node is None:
            raise ValueError("Source or destination node not found with the specified colors.")

        desc = {node: 0 for node in self.graph}
        Q = [start_node]
        R = [start_node]
        desc[start_node] = 1

        while len(Q) > 0:
            u = Q.pop(0)
            for v in self.graph[u]["neighbors"]:
                if desc[v] == 0 and self.graph[v]["color"] != [0, 0, 0]:
                    desc[v] = 1
                    Q.append(v)
                    R.append(v)

        return R