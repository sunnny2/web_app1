file = ("todos.txt")

def get_todos(filepath = file):
    """ read a text file and return list of todo items"""

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=file):
    """write to-do item list in text file. """

    with open(filepath,'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())

