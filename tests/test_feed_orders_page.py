import allure
from pages.main_page import MainPage
from pages.feed_orders_page import FeedOrders
from pages.login_page import LoginPage
from pages.personal_cabinet_page import PersonalCabinet
import stellar_burgers_api
from helper import UserFactory


class TestFeedOrders:
    @allure.title("Проверяем, что при нажатии на заказ открываются подробности")
    @allure.description(
        "Переходим в Ленту закзов, нажимаем на заказ, проверяем, что всплывающее окно с информацией открылось"
    )
    def test_click_on_last_order(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_orders_button()
        feed_orders = FeedOrders(driver)
        feed_orders.wait_clickable_last_order()
        feed_orders.click_last_order()
        feed_orders.wait_visibility_order_number_in_info_window()

        assert feed_orders.get_availability_active_info_order_window() == True

    @allure.title("Проверяем, что счетчик Выполнено за сегодня увеличивается")
    @allure.description(
        "Создаем пользователя, авторизуемся, фиксируем число в счетчике выполнено за сегодня, оформляем заказ, проверяем, что счетчик увеличился"
    )
    def test_increase_counter_completed_for_today(self, driver):
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
        main_page.click_feed_orders_button()
        feed_orders = FeedOrders(driver)
        feed_orders.wait_visibility_counter_completed_today()
        current_quantity = feed_orders.get_quantity_counter_completed_today()
        main_page.click_constructor_button()
        main_page.wait_visibility_create_order_button()
        main_page.drag_and_drop_bun()
        main_page.click_create_order_button()
        main_page.wait_clickable_close_success_order_window_button()
        main_page.close_success_order_window()
        main_page.click_feed_orders_button()
        feed_orders.wait_visibility_counter_completed_today()
        token = auth_user.json()["accessToken"]
        stellar_burgers_api.DeleteUserApi.delete_user(token)

        assert feed_orders.get_quantity_counter_completed_today() > current_quantity

    @allure.title(
        "Проверяем, что заказы из Истории заказов отобрабражаются в Ленте заказов"
    )
    @allure.description(
        "Создаем пользователя, авторизуемся, оформляем заказ, переходим в Историю заказов и проверяем что этот заказ есть в Ленте заказво"
    )
    def test_user_orders_history_displayed_on_feed_orders(self, driver):
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
        main_page.wait_clickable_close_success_order_window_button()
        main_page.close_success_order_window()
        main_page.click_personal_cabinet_button()
        personal_cabinet = PersonalCabinet(driver)
        personal_cabinet.wait_visibility_orders_history_button()
        personal_cabinet.click_orders_history_buttons()
        personal_cabinet.wait_load_orders_list()
        expected_result = personal_cabinet.get_number_last_order()
        main_page.click_feed_orders_button()
        feed_orders = FeedOrders(driver)
        token = auth_user.json()["accessToken"]
        stellar_burgers_api.DeleteUserApi.delete_user(token)

        assert expected_result in feed_orders.get_orders_list()

    @allure.title("Проверяем, что счетчик Выполнено за все время увеличивается")
    @allure.description(
        "Создаем пользователя, авторизуемся, фиксируем число в счетчике выполнено за все время, оформляем заказ, проверяем, что счетчик увеличился"
    )
    def test_increase_counter_completed_for_all_time(self, driver):
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
        main_page.click_feed_orders_button()
        feed_orders = FeedOrders(driver)
        feed_orders.wait_visibility_counter_completed_today()
        current_quantity = feed_orders.get_quantity_counter_completed_all_time()
        main_page.click_constructor_button()
        main_page.wait_visibility_create_order_button()
        main_page.drag_and_drop_bun()
        main_page.click_create_order_button()
        main_page.wait_clickable_close_success_order_window_button()
        main_page.close_success_order_window()
        main_page.click_feed_orders_button()
        feed_orders.wait_visibility_counter_completed_today()
        token = auth_user.json()["accessToken"]
        stellar_burgers_api.DeleteUserApi.delete_user(token)

        assert feed_orders.get_quantity_counter_completed_all_time() > current_quantity

    @allure.title("Проверяем, что заказ появляется в разделе В работе")
    @allure.description(
        "Создаем пользователя, авторизуемся, оформляем заказ, проверяем, что номер заказа появился в разделе в Работе"
    )
    def test_completed_order_appears_in_progress_section(self, driver):
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
        main_page.wait_clickable_close_success_order_window_button()
        main_page.wait_visibility_load_img()
        main_page.wait_invisibility_load_img()
        new_order_number = main_page.get_new_order_number()
        main_page.close_success_order_window()
        main_page.click_feed_orders_button()
        feed_orders = FeedOrders(driver)
        feed_orders.wait_visibility_order_number_in_work()
        list_orders_in_work = feed_orders.get_list_orders_in_work()
        token = auth_user.json()["accessToken"]
        stellar_burgers_api.DeleteUserApi.delete_user(token)

        assert new_order_number in list_orders_in_work
