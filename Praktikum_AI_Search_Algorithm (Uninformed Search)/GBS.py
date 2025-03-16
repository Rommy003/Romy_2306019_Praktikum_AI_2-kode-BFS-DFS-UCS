from queue import PriorityQueue

# Fungsi heuristik (contoh, Anda perlu mengganti ini sesuai kebutuhan)
def heuristic(node, goal):
    # Di sini Anda perlu mengimplementasikan fungsi heuristik yang sesuai
    # Contoh sederhana (heuristik nol, tidak informatif):
    heuristics = {
        'S': 7,
        'A': 9,
        'B': 4,
        'D': 5,
        'G': 0
    }
    return heuristics.get(node, 0)  # Mengembalikan 0 jika node tidak ditemukan

# Fungsi untuk merekonstruksi jalur
def reconstruct_path(came_from, start, goal):
    current = goal
    path = []

    while current != start:
        path.append(current)
        current = came_from[current]

    path.append(start)
    path.reverse()

    return path

# Fungsi algoritma Greedy Best-First Search
def greedy_search(graph, start, goal):
    frontier = PriorityQueue()  # Antrian prioritas
    frontier.put((heuristic(start, goal), start))  # Tambahkan simpul awal
    came_from = {}  # Menyimpan jalur
    explored = set()  # Menyimpan simpul yang sudah dikunjungi

    while not frontier.empty():
        current_node = frontier.get()[1]  # Ambil simpul dengan nilai heuristik terkecil

        if current_node == goal:
            print("Simpul tujuan ditemukan!")
            path = reconstruct_path(came_from, start, goal)
            print("Jalur terpendek:", path)
            return path  # Kembalikan jalur yang ditemukan

        explored.add(current_node)

        if current_node in graph:  # Tambahkan pemeriksaan ini
            for neighbor in graph[current_node]:
                if neighbor not in explored:
                    frontier.put((heuristic(neighbor, goal), neighbor))
                    came_from[neighbor] = current_node  # Simpan jalur

    print("Simpul tujuan tidak ditemukan!")
    return None

# Graf menggunakan dictionary (graf kedua)
graph = {
    'S': ['A', 'B'],
    'A': ['D', 'B'],
    'D': ['G'],  # Tambahkan 'G' sebagai tetangga 'D' agar 'G' dapat dicapai
    'B': []      # Tambahkan 'B' sebagai simpul tanpa tetangga
}

# Titik awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Panggil fungsi greedy search
greedy_search(graph, start_node, goal_node)
