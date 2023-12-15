from graph import Graph
from graph_visualization import *

image_path = "C:\\Users\\admin\\Desktop\\aeds III\\TP1\\toy.bmp"
graph_instance = Graph(image_path)
graph_instance.print_graph()

start_color = [0, 0, 255]  # Cor do nó de origem
end_color = [0, 255, 0]    # Cor do nó de destino

# Realizar BFS do nó de origem ao nó de destino, evitando nós pretos
path = graph_instance.bfs_path(start_color, end_color)
print("BFS Path:", path)
print(f"Número de arestas: {graph_instance.get_num_edges()}")

graph_instance.visualize_2d(graph, 12, 9)