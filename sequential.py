def sequential_file_allocation(disk, file_name, start, length):
    n = len(disk)

    # Check bounds
    if start + length > n:
        print(f"Cannot allocate {file_name}: Out of disk bounds.")
        return

    # Check if blocks are free
    for i in range(start, start + length):
        if disk[i] != -1:
            print(f"Cannot allocate {file_name}: Block {i} already allocated.")
            return

    # Allocate file
    for i in range(start, start + length):
        disk[i] = file_name
    print(f"File '{file_name}' allocated from Block {start} to Block {start + length - 1}.")


def display_disk(disk):
    print("\nDisk Status:")
    for i in range(len(disk)):
        print(f"Block {i}: {disk[i]}")
    print("-" * 40)


# Main program
if __name__ == "__main__":
    size = int(input("Enter total number of disk blocks: "))
    disk = [-1] * size

    while True:
        print("\nMenu: 1. Allocate File  2. Display Disk  3. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            file_name = input("Enter file name: ")
            start = int(input("Enter starting block: "))
            length = int(input("Enter length of file (in blocks): "))
            sequential_file_allocation(disk, file_name, start, length)

        elif choice == 2:
            display_disk(disk)

        elif choice == 3:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")
