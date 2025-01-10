import pytest
from src.decorators.log import log


@pytest.fixture
def log_file(tmp_path):
    return tmp_path / "test_log.txt"

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (5, 7, 12),
    (-1, -2, -3),
    (0, 0, 0)
])
def test_log_to_file(log_file, x, y, expected):
    @log(filename=str(log_file))
    def my_function(x, y):
        return x + y

    result = my_function(x, y)
    assert result == expected
    with open(log_file, "r") as f:
        content = f.read().strip()
        assert content == "my_function ok"

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (5, 7, 12),
    (-1, -2, -3),
    (0, 0, 0)
])
def test_log_to_console(capsys, x, y, expected):
    @log()
    def my_function(x, y):
        return x + y

    result = my_function(x, y)
    assert result == expected
    captured = capsys.readouterr()
    assert 'my_function ok' in captured.out

@pytest.mark.parametrize("x, y", [
    (1, 2),
    (5, 7),
    (-1, -2),
    (0, 0)
])
def test_log_error_to_file(log_file, x, y):
    @log(filename=str(log_file))
    def my_function(x, y):
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        my_function(x, y)
    with open(log_file, "r") as f:
        content = f.read().strip()
        assert content == f"my_function error: ValueError. Inputs: ({x}, {y}), {{}}"

@pytest.mark.parametrize("x, y", [
    (1, 2),
    (5, 7),
    (-1, -2),
    (0, 0)
])
def test_log_error_to_console(capsys, x, y):
    @log()
    def my_function(x, y):
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        my_function(x, y)
    captured = capsys.readouterr()
    assert f"my_function error: ValueError. Inputs: ({x}, {y}), {{}}" in captured.err
