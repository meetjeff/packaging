from example_package_jeff_hsu.example import check_email, check_url

def test_check_email():
    assert check_email("test@example.com") == "test@example.com is a email"
    assert check_email("test_example.com") == "test_example.com is not a email"
    assert check_email("test@example") == "test@example is not a email"

def test_check_url():
    assert check_url("https://www.example.com") == "https://www.example.com is a url"
    assert check_url("www.example.com") == "www.example.com is not a url"
    assert check_url("https://www.example") == "https://www.example is a url"