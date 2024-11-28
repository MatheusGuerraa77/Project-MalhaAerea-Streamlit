# ✈️ **Malha de Transporte Aéreo dos EUA com Dados Reais**  

Este código implementa uma aplicação interativa usando **Python** e **Streamlit** para modelar a malha de transporte aéreo entre aeroportos dos Estados Unidos. A aplicação permite visualizar a rede de conexões entre os aeroportos com base em dados geográficos reais, além de calcular a rota mais curta entre dois pontos e estimar o tempo de voo do aeroporto de origem até o aeroporto de destindo.  

---

## 🚀 Funcionalidades

1. **Calcular Rota Mais Curta**:  
   Utiliza o algoritmo de menor caminho para encontrar a rota mais eficiente entre aeroportos.

2. **Visualização de Rotas Aéreas**:  
   Mapa interativo que destaca a rota calculada em verde e mostra todas as conexões disponíveis em azul.

3. **Cálculos Baseados em Geodésia**:  
   Distâncias entre aeroportos são calculadas utilizando a fórmula de Haversine, considerando a curvatura da Terra.

4. **Informações Detalhadas**:  
   - Distância total da rota (em km).  
   - Tempo estimado de voo (em horas) com base em uma velocidade média de 850 km/h.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Streamlit**: Framework para criar a interface interativa.
- **Matplotlib**: Geração de gráficos e visualizações.
- **NetworkX**: Modelagem e manipulação de grafos.
- **Pillow**: Manipulação de imagens.
- **Geodésia (Haversine)**: Cálculo de distâncias baseadas em coordenadas.

---

## 📍 Aeroportos Modelados

| Código | Cidade                  | Coordenadas (Lat, Lon)      |
|--------|-------------------------|-----------------------------|
| SEA    | Seattle                | (47.4502, -122.3088)       |
| SFO    | San Francisco          | (37.6213, -122.3790)       |
| LAS    | Las Vegas              | (36.0840, -115.1537)       |
| DEN    | Denver                 | (39.8561, -104.6737)       |
| JFK    | Nova York              | (40.6413, -73.7781)        |
| MCO    | Orlando                | (28.4312, -81.3081)        |
| ORD    | Chicago                | (41.9742, -87.9073)        |

---

## 📊 Visualização

1. **Mapa com Conexões**:  
   - **Nós (aeroportos)**: Representados por círculos vermelhos.  
   - **Arestas (rotas)**: Linhas azuis para conexões gerais e verdes para a rota mais curta.  

---

## **💡 O que Este Código Oferece?**
- **Educação:** Excelente exemplo para demonstrar a aplicação de grafos em problemas reais.  
- **Interatividade:** Interface moderna e fácil de usar para simulações.  

**🚀 Experimente usar diferentes aeroportos para explorar rotas otimizadas!** 
