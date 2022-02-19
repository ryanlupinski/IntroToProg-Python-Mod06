# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# RLupinski,02.16.2022
#    - Modified code to complete assignment 6
#    - Refactor all instances of ToDoFile.txt to ToDoList.txt
# RLupinski,02.17.2022
#    - add comments and completed options 3-4
# RLupinski, 02.19.2022
#    - add more comments
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoList.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of the processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        try:  # check if ToDoList.txt already exists
            objFile = open(file_name, "r")  # open ToDoList.txt in read mode
            for line in objFile:  # for each line in the file
                task, priority = line.split(",")  # split elements in the file line by a comma, save to variables
                row = {"Task": task.strip(), "Priority": priority.strip()}  # create dicRow from previous variables
                list_of_rows.append(row)  # append each row to the lstTable
            objFile.close()  # close the file
        except:  # if ToDoList.txt doesn't exist create a new txt file and populate with a header
            objFile = open(file_name, 'w')  # open the file
            objFile.write("Task" + ',' + "Priority" + '\n')  # write task,priority header to file
            objFile.close()  # close the file
            print("ToDoList.txt not found. Creating a new ToDoList.txt file")  # print to console
        return list_of_rows, 'Success'  # return the lstTable

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ adds a task and priority to the list

        :param task: string, task to be added
        :param priority: string, priority level
        :param list_of_rows: list of dictionary rows,task list
        :return: updated task list
        """
        dicRow = {'Task': task, 'Priority': priority}  # create a new dicRow with new task
        list_of_rows.append(dicRow)  # append the table w/ new dicRow
        return list_of_rows, 'Success'  # return the updated list

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ removes a task from the list

        :param task: string, task to be removed
        :param list_of_rows: list of dictionary rows,task list
        :return: updated task list
        """
        for row in range(len(list_of_rows)):  # look in each row of the lstTable
            if list_of_rows[row]['Task'] == task:  # check if task key equals the task to be removed
                del list_of_rows[row]  # delete the row
                break  # break the if loop
        return list_of_rows, 'Success'  # return the updated list

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ writes data to the file

        :param file_name: file name to save data
        :param list_of_rows: current task list in memory
        :return: returns the task list
        """
        objFile = open(file_name, 'w')  # open connection to file in write mode
        for row in list_of_rows:    # for each row lstTable
            strTask = row['Task'] # pull task value from lstTable
            strPriority = row['Priority']   # pull priority value from lstTable
            objFile.write(str(strTask) + "," + str(strPriority) + "\n")  # write task/priority values to file
        objFile.close()  # close the file
        return list_of_rows, 'Success'  # return the updated list


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoList.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        strTask = str(input("Add task: "))  # prompt user to add a task
        strPriority = str(input("Add priority[1(high) - 5(low): "))  # prompt user to define priority
        Processor.add_data_to_list(strTask, strPriority, lstTable)  # pass task, priority, and task table args to add data function
        IO.input_press_to_continue(strStatus)  # hold for user
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        strTask = str(input("Remove a task: "))  # prompt user to add a task
        Processor.remove_data_from_list(strTask, lstTable) # pass task and task table as args to remove data function
        IO.input_press_to_continue(strStatus)  # hold for user
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")  # prompt user before saving
        if strChoice.lower() == "y":    # if user types y
            Processor.write_data_to_file(strFileName, lstTable) # pass file name and task table to write to file function
            IO.input_press_to_continue(strStatus)  # hold for user
        else:
            IO.input_press_to_continue("Save Cancelled!")   # save to file aborted
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':    # if user types y
            Processor.read_data_from_file(strFileName, lstTable)  # calls read file data function again
            IO.input_press_to_continue(strStatus)  # hold for user
        else:
            IO.input_press_to_continue("File Reload Cancelled!")    # reload data to memory aborted
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
