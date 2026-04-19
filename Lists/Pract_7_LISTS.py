queue = []

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = int(input("Enter element: "))
        queue.append(item)
        print("Element added")

    elif choice == 2:
        if queue:
            print("Removed element:", queue.pop(0))
        else:
            print("Queue is empty")

    elif choice == 3:
        print("Queue:", queue)

    elif choice == 4:
        print("Exiting program")
        break

    else:
        print("Invalid choice")
