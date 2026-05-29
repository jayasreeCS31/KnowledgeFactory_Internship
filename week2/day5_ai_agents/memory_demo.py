memory = []
while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("\nConversation Ended")
        break
    memory.append(user)
    print("\nMemory Contents:")
    for msg in memory:
        print("-", msg)
    print()