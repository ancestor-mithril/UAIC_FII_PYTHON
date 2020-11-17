from typing import List
import os
from utilities.custom_error import CustomError
from utilities.utils import color_print


def get_duplicate_files(path_to_directory: str, recursive_walk: bool = True) -> List[List[str]]:
    """
    the target directory is recursively walked

    :param recursive_walk: True, if user wants to check all files in directory, False, only for files in root of
                            directory
    :param path_to_directory: path to a valid directory
    :return: List[each duplicate group = List[paths_to_duplicated_files] ]
                All files inside target directory which are duplicates grouped by duplicated text
    """
    if not os.path.isdir(path_to_directory):
        raise CustomError("{path} is not a valid path to a directory".format(path=path_to_directory))
    if recursive_walk:
        all_files = []
        for root, directories, files in os.walk(path_to_directory):
            all_files += [
                os.path.abspath(os.path.join(root, file_name)) for file_name in files if
                os.path.isfile(os.path.join(root, file_name)) and os.access(os.path.join(root, file_name), os.R_OK)
            ]
    else:
        all_files = [f for f in os.listdir() if os.path.isfile(f)]

    return return_duplicates(all_files)


def return_duplicates(all_files: List[str]) -> List[List[str]]:
    """
    for each unique pair of files, if they are equal and were not previously in any group of duplicates,
    a new group is created and appended to all groups

    :param all_files: list of correct (and assumed to be validated) file paths to all files
    :return: list of duplicates list
    """
    duplicate_groups = []
    selected_files = []
    for i in range(len(all_files) - 1):
        duplicate_group = [all_files[i]]
        if all_files[i] in selected_files:
            continue
        for j in range(i + 1, len(all_files)):
            if are_equal(all_files[i], all_files[j]):
                duplicate_group.append(all_files[j])
                selected_files.append(all_files[j])

        if len(duplicate_group) > 1:
            duplicate_groups.append(duplicate_group)

    return duplicate_groups


def are_equal(file_1: str, file_2: str, chunk_size: int = 1024) -> bool:
    """
    reads chunks of blocks for both files and checks them to be equal

    :param chunk_size: size of chunk to be read
    :param file_1: path to file
    :param file_2: path to file
    :return: True, if files are equal, False otherwise
    """
    assert os.path.isfile(file_1) and os.path.isfile(file_2), "paths are not file"
    try:
        with open(file_1, 'rb') as fd_1:
            with open(file_2, 'rb') as fd_2:
                while True:
                    data_1 = fd_1.read(chunk_size)
                    data_2 = fd_2.read(chunk_size)
                    if data_1 != data_2:
                        return False
                    if not data_1:
                        break
        return True
    except Exception as e:
        raise CustomError(e)


def print_files(files: List[str]):
    """

    :param files: list of files to be printed
    :return: nothing
    """
    for file_index in range(len(files)):
        print(f"File {file_index + 1}\t-> {files[file_index]}")


def delete_file(file_path: str):
    """

    :param file_path: file to be deleted
    :return: nothing
    """
    assert os.path.exists(file_path), "File does not exist"
    os.remove(file_path)


def handle_file_delete(duplicates: List[str], file_index: int) -> List[str]:
    """
    attempting delete of file. user is asked for confirmation. duplicates list if necessary and returned

    :param duplicates: list of duplicated files
    :param file_index: index of file to be deleted
    :return: list of files after delete attempt
    """
    assert 0 <= file_index < len(duplicates), "Index out of range"
    assert len(duplicates) > 0, "Duplicate list is already empty"
    color_print(f"Selected file: {duplicates[file_index]}")
    color_print("Delete?[y/n]")
    user_input = input()
    if user_input == "y" or user_input == "yes":
        delete_file(duplicates.pop(file_index))
    elif user_input != "n" and user_input != "no":
        color_print(f"Unknown input: {user_input}", color='red')
    return duplicates


def handle_user_input(duplicates: List[str]):
    """

    :param duplicates: group of duplicates
    :return:
    """
    help_string = "type \"help\" for help\n" + "type \"skip\" to skip deleting duplicate files\n" + \
                  "type \"show\" to display again duplicated files\n" + "type a file index to delete selected file"
    color_print(f"Choose all files to be discarded, type \"help\" for help, or type \"skip\" to skip")
    while True:
        user_input = input()
        if user_input == "skip":
            return
        elif user_input == "help":
            color_print(help_string, color="green")
        elif user_input == "show":
            print_files(duplicates)
        else:
            try:
                file_index = int(user_input)
            except ValueError:
                color_print("Invalid input. Press \"help\" for more information.", color='red')
                continue
            except Exception as e:
                raise CustomError(e)
            if 1 <= file_index <= len(duplicates):
                duplicates = handle_file_delete(duplicates, file_index - 1)
                if len(duplicates) > 0:
                    color_print(f"Duplicated files remaining: {len(duplicates)}. Delete more files or skip.")
                else:
                    color_print(f"All files deleted.\n")
                    return
            else:
                color_print(f"Invalid file index: {file_index}", color='red')
                continue


def process_duplicates(duplicates: List[List[str]]):
    """
    for each duplicate group, user is prompted to delete or skip deleting duplicated files

    :param duplicates: list of groups of duplicates
    :return: nothing
    """
    color_print(f"Target folder has {len(duplicates)} duplicate groups.")
    if len(duplicates) > 0:
        color_print("User may now proceed to remove.")
    for d in range(len(duplicates)):
        color_print(f"Group {d + 1}/{len(duplicates)}:")
        print_files(duplicates[d])
        handle_user_input(duplicates[d])


