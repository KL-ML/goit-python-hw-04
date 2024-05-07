from pathlib import Path
import sys
from handlers import print_dir
from handlers import main_dir_colored, exept_colored

def main():
    try:
        directory = Path(sys.argv[1])
        main_dir_colored(directory.name)
        print_dir(directory)
    except FileNotFoundError:
        exept_colored('No such file or directory or path is wrong')
        pass
    except NotADirectoryError:
        exept_colored('Not a directory')
        pass

if __name__ == '__main__':
    main()