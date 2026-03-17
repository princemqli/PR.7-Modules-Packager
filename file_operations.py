def create_file():
    name = input("Enter file name: ")
    open(name, "w").close()
    print("File created successfully!")

def write_file():
    name = input("Enter file name: ")
    data = input("Enter data to write: ")
    with open(name, "w") as f:
        f.write(data)
    print("Data written successfully!")

def read_file():
    name = input("Enter file name: ")
    with open(name, "r") as f:
        print("File Content:")
        print(f.read())

def append_file():
    name = input("Enter file name: ")
    data = input("Enter data to append: ")
    with open(name, "a") as f:
        f.write("\n" + data)
    print("Data appended successfully!")