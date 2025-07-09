class DataCollection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        return f"DataCollection({self.data})"

def main():
    collection = DataCollection([1, 2, 3, 4, 5])

    print(f"DataCollection: {collection}")

    # Iterate
    for item in collection:
        print(item)
    
    # Unpacking
    a, b, c, d, e = collection
    print(a,c)

    # Indexing
    print(f"Element at index 0: {collection[0]}")
    print(f"Element at last position: {collection[-1]}")

    # Slicing
    print(collection[1:4])

    print(f"Length of collection: {len(collection)}")

if __name__ == "__main__":
    main()