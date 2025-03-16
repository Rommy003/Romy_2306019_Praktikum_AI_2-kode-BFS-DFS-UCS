# Python3 program to print DFS traversal
# from a given graph

from collections import defaultdict

# Kelas ini merepresentasikan sebuah graf yang diarahkan
# menggunakan representasi daftar kejadian
class Graph:

    # Konstruktor
    def __init__(self):
        # Kamus default untuk menyimpan graf
        self.graph = defaultdict(list)

    # Fungsi untuk menambahkan tepi ke graf
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Fungsi yang digunakan oleh DFS
    def DFSUtil(self, v, visited):
        # Tandai node saat ini sebagai sudah dikunjungi
        # dan cetak
        visited.add(v)
        print(v, end=' ')

        # Panggil rekursif untuk semua titik ujung
        # yang berdekatan dengan titik ini
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # Fungsi untuk memulai traversal DFS dari node tertentu
    def DFS(self, v):
        # Tandai semua node sebagai tidak dikunjungi
        visited = set()
        # Panggil fungsi pembantu rekursif untuk mencetak traversal DFS
        self.DFSUtil(v, visited)

# Contoh penggunaan
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("DFS traversal dari node 2:")
g.DFS(2)
# Fungsi untuk melakukan penelusuran DFS. Ini menggunakan
# DFSUtil() rekursif
def DFS(self, v):

    # Buat himpunan untuk menyimpan node yang sudah dikunjungi
    visited = set()

    # Panggil fungsi bantu rekursif
    # untuk mencetak penelusuran DFS
    self.DFSUtil(v, visited)

# Kode pengguna
if __name__ == "__main__":

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Berikut adalah Penelusuran Depth First (dimulai dari node 2)")

    # Panggilan fungsi
    g.DFS(2)

# Kode ini disumbangkan oleh Neelam Yadav
