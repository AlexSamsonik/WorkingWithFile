import pytest
import logging
import os
from common.constants import (TEMP_DIRECTORY, FILE_NAME, FILE_NAME_CONTEXT, FILE_NOBODY_OWNER)
from common.constants import (UID_NOBODY, GID_NOBODY)
from file_system_operation.ext4_operation import (add_context, change_owner)

log = logging.getLogger()


@pytest.fixture(scope="function", autouse=True)
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
def change_owner_to_nobody():
    """Change owner to nobody."""
    file_path = os.path.join(TEMP_DIRECTORY, FILE_NOBODY_OWNER)
    change_owner(file_path, UID_NOBODY, GID_NOBODY)
