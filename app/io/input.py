import pandas as pd


def input_console(prompt):
    """Function input to text from console

    Args:
        prompt (str): prompt to display before taking input

    Returns:
        str: text from console

    """
    text = input(prompt)
    return text


def read_file_default(file_path):
    """Function to read text from a file(with default Python tools)

    Args:
        file_path (str): path to file for reading

    Returns:
        str: text from file

    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return ''.join(lines).strip()
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None


def read_file_pandas(file_path):
    """Function to read text from a file(with Pandas)

    Args:
        file_path (str): path to file for reading

    Returns:
        str: text from file

    """
    try:
        data = pd.read_csv(file_path, header=None, names=['text'])
        text = '\n'.join(data['text'])
        return text
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None
