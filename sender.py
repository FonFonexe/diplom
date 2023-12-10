# Наумов Сергей, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


def new_order():
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER, json=data.CREATE_ORDER_BODY)


def aut_track():
    order = new_order()
    return order.json()["track"]


def get_order():
    url = configuration.BASE_URL + configuration.GET_ORDER + str(aut_track())
    print(url)
    return requests.get(url)


respons = get_order()
assert respons.status_code == 200
print(respons.json())
print(respons.status_code)
