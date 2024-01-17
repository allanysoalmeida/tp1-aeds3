import cv2
from collections import deque
import numpy as np
from typing import List, Any

class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node: Any) -> None:
        if node not in self.adj:
            self.adj[node] = {}

    def add_edge(self, u: Any, v: Any) -> None:
        self.adj[u][v] = 1

    def is_valid_neighbor(self, y, x, height, width):
        return 0 <= y < height and 0 <= x < width

    def create_graph_from_image(self, image_path):
        img = cv2.imread(image_path)
        height, width, _ = img.shape

        for y in range(height):
            for x in range(width):
                current_node = (y, x)
                current_color = tuple(img[y, x])

                self.add_node(current_node)

                valid_neighbors = [(y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x)]

                for neighbor_y, neighbor_x in valid_neighbors:
                    if self.is_valid_neighbor(neighbor_y, neighbor_x, height, width):
                        neighbor_node = (neighbor_y, neighbor_x)
                        neighbor_color = tuple(img[neighbor_y, neighbor_x])

                        if current_color == (0, 0, 0) and neighbor_color == (0, 0, 0):
                            self.add_edge(current_node, neighbor_node)

                        if current_color != (0, 0, 0) and neighbor_color != (0, 0, 0):
                            self.add_edge(current_node, neighbor_node)

        return self

    def bfs(self, start: Any, end: Any) -> List[Any]:
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            current_node, path = queue.popleft()

            if current_node == end:
                self.print_arrows_for_path(path)
                return path

            visited.add(current_node)
            neighbors = self.adj[current_node]

            for neighbor in neighbors:
                if neighbor not in visited:
                    next_path = path + [neighbor]
                    queue.append((neighbor, next_path))
                    visited.add(neighbor)

        print("path not found")
        return []

    def print_arrows_for_path(self, path: List[Any]) -> None:
        
        print("\n \n----------------------BFS PATH----------------------\n ")
        if not path:
            return

        for i in range(len(path) - 1):
            current_node = path[i]
            next_node = path[i + 1]

            y_diff = next_node[0] - current_node[0]
            x_diff = next_node[1] - current_node[1]

            if y_diff == 1:
                print("vv", end=" ")
            elif y_diff == -1:
                print("^^", end=" ")
            elif x_diff == 1:
                print(">>", end=" ")
            elif x_diff == -1:
                print("<<", end=" ")
                
        print("\n")

        print()

    def count_edges(self) -> int:
        return sum(len(neighbors) for neighbors in self.adj.values())

    def print_nodes_info(self, img):
        for node, neighbors in self.adj.items():
            print(f"Node: {node}, Color: {img[node[0], node[1]].tolist()}, Neighbors: {list(neighbors.keys())}")
