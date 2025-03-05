# First_repo

#The menu section that shows the first tasks you can perform
def menu():
    print("Choose by number ")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Mark tasks as completed")
    print("4. Remove tasks")
    print("5. Update a task")
    print("6. Sort tasks")

#first menu you can add tasks and the priority of that task
def add_task(tasks):
    add_task_name= input("enter the task name: ")
    priority = input("Set the priority of the task (High,Meadium,Low): ")
    task={"name":add_task_name, "priority":priority, "status":"incomplete"} 
    tasks.append(task)   

#you can see the tasks stored
def View_tasks(tasks):
    if not tasks:
        print("Tasks are not available")
    else:
        for i, task in enumerate(tasks, start=1):
             print(f"{i}. {task['name']} - priority: {task['priority']} - Status: {task['status']}")

#you can update the status of the task incomplete to complete
def mark_complete(tasks):
    select_task = int(input("Enter the task number to chnage the status to complete: "))
    if select_task <= len(tasks):
        stat = str(input("Chnage the status incomplete or complete: "))
        tasks [select_task -1] ["status"] = stat
        print("task staus updated succesfully to completed")

    else:
        print("Invalid task number")    




tasks=[]
while True:
    menu()
    choice = input("Enter the number to perform speciific task: ")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        View_tasks(tasks)
    elif choice == "3":
        mark_complete(tasks)    
    elif choice == "7":  # Exit option
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a valid number.")        



   

  