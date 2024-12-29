def read_lines_from_file(file_path):
    """
    Reads all lines from a file and returns them as a list.

    :param file_path: Path to the file
    :return: A list of lines from the file
    """
    try:
        with open(file_path, 'r') as file:  # Open the file in read mode
            lines = file.readlines()       # Read all lines
        return lines
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    
def read_all_text_from_file(file_path):
    """
    Reads all text from a file and returns them as a text.

    :param file_path: Path to the file
    :return: All text from the file
    """
    try:
        with open(file_path, 'r') as file:  # Open the file in read mode
            text = file.read()       # Read all lines
        return text
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
