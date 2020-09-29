""" Test's module for testing file system."""

import os
import logging
import pytest
from common.constants import (TEMP_DIRECTORY, LIST_FILE_NAME, FILE_NAME, FILE_NAME_CONTEXT)
from common.constants import (UID, GID)
from file_system_operation.ext4_operation import (create_directory, delete_directory, create_files)

log = logging.getLogger()


@pytest.fixture(scope="session")
def setup_module():
    """Create temporally directory with files."""
    create_directory(TEMP_DIRECTORY)
    create_files(TEMP_DIRECTORY, LIST_FILE_NAME)


@pytest.fixture(scope="session")
def teardown_module():
    """Recursively delete a directory tree."""
    delete_directory(TEMP_DIRECTORY)


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
    """

    # Step 4
    with open(os.path.join(TEMP_DIRECTORY, FILE_NAME)) as file:  # TODO: try/except ?
        actual_context = file.read()
    log.info(f"Verifies that file context equals '{FILE_NAME_CONTEXT}'.")
    assert actual_context == FILE_NAME_CONTEXT, f"File context does not match " \
                                                f"Actual context: '{actual_context}' " \
                                                f"Expected context: '{FILE_NAME_CONTEXT}'"


def test_check_uid(log_test_name, create_and_delete_file):
    """Test check file UID.

    Steps:
    1. Create temporally directory if it does not exist.
    2. Create file inside temporally directory.
    3. Verifies that uid equals UID
    4. Remove file from the temporally directory.
    """

    # Step 4
    actual_uid = os.stat(create_and_delete_file).st_uid
    log.info(f"Verifies that uid equals UID.")
    assert actual_uid == UID, f"File uid does not match. Actual UID: '{actual_uid}' Expected UID: '{UID}'"


def test_check_gid(log_test_name, create_and_delete_file):
    """Test check file GID.

    Steps:
    1. Create temporally directory if it does not exist.
    2. Create file inside temporally directory.
    3. Verifies that uid equals GID
    4. Remove file from the temporally directory.
    """

    # Step 4
    actual_gid = os.stat(create_and_delete_file).st_gid
    log.info(f"Verifies that uid equals GID.")
    assert actual_gid == GID, f"File gid does not match. Actual GID: '{actual_gid}' Expected GID: '{GID}'"
