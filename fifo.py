def fifo(pages, capacity):
    frame = []
    page_faults = 0
    print("Pages\t\tFrames\t\t\tPage Fault")

    for page in pages:
        if page not in frame:
            if len(frame) < capacity:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_faults += 1
            fault = "Yes"
        else:
            fault = "No"

        print(str(page) + "\t\t" + str(frame) + "\t\t\t" + fault)

    print("Total Page Faults = ", page_faults)

n = int(input("Enter Total No. of Pages: "))
pages = []
for i in range(n):
    p = int(input("Enter Page " + str(i+1) + ": "))
    pages.append(p)

capacity = int(input("Enter No. of Frames: "))
fifo(pages, capacity)