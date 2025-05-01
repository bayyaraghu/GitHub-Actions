# app.py
# Making changes
def add(a, b):
    return a + b
def mul(a, b):
    return a * b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
