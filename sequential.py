def sequential_file_allocation(start_block, file_size, disk_blocks):
    allocated = []
    for i in range(start_block, start_block + file_size):
        if i >= len(disk_blocks) :
            print("File cannot be allocated sequentially.")
            return
        allocated.append(i)
    for block in allocated:
        disk_blocks[block] = 1
    print("File allocated at blocks:", allocated)


disk = [0] * 20  
sequential_file_allocation(5,4,disk)