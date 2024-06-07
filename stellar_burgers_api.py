import requests
from data import Urls
import allure


class CreateUserApi:
    @staticmethod
    @allure.step("Отправка запроса на создание пользователя")
    def create_user(body):
        return requests.post(
            Urls.STELLAR_BURGERS + Urls.CREATE_USER_ENDPOINT, json=body
        )


class DeleteUserApi:
    @staticmethod
    @allure.step("Отправка запроса на удаление пользователя")
    def delete_user(token):
        return requests.delete(
            Urls.STELLAR_BURGERS + Urls.DELETE_USER_ENDPOINT,
            headers={"Authorization": token},
        )
