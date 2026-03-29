from src.decorators import log


def test_decorator_1(capsys, test_log) -> None:
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    message = capsys.readouterr()
    assert message.out == test_log


def test_decorator_2() -> None:
    @log(filename="test")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    assert my_function(1, 2) == 3


def test_decorator_3(capsys, test_log_2) -> None:
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    message = capsys.readouterr()
    assert message.out == test_log_2
