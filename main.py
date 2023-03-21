todo = []
exited = False

def viewList():
    printFormat("-----Current List-----")
    for i in range(0, len(todo)):
        print(f"{i+1}                       {todo[i]}")

def addToList():
    editing = True
    printFormat("Type the new todo item:")
    while editing:
        addition = input("Item: ")
        todo.append(addition)
        if input("Done? y/n: ") == "y":
            editing = False

def deleteFromList():
    printFormat("Type the item number to delete:")
    index = int(input("Item number: "))
    todo.pop(index - 1)

def exit_loop():
    exited = True
    exit()

choices = {
    1: viewList,
    2: addToList,
    3: deleteFromList,
    4: exit_loop
}

def printFormat(s):
    print(s.center(70))

def printMenu():
    printFormat("-----Welcome to the Todo List-----")
    print("\n")
    printFormat("What do you want to do?")
    print("1: View List")
    print("2: Add Item")
    print("3: Delete Item")
    print("4: Exit")

while(not exited):
    printMenu()
    choice = int(input("- "))
    if choice > 0 and choice < 5:
        choices[choice]()
