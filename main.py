from app.io import input, output


def main():
    file_path_default = "D:\\wrkspc\\project_template\\data\\default_example_output.txt"
    file_path_pandas = "D:\\wrkspc\\project_template\\data\\pandas_example_output.txt"

    # user input
    text = input.input_console("Write smth: ")

    # output from console
    output.output_console(f'user input = ' + text)

    # write to file default
    output.write_file_default(text, file_path_default)

    # write to file pandas
    output.write_file_pandas(text, file_path_pandas)

    #read file default
    output.output_console('Output file(default):\n'+input.read_file_default(file_path_default))

    #read file pandas
    output.output_console('Output file(pandas):\n'+input.read_file_pandas(file_path_pandas))

if __name__ == "__main__":
    main()
