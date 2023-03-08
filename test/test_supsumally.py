from src import hoge


def test_bar():
    assert hoge.greet() == 'hello'
