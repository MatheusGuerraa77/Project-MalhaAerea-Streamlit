import streamlit as st
import math
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image

# Função para calcular a distância geodésica (Haversine)
def calculate_distance(coord1, coord2):
    R = 6371  # Raio médio da Terra em km
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    distance = 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return distance

# Aeroportos e suas coordenadas geográficas reais (latitude, longitude)
airports_project = {
    "Seattle (SEA)": (47.4502, -122.3088),
    "San Francisco (SFO)": (37.6213, -122.3790),
    "Las Vegas (LAS)": (36.0840, -115.1537),
    "Denver (DEN)": (39.8561, -104.6737),
    "New York (JFK)": (40.6413, -73.7781), 
    "Orlando (MCO)": (28.4312, -81.3081),  
    "Chicago (ORD)": (41.9742, -87.9073),  
}

# Definição das rotas e cálculo dos pesos (distância entre os aeroportos)
routes_project = [
    ("Seattle (SEA)", "San Francisco (SFO)"),
    ("San Francisco (SFO)", "Las Vegas (LAS)"),
    ("Las Vegas (LAS)", "Denver (DEN)"),
    ("Seattle (SEA)", "Denver (DEN)"),
    ("New York (JFK)", "Chicago (ORD)"),      
    ("New York (JFK)", "Orlando (MCO)"),     
    ("Chicago (ORD)", "Denver (DEN)"),        
    ("Orlando (MCO)", "Las Vegas (LAS)"),     
]

# Criar o grafo
G_project = nx.Graph()
for airport, coord in airports_project.items():
    G_project.add_node(airport, pos=coord)

for route in routes_project:
    coord1 = airports_project[route[0]]
    coord2 = airports_project[route[1]]
    distance = calculate_distance(coord1, coord2)
    G_project.add_edge(route[0], route[1], weight=distance)

# Obter posições dos nós (usando latitude e longitude para visualização no mapa)
pos_project = {
    "Seattle (SEA)": (220, 1150),
    "San Francisco (SFO)": (85, 690),
    "Las Vegas (LAS)": (325, 570),
    "Denver (DEN)": (710, 680),
    "New York (JFK)": (1760, 800),  
    "Orlando (MCO)": (1610, 220),  
    "Chicago (ORD)": (1280,780),  
}


# Implementação para encontrar a rota mais curta entre todos os pares
def find_shortest_path(graph, source, target):
    path = nx.shortest_path(graph, source=source, target=target, weight="weight")
    distance = nx.shortest_path_length(graph, source=source, target=target, weight="weight")
    return path, distance

# Carregar o mapa
image_path = "data/mapaairport.png"
map_image = Image.open(image_path)

# Streamlit Interface
st.title("Malha de Transporte Aéreo dos EUA com Dados Reais")
st.sidebar.title("Opções de Rotas")

# Escolher os aeroportos de origem e destino
source_airport = st.sidebar.selectbox("Selecione o aeroporto de origem", list(airports_project.keys()))
target_airport = st.sidebar.selectbox("Selecione o aeroporto de destino", list(airports_project.keys()))

# Calcular a rota mais curta entre os dois aeroportos
if source_airport != target_airport:
    shortest_path, shortest_distance = find_shortest_path(G_project, source_airport, target_airport)
    avg_speed = 850  # Velocidade média do avião em km/h
    flight_time = shortest_distance / avg_speed  # Tempo médio de voo

    # Exibir informações
    st.write(f"**Origem:** {source_airport}")
    st.write(f"**Destino:** {target_airport}")
    st.write(f"**Rota mais curta:** {' ➝ '.join(shortest_path)}")
    st.write(f"**Distância total:** {shortest_distance:.2f} km")
    st.write(f"**Tempo médio de voo:** {flight_time:.2f} horas")

    # Plotar o mapa e grafo
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.imshow(map_image, extent=[0, 2000, 0, 1200], alpha=0.8)

    # Desenhar o grafo completo
    nx.draw_networkx_nodes(G_project, pos_project, node_size=100, node_color="red", ax=ax)
    nx.draw_networkx_edges(G_project, pos_project, edge_color="blue", alpha=0.5, ax=ax)

    # Destacar a rota mais curta
    shortest_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
    nx.draw_networkx_edges(G_project, pos_project, edgelist=shortest_edges, edge_color="green", width=2, ax=ax)

    # Exibir pesos das arestas (distâncias)
    edge_labels = nx.get_edge_attributes(G_project, 'weight')
    nx.draw_networkx_edge_labels(
        G_project, pos_project, edge_labels={k: f"{v:.1f} km" for k, v in edge_labels.items()}, font_size=8, ax=ax
    )

    # Adicionar título
    ax.set_title(
        f"Malha de Transporte Aéreo - Rota Mais Curta de {source_airport} para {target_airport}",
        fontsize=14,
    )
    ax.axis("off")
    st.pyplot(fig)
else:
    st.write("Por favor, selecione dois aeroportos diferentes para calcular a rota.")
