import pytest
from src.decorators.log import log


@pytest.fixture
def log_file(tmp_path):
    return tmp_path / "test_log.txt"

def test_log_to_file(log_file):
    @log(filename=str(log_file))
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open(log_file, "r") as f:
        content = f.read().strip()
        assert content == "my_function ok"

def test_log_to_console(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out.strip() == "my_function ok"

def test_log_error_to_file(log_file):
    @log(filename=str(log_file))
    def my_function(x, y):
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        my_function(1, 2)
    with open(log_file, "r") as f:
        content = f.read().strip()
        assert content == "my_function error: ValueError. Inputs: (1, 2), {}"

def test_log_error_to_console(capsys):
    @log()
    def my_function(x, y):
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.err.strip() == "my_function error: ValueError. Inputs: (1, 2), {}"
