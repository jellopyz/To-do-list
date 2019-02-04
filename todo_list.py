"""
To do list program
Developer: Thanakorn Amnajsatit
Description: It's command line program to show Todo Lists 
and be able to remove complete task from Todo Lists
"""

import json

# Main Function
def main():

    # Read File
    try:
        with open("task_list.json", "r") as f:
            jsonString = f.read()
        if len(jsonString) == 0: # No task in list or json file
            task_list = {'TodoLists':[]}
        else:
            task_list  = json.loads(jsonString)
            showTodoList(task_list['TodoLists'])
    except:
        task_list = {'TodoLists':[]}

    # Start entering task
    showDescription()
    while(True):
        task = input("Your task: ")
        if task == "":# Stop entering the tasks
            showTodoList(task_list['TodoLists'])
            print("###Type \"task's number or task's name\" to remove task from list.")
            print("###Type nothing and press enter to stop entering tasks/removing tasks.")
            print("**Insert completed task")
            while(True):
                completed_task = input("Remove: ")
                if completed_task == "": # stop removing the tasks
                    showTodoList(task_list['TodoLists'])
                    task_list['TodoLists'] = removeCompletedTask(task_list['TodoLists'])
                    break
                if completed_task in task_list['TodoLists']:# check completed task if you type task's name
                    index = task_list['TodoLists'].index(completed_task)
                    task_list['TodoLists'][index] = completed_task + "(Completed)"
                    print("Remove successful!!!")
                elif completed_task.isnumeric() == True and 0 < int(completed_task) < len(task_list['TodoLists']): # check completed task if you type task's number
                    index = int(completed_task)-1
                    task_list['TodoLists'][index] = task_list['TodoLists'][index] + "(Completed)"
                    print("Remove successful!!!")
                else:
                    print("*You already remove or input was wrong.") # when you type wrong
                    print("*Please type task's name or task's number correctly.") # when you type wrong
                
            break
        else:
            task_list['TodoLists'].append(task) # add task to task_list

    # Write File
    with open("task_list.json", "w") as f:
        f.write(json.dumps(task_list))

def removeCompletedTask(task_list):
    # Remove every task that's completed in task_list
    removed_list = []
    if len(task_list) == 0:
        return removed_list
    else:
        for i in task_list:
            if '(Completed)' in i:
                pass
            else:
                removed_list.append(i)
        return removed_list

def showTodoList(todo_list):
    # Show all the tasks
    print("***Todo List***")
    if len(todo_list) == 0:
        print("No task in list")
    else:
        for i in range(0, len(todo_list)):
            print(str(i+1)+"."+todo_list[i])

def showDescription():
    print("###Please enter a chore or task you have to do.")
    print("###Type nothing and press enter to stop entering tasks/removing tasks.")

main()
