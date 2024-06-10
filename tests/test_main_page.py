import allure
import data
from pages.main_page import MainPage
from pages.login_page import LoginPage
import stellar_burgers_api
from helper import UserFactory


class TestMainPage:
    @allure.title("Проверяем переход по кнопке Конструктор")
    @allure.description(
        "Переходим на страницу авторизации, нажимаем кнопку Конструктор, проверяем, что вернулись на главную страницу"
    )
    def test_step_on_main_by_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_enter_account_button()
        main_page.click_constructor_button()

        assert main_page.get_current_url() == data.Urls.STELLAR_BURGERS

    @allure.title("Проверяем переход по кнопке Лента заказов")
    @allure.description(
        "Нажимаем на кнопку Лента заказов, проверяем, что перешли на нужную страницу"
    )
    def test_feed_orders_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_orders_button()

        assert main_page.get_current_url() == data.Urls.FEED_ORDERS_PAGE

    @allure.title("Проверяем, что появится информация при клике по ингредиенту")
    @allure.description(
        "Кликаем по флюоресцентной булке, проверяем что появилось с окной с информацией об ингредиенте"
    )
    def test_click_on_ingredient_and_show_info(self, driver):
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun()

        assert main_page.get_name_by_active_bun() == "Детали ингредиента"

    @allure.title("Проверяем работу закрытия окна с инфо о ингредиенте")
    @allure.description(
        "Кликаем по флюоресцентной булке, нажимаем на крестик, проверяем, что окно закрылось"
    )
    def test_close_window_with_info_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.click_fluorescent_bun()
        main_page.close_info_ingredient_window()
        main_page.wait_invisibility_ingredient_info_window()

        assert main_page.get_availability_active_info_ingredient_window() == False

    @allure.title("Проверяем перетаскивание ингредиента в заказ")
    @allure.description(
        "Переносим булочку в заказ, проверяем, что счетчик у выбранного ингредиента увеличился"
    )
    def test_drag_on_drop_bun_and_counter_increased(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_bun()

        assert main_page.get_quantity_ingredients_per_order() > 0

    @allure.title("Проверяем, что авторизованный пользователь может оформить заказ")
    @allure.description(
        "Авторизуемся в системе, добавляем булочку в заказ, нажимаем кнопку Оформить заказ, проверяем, что оформление заказ прошло успешно"
    )
    def test_create_order_by_auth_user(self, driver):
        new_user = UserFactory.generate_new_user()
        auth_user = stellar_burgers_api.CreateUserApi.create_user(new_user)
        email = new_user["email"]
        password = new_user["password"]
        main_page = MainPage(driver)
        main_page.click_enter_account_button()
        login_page = LoginPage(driver)
        login_page.set_email(email)
        login_page.set_password(password)
        login_page.click_enter_button()
        main_page.wait_visibility_create_order_button()
        main_page.drag_and_drop_bun()
        main_page.click_create_order_button()
        token = auth_user.json()["accessToken"]
        stellar_burgers_api.DeleteUserApi.delete_user(token)

        assert (
            main_page.get_text_successfully_registration()
            == "Ваш заказ начали готовить"
        )
