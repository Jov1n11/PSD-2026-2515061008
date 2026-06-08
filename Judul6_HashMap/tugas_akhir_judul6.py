class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapNPM:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def display(self):
        print("\nData Mahasiswa:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next
            print("NULL")

def main():
    hashmap = HashMapNPM()
    hashmap.insert(2515001, "Andi")
    hashmap.insert(2515011, "Budi")
    hashmap.insert(2515002, "Citra")
    hashmap.insert(2515012, "Dewi")
    hashmap.insert(2515003, "Udin")
    hashmap.insert(2515004, "Yanto")
    hashmap.insert(2515000, "Santi")
    hashmap.display()

    npm = int(input("\nMasukkan NPM yang dicari: "))

    hasil = hashmap.search(npm)
    if hasil is not None:
        print(f"Mahasiswa ditemukan: {hasil.value}")
    else:
        print("Mahasiswa tidak ditemukan")

if __name__ == "__main__":
    main()