from handlers import dir_tree_slyled, dir_colored, file_colored

def print_dir(directory, i = 0):
    i += 1
    for path in directory.iterdir():
        relative_path = path.relative_to(directory)
        if path.is_file():
            print(dir_tree_slyled(i) + file_colored(relative_path))
        elif path.is_dir():
            print(dir_tree_slyled(i) + dir_colored(relative_path))
            print_dir(path, i)
