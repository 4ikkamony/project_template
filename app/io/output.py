import pandas as pd


def output_console(text):
    """Function to output text to console

    Args:
        text (str): text to output

    """
    print(text)


def write_file_default(text, file_path):
    """Function to write text to file(with default Python tools)

    Args:
        text (str): text to write
        file_path (str): path to file for writing

    """
    try:
        with open(file_path, 'a') as file:
            try:
                file.write(text+'\n')
            except IOError as e:
                print(f"Error writing to {file_path}: {e}")
    except FileNotFoundError as e:
        print(f"Error opening {file_path}: {e}")


def write_file_pandas(text, file_path):
    """Function to write text to file(with Pandas)

    Args:
        text (str): text to write
        file_path (str): path to file for writing

    """
    try:
        data = [text]
        df = pd.DataFrame(data)
        df.to_csv(file_path, mode='a', header=False, index=False)
    except FileNotFoundError as e:
        print(f"Error writing to {file_path}: {e}")
