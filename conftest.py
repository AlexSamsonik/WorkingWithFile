import pytest
import logging

log = logging.getLogger()


@pytest.fixture(scope="function")
def log_test_name(request):
    """ Log when test started and finished."""

    log.info(f"{request.node.name} started.")

    def log_test_finish():
        log.info(f"{request.node.name} finished.")
    request.addfinalizer(log_test_finish)
    return request.fixturename
