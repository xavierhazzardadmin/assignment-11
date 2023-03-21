todo = []
exited = False

def printItem(index, string, priority):
    print(index, end="")
    print(string.center(69), end="")
    print(priority)

def printFormat(s):
    print(s.center(70))

def viewList():
    printFormat("-----Current List-----")
    for i in range(0, len(todo)):
        printItem(i+1, todo[i][0], f"Priority: {todo[i][1]}")

def addToList():
    editing = True
    printFormat("Type the new todo item:")
    while editing:
        item = input("Item: ")
        priority = int(input("Priority: "))
        todo.append([item, priority])
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
