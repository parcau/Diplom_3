from selenium.webdriver.common.by import By


PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[contains(.,'Восстановить пароль')]")
ENTER_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")
EMAIL_FIELD = (By.XPATH, "//input[contains(@name,'name')]")
PASSWORD_FIELD = (By.XPATH, "//input[contains(@name,'Пароль')]")
