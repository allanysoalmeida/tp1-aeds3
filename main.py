import cv2
from graph import Graph


image_path = "C:\\Users\\admin\\Desktop\\aeds III\\TP1\\toy.bmp"
graph = Graph().create_graph_from_image(image_path)
graph.print_nodes_info(cv2.imread(image_path))

start_node = (8, 3)
end_node = (0, 10)

path = graph.bfs(start_node, end_node)