import logging
import os
import shutil

log = logging.getLogger()

# TODO: DRY. A lot of the same try/except!


def create_directory(dir_path):
    """Create a directory.

    :param dir_path: path to a directory
    """

    try:
        log.info(f"Create the directory '{dir_path}'.")
        os.mkdir(dir_path)  # How high is the probability that this will not work out ?

        # TODO: It will work only if everything is OK.
        #  Need to decide which strategy to choose when something went wrong.

        # TODO: Next strategy:
        #  1. os.makedirs(TEMP_DIRECTORY, exist_ok=True)
        #  2. try/except
        #  3. if os.path.exists(TEMP_DIRECTORY): [...] ;
    except (IsADirectoryError, NotADirectoryError, PermissionError):
        log.error(f"Creating directory '{dir_path}' failed.")
        raise
    else:
        log.info(f"Successfully creating directory '{dir_path}'.")


def delete_directory(dir_path):
    """Recursively delete a directory tree.

    :param dir_path: path to a directory
    """

    try:
        log.info(f"Delete the directory tree '{dir_path}'.")
        shutil.rmtree(dir_path)  # How high is the probability that this will not work out ?

        # TODO: It will work only if everything is OK.
        #  Need to decide which strategy to choose when something went wrong.

        # TODO: Next strategy:
        #  1. try/except/finally
        #  2. if not os.path.exists(TEMP_DIRECTORY): [...] ;
    except (IsADirectoryError, NotADirectoryError, PermissionError):
        log.error(f"Deleting directory '{dir_path}' failed.")
        raise
    else:
        log.info(f"Successfully deleting directory '{dir_path}'.")


def create_file(file_path):
    """Create file.

    :param file_path: path to a file.
    :return: path to a file.
    """
    try:
        log.info(f"Creating file '{file_path}'.")
        open(file_path, "x").close()
    except (IsADirectoryError, NotADirectoryError, PermissionError):
        log.error(f"Creating file '{file_path}' failed.")
        raise
    except FileNotFoundError:
        log.error(f"No such file or directory: '{file_path}'.")
        raise
    else:
        log.info(f"Successfully creating file '{file_path}'.")
        return file_path


def create_files(dir_path, files: list):
    """Create files inside specific directory."""

    for file in files:
        log.info(f"Creating file by name '{file}' inside the directory '{dir_path}'.")
        create_file(os.path.join(dir_path, file))


def remove_file(file_path):
    """ Remove file.

    :param file_path: path to a file
    """
    try:
        log.info(f"Remove file '{file_path}'.")
        os.remove(file_path)
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

    :param file_path: path to a file
    :param file_context: context which need to add to the file

    """
    try:
        with open(file_path, "w") as file:
            log.info(f"Adding context to the '{file_path}'")
            file.write(file_context)
    except (IsADirectoryError, NotADirectoryError, PermissionError):
        log.error(f"Adding context failed to the '{file_path}'.")
        raise
    except FileNotFoundError:
        log.error(f"No such file or directory: '{file_path}'.")
        raise
    else:
        log.info(f"Successfully adding context to the '{file_path}'.")
