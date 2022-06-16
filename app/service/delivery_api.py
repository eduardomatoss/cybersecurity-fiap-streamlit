from requests import get


def get_all_deliveryman():
    return get("https://cybersecurity-fiap.herokuapp.com/v1/deliveryman").json()


def get_all_buyers():
    return get("https://cybersecurity-fiap.herokuapp.com/v1/buyer").json()
