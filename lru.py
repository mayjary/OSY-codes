def lru(pages, capacity):
    frame = []
    page_faults = 0
    print("Page\t\tFrame\t\t\tPage Fault")

    for i in range(len(pages)):
        page = pages[i]
        if page not in frame:
            if len(frame) < capacity:
                frame.append(page)
            else:
                recent_pages = pages[:i]
                lru_page = None
                least_index = i

                for f in frame:
                    if f in recent_pages:
                        last_use = len(recent_pages) - 1 - recent_pages[::-1].index(f)
                        if last_use < least_index:
                            least_index = last_use
                            lru_page = f
                    else:
                        lru_page = f
                        break
                frame.remove(lru_page)
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

capacity = int(input("Enter Total no. of Frames: "))
lru(pages, capacity)