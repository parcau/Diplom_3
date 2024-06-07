import allure
from selenium.webdriver import ActionChains
import locators.main_page_locators
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @allure.step("Кликаем по кнопке Войти в аккаунт")
    def click_enter_account_button(self):
        button = self.find_element(locators.main_page_locators.ENTER_ACCOUNT_BUTTON)
        button.click()

    @allure.step("Ожидаем наличия кнопки Войти в аккаунт")
    def wait_clickable_enter_in_account_button(self):
        return self.wait_clickable_element(
            locators.main_page_locators.ENTER_ACCOUNT_BUTTON
        )

    @allure.step("Кликаем по кнопке Личный кабинет")
    def click_personal_cabinet_button(self):
        button = self.find_element(locators.main_page_locators.PERSONAL_CABINET_BUTTON)
        button.click()

    @allure.step("Кликаем по кнопке Конструктор")
    def click_constructor_button(self):
        button = self.find_element(locators.main_page_locators.CONSTRUCTOR_BUTTON)
        button.click()

    @allure.step("Получаем текущий url страницы")
    def get_current_url(self):
        return self.current_url()

    @allure.step("Кликаем по кнопке Лента заказов")
    def click_feed_orders_button(self):
        button = self.find_element(locators.main_page_locators.ORDER_FEED_BUTTON)
        button.click()

    @allure.step("Кликаем по флюоресцентной булке")
    def click_fluorescent_bun(self):
        button = self.find_element(locators.main_page_locators.FLUORESCENT_BUN)
        button.click()

    @allure.step("Получаем название флюоресцентной булки из окна информации")
    def get_name_by_active_bun(self):
        active_ingredient = self.find_element(
            locators.main_page_locators.ACTIVE_INGREDIENT
        )
        return active_ingredient.text

    @allure.step("Закрываем окно с инфо о ингредиенте")
    def close_info_ingredient_window(self):
        button = self.find_element(locators.main_page_locators.CLOSE_INFO_BUTTON)
        button.click()

    @allure.step("Проверяем наличие открытого окна с инфо о ингредиенте")
    def get_availability_active_info_ingredient_window(self):
        element = self.find_element(locators.main_page_locators.CLOSE_INFO_BUTTON)
        if element.is_displayed():
            return True
        else:
            return False

    @allure.step("Перетягиваем булочку в заказ")
    def drag_and_drop_bun(self):
        source_element = self.find_element(locators.main_page_locators.FLUORESCENT_BUN)
        target_element = self.find_element(
            locators.main_page_locators.ADD_TO_ORDER_FIELD
        )
        actions = ActionChains(self.driver)
        return actions.drag_and_drop(source_element, target_element).perform()

    @allure.step("Получаем кол-во добавленного ингредиента в заказ")
    def get_quantity_ingredients_per_order(self):
        quantity = self.find_element(
            locators.main_page_locators.COUNTER_FLUORESCENT_BUN
        )
        return int(quantity.text)

    @allure.step("Кликаем по кнопке Оформить заказ")
    def click_create_order_button(self):
        button = self.find_element(locators.main_page_locators.CREATE_ORDER_BUTTON)
        button.click()

    @allure.step("Получаем текст из инфо об успешно оформленом заказе")
    def get_text_successfully_registration(self):
        success_reg = self.find_element(
            locators.main_page_locators.SUCCESSFUL_REGISTRATION
        )
        return success_reg.text

    @allure.step("Ожидаем наличия кнопки Оформить заказ")
    def wait_visibility_create_order_button(self):
        return self.wait_visibility_element(
            locators.main_page_locators.CREATE_ORDER_BUTTON
        )

    @allure.step("Ожидаем закрытия всплывающего окна с инфо о ингредиенте")
    def wait_invisibility_ingredient_info_window(self):
        return self.wait_invisibility_element(
            locators.main_page_locators.CLOSE_INFO_BUTTON
        )

    @allure.step("Закрываем окно с успешным оформлением заказа")
    def close_success_order_window(self):
        button = self.find_element(
            locators.main_page_locators.CLOSE_SUCCESS_ORDER_WINDOW_BUTTON
        )
        return button.click()

    @allure.step(
        "Ожидаем кликабельности кнопки закрытия окна с успешным оформлением заказа"
    )
    def wait_clickable_close_success_order_window_button(self):
        return self.wait_clickable_element(
            locators.main_page_locators.CLOSE_SUCCESS_ORDER_WINDOW_BUTTON
        )

    @allure.step("Получаем номер созданного зхаказ")
    def get_new_order_number(self):
        number = self.find_element(locators.main_page_locators.NEW_ORDER_NUMBER)
        return number.text

    @allure.step("Ожидаем видимости изображения загрузки сформированного зазака")
    def wait_visibility_load_img(self):
        return self.wait_visibility_element(
            locators.main_page_locators.LOADING_IMG_ORDER_FORMATION
        )

    @allure.step("Ожидаем невидимости изображения загрузки сформированного заказа")
    def wait_invisibility_load_img(self):
        return self.wait_invisibility_element(
            locators.main_page_locators.LOADING_IMG_ORDER_FORMATION
        )
