import random
import string
import time #needs to be implemented in here

'''Since we need to:
Test the hash table with 10, 100, and 1000 records.
Measure and comment on the time performance for lookup, insertion, and deletion operations.

I thought it would be easier to separate the testing from the main one with user input. Once the performance is tested, it can be added into the comments on the main.py file
'''

class Node:
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hashFunction(self, key):
        return abs(hash(key) % self.size)

    def insert(self, isbn, title):
        index = self.hashFunction(isbn)
        new_node = Node(isbn, title)
        
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while True:
                if current.isbn == isbn:
                    current.title = title
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node

    def lookup(self, isbn):
        index = self.hashFunction(isbn)
        current = self.table[index]
        
        while current is not None:
            if current.isbn == isbn:
                return current.title
            current = current.next
        
        return None

    def delete(self, isbn):
        index = self.hashFunction(isbn)
        current = self.table[index]
        previous = None
        
        while current is not None:
            if current.isbn == isbn:
                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        
        return False

    def display(self):
        for index in range(self.size):
            current = self.table[index]
            if current:
                print(f"Index {index}: ", end="")
                while current:
                    print(f"({current.isbn}, {current.title}) -> ", end="")
                    current = current.next
                print("None")

def generate_isbn():
    # Generate a random ISBN for testing
    return ''.join(random.choices(string.digits, k=13))

def main():
    sizes = [10, 100, 1000]
    
    for size in sizes:
        print(f"\nTesting with {size} records:")
        hash_table = HashTable(size)

        for _ in range(size):
            isbn = generate_isbn()
            title = f"Book {isbn[-1]}"  # Simple title using last digit of ISBN
            hash_table.insert(isbn, title)

        hash_table.display()

if __name__ == "__main__":
    main()
