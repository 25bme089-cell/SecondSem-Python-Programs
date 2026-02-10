stack = []

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element to push: "))
        stack.append(item)
        print("Element pushed successfully")

    elif choice == 2:
        if stack:
            print("Popped element:", stack.pop())
        else:
            print("Stack is empty")

    elif choice == 3:
        if stack:
            print("Top element:", stack[-1])
        else:
            print("Stack is empty")

    elif choice == 4:
        print("Stack elements:", stack)

    elif choice == 5:
        print("Exiting program")
        break

    else:
        print("Invalid choice")
