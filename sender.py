# Наумов Сергей, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


def test_create_order():
    def new_order():
        return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER, json=data.CREATE_ORDER_BODY)

    order = new_order()
    track = order.json()["track"]

    url = configuration.BASE_URL + configuration.GET_ORDER + str(track)
    response = requests.get(url)

    assert response.status_code == 200
    return response.json()


result = test_create_order()
print(result)
