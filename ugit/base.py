import os
from . import data


def write_tree(directory="."):
    with os.scandir(directory) as it:
        for entry in it:
            full = f"{directory}/{entry.name}"
            if is_ignored(full):
                continue

            if entry.is_file(follow_symlinks=False):
                with open(full, "rb") as f:
                    print(data.hash_object(f.read(), full))
            elif entry.is_dir(follow_symlinks=False):
                write_tree(full)
    # TODO actually create the tree object


def is_ignored(path):
    ignore_dirs = ['.ugit', 'venv', '.git', 'ugit.egg-info']
    return any(ignore_dir in path.split("/") for ignore_dir in ignore_dirs)
