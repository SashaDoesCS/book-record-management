class Node:
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  # Each bucket starts as None

    def hashFunction(self, key):
        return abs(hash(key) % self.size)

    def insert(self, isbn, title):
        index = self.hashFunction(isbn)
        new_node = Node(isbn, title)
        
        if self.table[index] is None:
            # No collision, insert directly
            self.table[index] = new_node
        else:
            # Collision: Use linked list to resolve
            current = self.table[index]
            while True:
                if current.isbn == isbn:
                    # ISBN already exists, update the title
                    current.title = title
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node  # Append the new node

    def lookup(self, isbn):
        index = self.hashFunction(isbn)
        current = self.table[index]
        
        while current is not None:
            if current.isbn == isbn:
                return current.title
            current = current.next
        
        return None  # ISBN not found

    def delete(self, isbn):
        index = self.hashFunction(isbn)
        current = self.table[index]
        previous = None
        
        while current is not None:
            if current.isbn == isbn:
                if previous is None:
                    self.table[index] = current.next  # Remove head
                else:
                    previous.next = current.next  # Remove middle or tail
                return True
            previous = current
            current = current.next
        
        return False  # ISBN not found

    def display(self):
        for index in range(self.size):
            current = self.table[index]
            if current:
                print(f"Index {index}: ", end="")
                while current:
                    print(f"({current.isbn}, {current.title}) -> ", end="")
                    current = current.next
                print("None")

def main():
    hash_table = HashTable()
    
    # Sample data with duplicate ISBNs for testing
    sample_data = [
        ("978-3-16-148410-0", "Book A"),
        ("978-1-86197-876-9", "Book B"),
        ("978-1-4028-9462-6", "Book C"),
        ("978-0-262-13472-9", "Book D"),
        ("978-3-16-148410-0", "Book A Updated"),  # Duplicate for collision
        ("978-0-321-48681-5", "Book E"),
        ("978-0-13-110163-0", "Book F"),
        ("978-0-07-042822-7", "Book G"),
        ("978-0-201-50822-6", "Book H"),
        ("978-1-56619-909-4", "Book I"),
        ("978-0-306-40615-7", "Book J"),
        ("978-3-16-148410-0", "Book A Again"),  # Another duplicate
        ("978-1-4028-9462-6", "Book C Updated"),  # Duplicate for collision
        ("978-0-123-45678-9", "Book K"),
        ("978-0-321-14653-8", "Book L"),
        ("978-0-201-63416-5", "Book M"),
        ("978-1-86197-876-9", "Book B Updated"),  # Duplicate for collision
        ("978-1-60309-057-5", "Book N"),
        ("978-1-891830-75-4", "Book O"),
        ("978-0-7356-6743-6", "Book P"),
        ("978-1-56619-909-4", "Book I Updated"),  # Duplicate for collision
    ]
    
    # Insert sample data
    for isbn, title in sample_data:
        hash_table.insert(isbn, title)

    while True:
        print("\nOptions: insert, lookup, delete, display, exit")
        choice = input("Choose an option: ").strip().lower()

        if choice == 'insert':
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            hash_table.insert(isbn, title)
            print(f"Inserted: ({isbn}, {title})")

        elif choice == 'lookup':
            isbn = input("Enter ISBN to lookup: ")
            title = hash_table.lookup(isbn)
            if title:
                print(f"Found: {title}")
            else:
                print("ISBN not found.")

        elif choice == 'delete':
            isbn = input("Enter ISBN to delete: ")
            if hash_table.delete(isbn):
                print(f"Deleted ISBN: {isbn}")
            else:
                print("ISBN not found.")

        elif choice == 'display':
            hash_table.display()

        elif choice == 'exit':
            break

        else:
            print("Invalid option. Please try again.")

main()

'''
Testing done on a separate file.

Testing with 10 records:
Insertion time for 10 records: 0.000142 seconds
Lookup time for 10 records: 0.000053 seconds
Deletion time for 10 records: 0.000045 seconds

Testing with 100 records:
Insertion time for 100 records: 0.000386 seconds
Lookup time for 100 records: 0.002367 seconds
Deletion time for 100 records: 0.001538 seconds

Testing with 1000 records:
Insertion time for 1000 records: 0.004878 seconds
Lookup time for 1000 records: 0.265458 seconds
Deletion time for 1000 records: 0.162941 seconds
'''
