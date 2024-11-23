# ✈️ **Malha de Transporte Aéreo dos EUA com Dados Reais**  

Este código implementa uma aplicação interativa usando **Python** e **Streamlit** para modelar a malha de transporte aéreo entre aeroportos dos Estados Unidos. A aplicação permite visualizar a rede de conexões entre os aeroportos, calcular a rota mais curta entre dois pontos e estimar o tempo de voo.  

---

## **🛠️ Funcionalidades do Código**  

### **1️⃣ Modelagem da Rede Aérea com Grafos**
- **Nós (Aeroportos):** Cada aeroporto é representado como um nó no grafo, com suas coordenadas geográficas reais (latitude e longitude).  
- **Arestas (Rotas Aéreas):** As rotas conectando os aeroportos são modeladas como arestas ponderadas, onde o peso é a **distância geodésica** calculada usando a fórmula de Haversine.  

### **2️⃣ Algoritmo de Busca**
- Implementação do **algoritmo de menor caminho (Dijkstra)** para encontrar a rota mais curta entre dois aeroportos com base na distância.  

### **3️⃣ Interface Gráfica Interativa**
- Criação de uma interface em **Streamlit** para:  
  - Escolher aeroportos de origem e destino.  
  - Exibir informações detalhadas da rota mais curta, como distância total e tempo médio de voo.  
  - Visualizar a malha de transporte em um mapa interativo.  

### **4️⃣ Visualização Gráfica**
- Utilização do **Matplotlib** para renderizar o mapa e a rede aérea:  
  - **Mapa base:** Uma imagem de fundo que simula a localização geográfica dos aeroportos.  
  - **Grafo Completo:** Conexões entre todos os aeroportos desenhadas com arestas azuis.  
  - **Rota Mais Curta:** Destacada em verde no mapa, indicando claramente o trajeto otimizado.  
  - **Rótulos das Distâncias:** As distâncias entre aeroportos são exibidas diretamente nas arestas do grafo.  

---

## **📊 Tecnologias Utilizadas**
- **Python:** Linguagem de desenvolvimento.  
- **Streamlit:** Framework para criar a interface interativa.  
- **NetworkX:** Biblioteca para modelar e manipular grafos.  
- **Geopy:** Cálculo da distância geodésica entre coordenadas.  
- **Matplotlib:** Renderização do grafo e mapa.  
- **Pillow (PIL):** Manipulação de imagens para exibir o mapa base.  

---

## **🎯 Funcionalidade Principal**
### **Cálculo da Rota Mais Curta**
1. **Seleção dos Aeroportos:**  
   A partir da barra lateral, o usuário escolhe os aeroportos de origem e destino.  
2. **Resultado Detalhado:**  
   - **Rota mais curta:** Exibição da sequência de aeroportos no caminho.  
   - **Distância total:** Em quilômetros.  
   - **Tempo médio de voo:** Com base na velocidade média de 850 km/h.  
3. **Visualização:**  
   O mapa exibe a rota mais curta destacada em verde, com os pesos das arestas visíveis.  

---

## **📌 Fluxo do Código**
1. **Definição dos Dados:**  
   - Coordenadas reais dos aeroportos e rotas aéreas conectando-os.  
2. **Cálculo das Distâncias:**  
   Uso da fórmula de Haversine para calcular o peso das arestas (distância geográfica).  
3. **Modelagem do Grafo:**  
   Construção do grafo utilizando a biblioteca NetworkX.  
4. **Interface do Usuário:**  
   - Streamlit apresenta opções para selecionar os aeroportos e exibe os resultados.  
5. **Visualização no Mapa:**  
   - Renderização do grafo sobreposto a um mapa geográfico.

---

## **💡 O que Este Código Oferece?**
- **Educação:** Excelente exemplo para demonstrar a aplicação de grafos em problemas reais.  
- **Planejamento:** Pode ser adaptado para redes logísticas e transporte.  
- **Interatividade:** Interface moderna e fácil de usar para simulações.  

**🚀 Experimente usar diferentes aeroportos para explorar rotas otimizadas!**  
