FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """This function will open the todos.txt
     in read mode and return a list of them
     """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH ):
    """This function will open the todos.txt file
    in write mode and append a list of item into it
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)




if __name__ == "__main__":
    print("hello")
    print(get_todos())