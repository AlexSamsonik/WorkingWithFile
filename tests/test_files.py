""" Test's module for testing file system."""

import os
import shutil
import logging
import pytest
from common.constants import (TEMP_DIRECTORY, LIST_FILE_NAME, FILE_NAME, FILE_NAME_CONTEXT)

log = logging.getLogger()


def setup_module():
    """Create temporally directory."""

    log.info(f"Create the directory '{TEMP_DIRECTORY}'.")
    os.mkdir(TEMP_DIRECTORY)  # How high is the probability that this will not work out ?
    # TODO: It will work only if everything is OK.
    #  Need to decide which strategy to choose when something went wrong.

    # TODO: Next strategy:
    #  1. os.makedirs(TEMP_DIRECTORY, exist_ok=True)
    #  2. try/except
    #  3. if os.path.exists(TEMP_DIRECTORY): [...] ;


def teardown_module():
    """Recursively delete a directory tree."""

    log.info(f"Delete the directory tree '{TEMP_DIRECTORY}'.")
    shutil.rmtree(TEMP_DIRECTORY)  # How high is the probability that this will not work out ?
    # TODO: It will work only if everything is OK.
    #  Need to decide which strategy to choose when something went wrong.

    # TODO: Next strategy:
    #  1. try/except/finally
    #  2. if not os.path.exists(TEMP_DIRECTORY): [...] ;


@pytest.mark.parametrize("file_name", LIST_FILE_NAME)
def test_create_file(log_test_name, file_name):
    """ Test file creation.

    Steps:
    1. Create temporally directory if it does not exist.
    2. Create file inside temporally directory.
    3. Verifies that file has been created successfully inside temporally directory.
    4. Remove file from the temporally directory.

    :param log_test_name: pytest fixture which log when test starting and finishing.
    """

    # Step 2
    log.info(f"Creating file by name '{file_name}' inside the temporally directory '{TEMP_DIRECTORY}'.")
    open(os.path.join(TEMP_DIRECTORY, file_name), "x").close()

    # Step 3
    log.info(f"Verifies that file '{file_name}' has been created successfully "
             f"inside the temporally directory '{TEMP_DIRECTORY}'.")
    assert os.path.exists(os.path.join(TEMP_DIRECTORY, file_name)), \
        f"File '{file_name}' has not created successfully inside the temporally directory '{TEMP_DIRECTORY}'."


@pytest.mark.usefixtures("add_context_to_file")
def test_add_content_to_file(log_test_name):
    """ Test file context.

    Steps:
    1. Create temporally directory if it does not exist.
    2. Create file inside temporally directory.
    3. Add context to the file created.
    4. Verifies that file context equals FILE_NAME_CONTEXT.
    5. Remove file from the temporally directory.

    :param log_test_name: pytest fixture which log when test starting and finishing.
    :return:
    """
    with open(os.path.join(TEMP_DIRECTORY, FILE_NAME)) as file:
        context = file.read()
    log.info(f"Verifies that file context equals '{FILE_NAME_CONTEXT}'.")
    assert context == FILE_NAME_CONTEXT, "File context does not match"
