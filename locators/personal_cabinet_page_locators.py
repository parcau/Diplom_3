from selenium.webdriver.common.by import By

ORDERS_HISTORY_BUTTON = (By.XPATH, "//a[contains(.,'История заказов')]")
QUIT_BUTTON = (By.XPATH, "//button[contains(.,'Выход')]")
LAST_ORDER_NUMBER = (By.XPATH, "//p [@class= 'text text_type_digits-default']")
