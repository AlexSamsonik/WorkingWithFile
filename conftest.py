import pytest
import logging
import os
from common.constants import (TEMP_DIRECTORY, FILE_NAME, FILE_NAME_CONTEXT, FILE_OWNER)
from file_system_operation.ext4_operation import (create_file, remove_file, add_context)

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
    add_context(os.path.join(TEMP_DIRECTORY, FILE_NAME), FILE_NAME_CONTEXT)


@pytest.fixture(scope="function")
def create_and_delete_file():
    """Create and remove file."""

    file_path = os.path.join(TEMP_DIRECTORY, FILE_OWNER)
    yield create_file(file_path)
    remove_file(file_path)
