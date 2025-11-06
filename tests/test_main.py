from app.main import add, greet

def test_add():
    assert add(3, 2) == 5

def test_greet():
    assert greet("Pallavi") == "Welcome to CI/CD, Pallavi!"
