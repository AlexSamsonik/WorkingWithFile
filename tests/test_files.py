""" Test's module for testing file system."""

import os
import shutil
import logging
from common.constants import TEMP_DIRECTORY
from common.constants import FILE_NAME

log = logging.getLogger()


def setup_module():
    """Create temporally directory."""

    try:
        os.mkdir(TEMP_DIRECTORY)
    except OSError:
        log.info(f"Creation of the directory '{TEMP_DIRECTORY}' failed.")
    else:
        log.info(f"Successfully created the directory '{TEMP_DIRECTORY}'.")


def teardown_module():
    """Recursively delete a directory tree."""

    try:
        shutil.rmtree(TEMP_DIRECTORY)
    except OSError:
        log.info(f"Deletion of the directory '{TEMP_DIRECTORY} failed.")
    else:
        log.info(f"Successfully deleted the directory '{TEMP_DIRECTORY}'.")


def test_create_files():
    """ Test file creation.

    Steps:
    1. Create temporally directory if not exist.
    2. Create file inside temporally directory.
    3. Verifies that file has been created successfully inside temporally directory.
    4. Remove temporally directory.

    """

    # Step 2
    log.info(f"Creating file by name '{FILE_NAME}'")
    open(os.path.join(TEMP_DIRECTORY, FILE_NAME), "x").close()

    # Step 3
    log.info(f"Verifies that file '{os.path.join(TEMP_DIRECTORY, FILE_NAME)}' has been created successfully.")
    assert os.path.exists(os.path.join(TEMP_DIRECTORY, FILE_NAME)), f"File '{FILE_NAME}' has not created successfully."
