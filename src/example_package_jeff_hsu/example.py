import validators

def check_email(email: str):
    if validators.email(email):
        return(f"{email} is a email")
    return(f"{email} is not a email")

def check_url(url: str):
    if validators.url(url):
        return(f"{url} is a url")
    return(f"{url} is not a url")