import pytest
from logger import Logger


@pytest.fixture
def logger():
    return Logger()


def test_logger_multiple_messages(logger):
    assert logger.printer(1, 'hello') == True
    assert logger.printer(2, 'bye') == True
    assert logger.printer(8, 'bye') == False
    assert logger.printer(12, 'hello') == True
    assert logger.printer(13, 'bye') == True


def test_logger_edge_case_just_under_10_seconds(logger):
    logger.printer(1, 'hello')
    assert logger.printer(10, 'hello') == False


def test_logger_edge_case_exactly_10_seconds(logger):
    logger.printer(1, 'hello')
    assert logger.printer(11, 'hello') == True
