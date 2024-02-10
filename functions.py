# Define the path to the file that will store the to-do items
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items.

    Args:
        filepath (str): The path to the file that stores the to-do items. Defaults to FILEPATH.

    Returns:
        list: A list of to-do items.
    """
    # Open the file in read mode
    with open(filepath, "r") as file_local:
        # Read all lines from the file
        todos_local = file_local.readlines()
    # Return the list of to-do items
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file.

    Args:
        todos_arg (list): The list of to-do items to write to the file.
        filepath (str): The path to the file that stores the to-do items. Defaults to FILEPATH.
    """
    # Open the file in write mode
    with open(filepath, "w") as file:
        # Write the list of to-do items to the file
        file.writelines(todos_arg)


if __name__ == "__main__":
    # Print a greeting message
    print("Hello")
    # Print the list of to-do items
    print(get_todos())
