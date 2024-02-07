import cv2
from graph import Graph
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image_path = "C:\\Users\\UFOP PID\\Desktop\\allanys-tp1 aeds3 repository\\tp1-aeds3\\Datasets\\toyLaydown\\toy_0.bmp"
img = cv2.imread(image_path)

# Criar o grafo e carregar a imagem
graph = Graph()
graph.create_graph_from_image(image_path)
graph.find_shortest_path()

img = cv2.imread(image_path)
img = img / 255.0
img = np.flip(img, axis=0)

x_coords = []
y_coords = []
colors = []

for node, neighbors in graph.adj.items():
    y, x = node
    color = img[y, x].tolist()
    if color == [0, 0, 255]:  # Cor (0, 0, 255) representada como vermelho
        color = [1, 0, 0]  # Vermelho em formato RGB
    x_coords.append(x)
    y_coords.append(y)
    colors.append(color)

colors = np.array(colors)

# Plotar os nós
plt.figure(figsize=(8, 6))
plt.scatter(x_coords, y_coords, c=colors, s=100)
plt.title('Graph Visualization')
#plt.xlabel('X Coordinate')
#plt.ylabel('Y Coordinate')
#plt.grid(True)
plt.show()