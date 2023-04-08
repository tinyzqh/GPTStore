import os


def read_text_file(file_path: str) -> str:
    """Read the contents of a text file.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        str: The contents of the file as a string.
    """
    with open(file_path, "r") as file:
        file_contents = file.read()
    return file_contents


def read_text_lines_file(file_path: str) -> str:
    """Read the contents of a text file.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        str: The contents of the file as a string.
    """
    with open(file_path, "r") as file:
        file_contents = file.readlines()
    return file_contents


def write_text_lines_file(file_path: str, text_lines: list) -> None:
    """Write the contents of a text file.

    Args:
        file_path (str): The path to the file to write.
        text_lines (list): The contents of the file as a list.

    Returns:
        None
    """
    # 如果.txt文件不存在，就创建一个

    with open(file_path, "a") as file:
        for text in text_lines:
            file.write(",".join(text))
            file.write("\n")
        # file.writelines(text_lines)


if __name__ == "__main__":
    # Set the parent directory to the current working directory
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))

    # Construct the file path relative to the parent directory
    file_path = os.path.join(parent_dir, "src", "corpus", "diaochan", "system.txt")

    # Print the contents of the file
    print(read_text_file(file_path))
