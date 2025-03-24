def q8():
    queue = []

    def enqueue():
        item = input("Enter element to enqueue: ")
        queue.append(item)
        print(f"{item} added to the queue.")

    def dequeue():
        if queue:
            print(f"Dequeued element: {queue.pop(0)}")  # Remove from front
        else:
            print("Queue is empty. Nothing to dequeue.")

    def peek():
        if queue:
            print(f"Front element: {queue[0]}")
        else:
            print("Queue is empty. No front element.")

    def display():
        if queue:
            print("Queue elements:", queue)
        else:
            print("Queue is empty.")

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            enqueue()
        elif choice == '2':
            dequeue()
        elif choice == '3':
            peek()
        elif choice == '4':
            display()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
