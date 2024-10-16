Task Manager CLI Application

Create a new directory and file for Our Project.

Implementing Task Management Functions :

Adding Tasks:
    --> Creating a basic Command Line Interface that asks the user for his task ID, title and  completed tasks.

Viewing Tasks:
    --> Viewing function created allows the user to view their tasks, through looping each task in the list.

Deleting Tasks:
    --> Sometimes, users may want to remove tasks that are no longer needed.
    --> We can enable this by allowing the user to delete a task based on index 

Updating Tasks:
    --> We first display all the tasks so the user can decide which one they want yo update.
    --> The user is asked to provide the index number of the task, and then they can either update the id, title and completed.

Looping: 

Create an interactive loop that presents options to the user. This loop will allow the user to choose between adding, viewing, deleting, updating tasks are exiting the program.

File Handling:
    --> Implement functions to save and load tasks to/from a file using JSON:
        -> Save Tasks: Save the list of tasks to a file named tasks.json.
        -> Load Tasks: Load tasks from tasks.json when the start application.
