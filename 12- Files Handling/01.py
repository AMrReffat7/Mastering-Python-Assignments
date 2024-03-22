import os

# Define directory path
directory = r"C:\Users\A L I\Desktop\Python"

def main():
    # Create files and write content
    create_files()

    # Print directory and file information
    print_directory_info(directory)

    # Append content to txt1.txt
    append_content_to_txt1()

    # Print statistics for txt1.txt
    print_file_statistics(os.path.join(directory, "txt1.txt"))

    # Remove last 10 files
    remove_last_10_files()

def create_files():
    i = 0
    for file in range(1, 51):
        filename = "special-text.txt" if file == 25 else f"txt{file}.txt"
        with open(os.path.join(directory, filename), "w") as f:
            i += 1
            f.write(f"Elzero Web School => {i}\n" if i < 25 else f"Elzero Web School => {i + 1}\n")

def print_directory_info(directory):
    print(f"Current Working Directory: {os.getcwd()}")
    print("=" * 40)
    print("Number of Files:", len(os.listdir(directory)))
    print("=" * 40)

def append_content_to_txt1():
    with open(os.path.join(directory, "txt1.txt"), "a") as f:
        f.write("Appended => Elzero Web School\n" * 50)

def print_file_statistics(filepath):
    with open(filepath, "r") as f:
        content = f.read()
        lines = len(content.splitlines())
        words = len(content.split())
        characters = len(content.replace(" ", "").replace("\n", ""))
        character_l = content.count('l')
        print(f"Number of Lines: {lines}")
        print(f"Number of Words: {words}")
        print(f"Number of Characters: {characters}")
        print(f"Number of Character [l]: {character_l}")
        print("=" * 40)

def remove_last_10_files():
    for i in range(50, 40, -1):
        os.remove(os.path.join(directory, f"txt{i}.txt"))

if __name__ == "__main__":
    main()
