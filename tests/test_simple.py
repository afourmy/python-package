from pathlib import Path

from sample.child import Child
from sample.open_file import open_yaml_file
from sample.parent import Parent


def test_success():
    p1, p2 = Parent('p1', 35), Parent('p2', 30)
    Child('c1', 10, p1, p2)


def test_open_file():
    open_yaml_file(Path.cwd() / 'data' / 'parameters.yaml')
