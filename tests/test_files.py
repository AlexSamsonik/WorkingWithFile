""" Test's module for testing file system."""

import os
import logging
import pytest
from common.constants import (TEMP_DIRECTORY, LIST_FILE_NAME, FILE_NAME, FILE_NAME_CONTEXT, FILE_OWNER,
                              FILE_NOBODY_OWNER, FILE_READ_ONLY)
from common.constants import (UID, GID, UID_NOBODY, GID_NOBODY)
from common.constants import (MODE_400, MODE_644)
from common.constants import PERMISSION_MSG
from file_system_operation.ext4_operation import (create_directory, delete_directory_tree, create_files, change_owner)

log = logging.getLogger()


def setup_module():
    """Create temporally directory with files."""
    create_directory(TEMP_DIRECTORY)
    create_files(TEMP_DIRECTORY, LIST_FILE_NAME)


def teardown_module():
    """Recursively delete a directory tree."""
    delete_directory_tree(TEMP_DIRECTORY)


@pytest.mark.parametrize("file_name", LIST_FILE_NAME)
def test_file_existing(file_name):
    """ Test file existing.

    Steps:
    1. Create temporally directory if it does not exist.
    2. Create file inside temporally directory.
    3. Verifies that file exists inside temporally directory.
    4. Remove file from the temporally directory.
    """

    # Step 3
    log.info(f"Verifies that file '{file_name}' exists inside the temporally directory '{TEMP_DIRECTORY}'.")
    assert os.path.exists(os.path.join(TEMP_DIRECTORY, file_name)), \
        f"File '{file_name}' does not exist inside the temporally directory '{TEMP_DIRECTORY}'."


@pytest.mark.parametrize("file_name", LIST_FILE_NAME)
def test_file_mode(file_name):
    """ Test file mode.

    Steps:
    1. Create temporally directory if it does not exist.
    2. Create file inside temporally directory.
    3. Verifies that file mode equals 0o644 (-rw-r--r--).
    4. Remove file from the temporally directory.
    """

    # Step 3
    file_path = os.path.join(TEMP_DIRECTORY, file_name)
    log.info(f"Verifies that file mode equals 0o644 from file '{file_path}'.")
    actual_mode = oct(os.stat(file_path).st_mode)[-3:]
    assert actual_mode == MODE_644, f"File '{file_path}' does not have mode 0o644. " \
                                    f"Actual: '{actual_mode}' Expected: '{MODE_644}'."


@pytest.mark.usefixtures("add_context_to_file")
def test_add_content_to_file():
    """ Test file context.

    Steps:
    1. Create temporally directory if it does not exist.
    2. Create file inside temporally directory.
    3. Add context to the file created.
    4. Verifies that file context equals FILE_NAME_CONTEXT.
    5. Remove file from the temporally directory.
    """

    # Step 4
    with open(os.path.join(TEMP_DIRECTORY, FILE_NAME)) as file:
        actual_context = file.read()
    log.info(f"Verifies that file context equals '{FILE_NAME_CONTEXT}'.")
    assert actual_context == FILE_NAME_CONTEXT, f"File context does not match " \
                                                f"Actual context: '{actual_context}' " \
                                                f"Expected context: '{FILE_NAME_CONTEXT}'"


def test_check_uid():
    """Test check file UID.

    Steps:
    1. Create temporally directory if it does not exist.
    2. Create file inside temporally directory.
    3. Verifies that uid equals UID
    4. Remove file from the temporally directory.
    """

    # Step 3
    file_path = os.path.join(TEMP_DIRECTORY, FILE_OWNER)
    actual_uid = os.stat(file_path).st_uid
    log.info(f"Verifies that uid equals {actual_uid}.")
    assert actual_uid == UID, f"File uid does not match. Actual UID: '{actual_uid}' Expected UID: '{UID}'"


def test_check_gid():
    """Test check file GID.

    Steps:
    1. Create temporally directory if it does not exist.
    2. Create file inside temporally directory.
    3. Verifies that uid equals GID
    4. Remove file from the temporally directory.
    """

    # Step 3
    file_path = os.path.join(TEMP_DIRECTORY, FILE_OWNER)
    actual_gid = os.stat(file_path).st_gid
    log.info(f"Verifies that uid equals {actual_gid}.")
    assert actual_gid == GID, f"File gid does not match. Actual GID: '{actual_gid}' Expected GID: '{GID}'"


@pytest.mark.xfail()
def test_change_uid(change_owner_to_nobody):
    """Test change file UID.

    Steps:
    1. Create temporally directory if it does not exist.
    2. Create file inside temporally directory.
    3. Change uid to nobody.
    3. Verifies that uid equals 65534.
    4. Remove file from the temporally directory.
    """

    # Step 4
    actual_uid = os.stat(change_owner_to_nobody).st_uid
    log.info(f"Verifies that uid equals UID.")
    assert actual_uid == UID_NOBODY, f"File uid does not match. Actual UID: '{actual_uid}' Expected UID: '{UID}'"


def test_catch_permission_error():
    """Test catch permission error.

    Steps:
    1. Create temporally directory if it does not exist.
    2. Create file inside temporally directory.
    3. Try to change uid to nobody.
    4. Verifies that PermissionError Exception was received.
    5. Remove file from the temporally directory.
    """

    # Step 3
    with pytest.raises(PermissionError) as permission:
        file_path = os.path.join(TEMP_DIRECTORY, FILE_NOBODY_OWNER)
        change_owner(file_path, UID_NOBODY, GID_NOBODY)

    # Step 4
    permission_msg = permission.value.args[1]
    log.info(f"Verifies that catch PermissionError Exception.")
    assert permission_msg == PERMISSION_MSG, f"PermissionError does not catch. Actual message: '{permission_msg}' " \
                                             f"Expected message: '{PERMISSION_MSG}'."


def test_permission_read_only_by_owner(disable_write_permission):
    """Test change permission to read only by owner.

    Steps:
    1. Create temporally directory if it does not exist.
    2. Create file inside temporally directory.
    3. Change permission to read only by owner.
    4. Verifies that file mode equals 0o400 (-r--------).
    5. Remove file from the temporally directory.
    """

    # Step 4
    file_path = disable_write_permission
    log.info(f"Verifies that file mode equals 0o400 from file '{file_path}'.")
    actual_mode = oct(os.stat(file_path).st_mode)[-3:]
    assert actual_mode == MODE_400, f"File '{file_path}' does not have mode 0o400. " \
                                    f"Actual: '{actual_mode}' Expected: '{MODE_400}'."
