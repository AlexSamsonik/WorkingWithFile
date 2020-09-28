import pytest
import logging
import os
from common.constants import (TEMP_DIRECTORY, FILE_NAME, FILE_NAME_CONTEXT)

log = logging.getLogger()


@pytest.fixture(scope="function")
def log_test_name(request):
    """ Log when test started and finished."""

    log.info(f"{request.node.name} started.")

    def log_test_finish():
        log.info(f"{request.node.name} finished.")

    request.addfinalizer(log_test_finish)
    return request.fixturename


@pytest.fixture(scope="function")
def add_context_to_file():
    """Adding context to the file."""
    file_path = os.path.join(TEMP_DIRECTORY, FILE_NAME)
    try:
        with open(file_path, "w") as file:
            log.info(f"Adding context to the '{file_path}'")
            file.write(FILE_NAME_CONTEXT)
    except (IsADirectoryError, NotADirectoryError, PermissionError):
        log.error(f"Adding context failed to the '{file_path}'.")
        raise
    except FileNotFoundError:
        log.error(f"No such file or directory: '{file_path}'.")
        raise
    else:
        log.info(f"Successfully adding context to the '{file_path}'.")
