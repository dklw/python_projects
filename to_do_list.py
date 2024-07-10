print("welcome to your TO DO LIST".center(100))

todo_list = []

while True:
    
    print("Menu options\n")
    print("1. add task")
    print("2. remove task")
    print("3. dsiplay task")
    print("4. exit the program")
    
    choice = int(input("enter your choice : "))
    
    if choice == 1:
        task = input("enter your task : \n")
        todo_list.append(task)
        print(f"{task} has been added to your to do list")
        
    elif choice == 2:
        index = int(input("enter the index of the task to be removed : "))
        if 1 <= index <= len(todo_list):
            removed_task = todo_list.pop(index - 1)
            print(f"Task '{removed_task}' removed from the to-do list.")
            
    elif choice == 3:
        print("To Do List : \n")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
            
    elif choice == 4:
        print("exiting the program ! ".center(100))
        break
    
    else:
        print("invalid choice ! ".center(100))
        
          