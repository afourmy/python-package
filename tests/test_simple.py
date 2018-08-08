from sample.child import Child
from sample.parent import Parent


def test_success():
    p1, p2 = Parent('p1', 35), Parent('p2', 30)
    c1 = Child('c1', 10, p1, p2)
    print(c1)
