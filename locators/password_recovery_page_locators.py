from selenium.webdriver.common.by import By

EMAIL_FIELD = (By.XPATH, "//input[contains(@name,'name')]")
RECOVERY_BUTTON = (By.XPATH, "//button[contains(.,'Восстановить')]")
SAVE_BUTTON = (By.XPATH, "//button[contains(.,'Сохранить')]")
SHOW_HIDE_PASS_BUTTON = (
    By.XPATH,
    "//div[contains(@class,'input__icon input__icon-action')]",
)
PASSWORD_FIELD = (By.XPATH, "//input[contains(@type,'password')]")
PASSWORD_FIELD_PARENT = (By.XPATH, "//input[contains(@type,'text')]/parent::div")
INPUT_PASSWORD = (
    By.XPATH,
    "//input [@class= 'text input__textfield text_type_main-default' and @type= 'password']",
)
HIGHLIGHTED_PASSWORD_FIELD = (
    By.XPATH,
    "//div [@class= 'input pr-6 pl-6 input_type_text input_size_default input_status_active']",
)
