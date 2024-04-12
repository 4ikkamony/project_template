import pandas as pd


def output_console(text):
    """Function to output text to console

    Args:
        text (str): text to output

    """
    print(text)


def write_file_default(text, file_path, mode="w"):
    """Function to write text to file(with default Python tools)

    Args:
        text (str): text to write
        file_path (str): path to file for writing
        mode: "w" to overwrite(by default), "a" to append to existing file

    """
    try:
        with open(file_path, mode) as file:
            try:
                file.write(text+'\n')
            except IOError as e:
                print(f"Error writing to {file_path}: {e}")
    except FileNotFoundError as e:
        print(f"Error opening {file_path}: {e}")


def write_file_pandas(text, file_path, mode="w"):
    """Function to write text to file(with Pandas)

    Args:
        text (str): text to write
        file_path (str): path to file for writing
        mode: "w" to overwrite(by default), "a" to append to existing file

    """
    try:
        data = [text]
        df = pd.DataFrame(data)
        df.to_csv(file_path, mode, header=False, index=False)
    except FileNotFoundError as e:
        print(f"Error writing to {file_path}: {e}")
