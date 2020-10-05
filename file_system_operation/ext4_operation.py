import logging
import os
import shutil
from pathlib import Path


log = logging.getLogger()


def create_directory(dir_path):
    """Create a new directory at this given path.

    :param dir_path: path to the new directory.
    :return: path to the new directory.
    """

    try:
        log.info(f"Try to create the directory '{dir_path}'.")
        Path(dir_path).mkdir(exist_ok=True)
    except OSError:
        log.error(f"Creation of the directory '{dir_path}' failed.")
        raise
    else:
        log.info(f"Successfully created thr directory '{dir_path}'.")
        return dir_path


def delete_directory_tree(dir_path):
    """Recursively delete a directory tree.

    :param dir_path: path to a directory tree
    """

    try:
        log.info(f"Try to delete the directory tree '{dir_path}'.")
        shutil.rmtree(dir_path)
    except OSError:
        log.error(f"Deletion of the directory '{dir_path}' failed.")
        raise
    else:
        log.info(f"Successfully deleted the directory three '{dir_path}'.")


def create_file(file_path):
    """Create this file with the given access mode, if it doesn't exist.

    :param file_path: path to the file.
    :return: path to the file.
    """

    try:
        log.info(f"Try to create the file '{file_path}'.")
        Path(file_path).touch(exist_ok=True)
    except OSError:
        log.error(f"Creation of the file '{file_path}' failed.")
        raise
    else:
        log.info(f"Successfully created the file '{file_path}'.")
        return file_path


def create_files(dir_path, files: list):
    """Create files inside specific directory.

    :param dir_path: path to the directory.
    :param files: list with file names
    """

    for file in files:
        create_file(os.path.join(dir_path, file))


def remove_file(file_path):
    """Remove the file.

    :param file_path: path to the file
    """

    try:
        log.info(f"Remove file '{file_path}'.")
        Path(file_path).unlink()
    except (IsADirectoryError, NotADirectoryError, PermissionError):
        log.error(f"Removing file '{file_path}' failed.")
        raise
    except FileNotFoundError:
        log.error(f"No such file or directory: '{file_path}'.")
        raise
    else:
        log.info(f"Successfully removing file '{file_path}'.")


def add_context(file_path, file_context):
    """Adding context to the file.

    :param file_path: path to the file
    :param file_context: context which need to add to the file
    """

    try:
        with open(file_path, "w") as file:
            log.info(f"Try to add the context '{file_context}' to the '{file_path}'")
            file.write(file_context)
    except OSError:
        log.error(f"Addition of the context failed to the '{file_path}'.")
        raise
    else:
        log.info(f"Successfully added the context to the '{file_path}'.")


def change_owner(path: str, uid: int, gid: int):
    """Change the owner and group id of path to the numeric uid and gid.

    :param path: path to the file
    :param uid: new owner id
    :param gid: new group id
    """

    try:
        log.info(f"Try to change the owner and group to the numeric uid={uid} and gid={gid} from '{path}'")
        os.chown(path, uid, gid)
    except OSError as err:
        log.error(f"OS error: {err}")
        raise
    else:
        log.info(f"Successfully changed the owner and group to the numeric uid={uid} and gid={gid} from '{path}'.")
