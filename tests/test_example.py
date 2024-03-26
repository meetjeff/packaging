from example_package_jeff_hsu.example import add_one

def test_add_one():
    assert add_one(1) == 4
    assert add_one(-1) == 2
    assert add_one(0) == 3