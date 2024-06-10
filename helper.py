from faker import Faker
import allure


class UserFactory:
    @staticmethod
    @allure.step('Генерация тела для создания пользователя')
    def generate_new_user():
        fake = Faker()
        email = fake.email()
        password = fake.password()
        name = fake.name()
        payload = {"email": email, "password": password, "name": name}
        return payload
