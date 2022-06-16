from requests import get

def getAllDeliveryMan():
    return get('https://cybersecurity-fiap.herokuapp.com/v1/deliveryman').json()

def getAllBuyers():
    return get('https://cybersecurity-fiap.herokuapp.com/v1/buyer').json()