
def q7():
    l = []
    def push():
        item = input("Enter element to push: ")
        l.append(item)
        print(f"{item} pushed onto the l.")

    def pop():
        if l:
            print(f"Popped element: {l.pop()}")
        else:
            print("l is empty. Nothing to pop.")

    def peek():
        if l:
            print(f"Top element: {l[-1]}")
        else:
            print("l is empty. No top element.")

    def display():
        if l:
            print("l elements:", l[::-1])  # Reverse display (top at index 0)
        else:
            print("l is empty.")

    while True:
        print("\nl Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            push()
        elif choice == '2':
            pop()
        elif choice == '3':
            peek()
        elif choice == '4':
            display()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
