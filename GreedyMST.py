def Prim(G):
    # Membentuk MST kosong
    T = []
    
    # Menandai semua simpul belum dikunjungi
    visited = set()

    # Memilih simpul awal secara acak
    start_node = list(G.keys())[0]
    visited.add(start_node)

    # Mengulangi sampai semua simpul dikunjungi
    while len(visited) < len(G):
        min_weight = float('inf')
        min_edge = None

        # Mencari sisi terkecil yang tersambung dengan simpul yang telah dikunjungi
        for u in visited:
            for v, weight in G[u].items():
                if v not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (u, v)

        # Menambahkan sisi terkecil ke MST dan menandai simpul yang dikunjungi
        u, v = min_edge
        T.append((u, v))
        visited.add(v)

    return T

# Contoh penggunaan
G = {
    'A': {'B': 1, 'C': 3, 'E': 6},
    'B': {'A': 1, 'C': 2, 'D': 3, 'E': 5},
    'C': {'A': 3, 'B': 2, 'D': 5, 'F': 2},
    'D': {'B': 3, 'C': 5, 'E': 2, 'F': 4},
    'E': {'A': 6, 'B': 5, 'D': 2, 'F': 1},
    'F': {'C': 2, 'D': 4, 'E': 1}
}

MST = Prim(G)
print("Minimum Spanning Tree (Prim):")
for u, v in MST:
    print(f"{u} - {v} : {G[u][v]}")