import itertools #library untuk pemrosesan data berulang, permutasi, kombinasi.

def calculate_total_weight(graph, subgraph):
    # Menghitung total bobot dari sebuah subgraf.
    # Fungsi ini melakukan iterasi melalui setiap sisi dalam subgraf dan menambahkan bobotnya ke total_weight
    total_weight = 0
    for u, v, weight in subgraph:
        total_weight += weight
    return total_weight

def is_valid_subgraph(subgraph):
    # Memeriksa apakah subgraf yang dibentuk valid, yaitu setiap simpul hanya dikunjungi tepat satu kali.
    # Fungsi ini menghitung jumlah simpul unik dalam subgraf dan membandingkannya dengan jumlah sisi dalam subgraf ditambah satu.
    nodes = set()
    for u, v, _ in subgraph:
        nodes.add(u)
        nodes.add(v)
    return len(nodes) == len(subgraph) + 1

def brute_force_mst(graph):
    # Implementasi algoritma brute force untuk mencari MST.
    # Variabel min_weight diinisialisasi dengan nilai tak terhingga (infinity) dan min_subgraph dengan daftar kosong.
    # Variabel nodes mengambil semua simpul dalam graf dengan menggunakan metode keys().
    min_weight = float('inf')
    min_subgraph = []

    nodes = [node for node in graph.keys()] # Mengambil semua simpul graf

    for permutation in itertools.permutations(nodes):
        # Loop pertama menggunakan itertools.permutations untuk menghasilkan semua kemungkinan permutasi simpul
        subgraph = []
        is_valid = True
        for i in range(len(permutation) - 1):
            u = permutation[i]
            v = permutation[i + 1]
            if u in graph and v in graph[u]:
                # Ditambahkan ke subgraf jika mereka ada dalam graf.
                subgraph.append((u, v, graph[u][v]))
            else:
                is_valid = False
                break

        if is_valid and is_valid_subgraph(subgraph):
            # Subgraf diperiksa dengan fungsi is_valid_subgraph untuk memastikan bahwa setiap simpul dikunjungi tepat satu kali.
            total_weight = calculate_total_weight(graph, subgraph)
            if total_weight < min_weight:
                # Jika bobot total lebih kecil dari min_weight dan subgraf valid, maka bobot dan subgraf tersebut diperbarui.
                min_weight = total_weight
                min_subgraph = subgraph

    return min_subgraph, min_weight

# Penggunaan
graph = {
    'v1': {'v2': 1, 'v3': 3, 'v5': 6},
    'v2': {'v1': 1, 'v3': 2, 'v4': 3, 'v5': 5},
    'v3': {'v1': 3, 'v2': 2, 'v4': 5, 'v6': 2},
    'v4': {'v2': 3, 'v3': 5, 'v5': 2, 'v6': 4},
    'v5': {'v1': 6, 'v2': 5, 'v4': 2, 'v6': 1},
    'v6': {'v3': 2, 'v4': 4, 'v5': 1}
}

mst, total_weight = brute_force_mst(graph)
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total Bobot:", total_weight)
