def dfs(graph, v, visited, stack=None):
    """Обход графа в глубину."""
    visited[v] = True

    for i, connected in enumerate(graph[v]):
        if connected and not visited[i]:
            dfs(graph, i, visited, stack)

    if stack is not None:
        stack.append(v)

def transpose(graph):
    """Транспонирование графа."""
    return [[row[i] for row in graph] for i in range(len(graph))]

def strongly_connected_components(graph):
    """Поиск сильно связанных компонент в графе."""
    stack = []
    visited = [False] * len(graph)

    # Первый обход: добавление вершин в стек
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited, stack)

    transposed_graph = transpose(graph)

    visited = [False] * len(graph)
    components = []

    # Второй обход: поиск компонент на транспонированном графе
    while stack:
        i = stack.pop()
        if not visited[i]:
            component = []
            dfs(transposed_graph, i, visited, component)
            components.append(sorted(component))

    return sorted(components, key=lambda x: x[0])

def scc_interconnection_matrix(graph, components):
    """Построение матрицы связей между сильно связанными компонентами."""
    num_components = len(components)
    matrix = [[0] * num_components for _ in range(num_components)]

    for i, comp_from in enumerate(components):
        for j, comp_to in enumerate(components):
            if i != j:
                for v_from in comp_from:
                    for v_to in comp_to:
                        if graph[v_from][v_to]:
                            matrix[i][j] = 1
                            break
                    if matrix[i][j]:
                        break
                        
    return matrix

# Матрица смежности графа
adj_matrix1 = [
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
# Запасная матрица смежности графа
adj_matrix = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]


components = strongly_connected_components(adj_matrix)

# Вывод сильно связанных компонент
print("Strongly Connected Components:")
for idx, component in enumerate(components, 1):
    print(f"Component {idx}: {component}")

# Вывод матрицы связей между компонентами
print("\nInterconnection Matrix:")
interconnection_matrix = scc_interconnection_matrix(adj_matrix, components)
for row in interconnection_matrix:
    print(row)
