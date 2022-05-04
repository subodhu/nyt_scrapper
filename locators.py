from selenium.webdriver.common.by import By

# main page
LOGIN_LINK = (By.CSS_SELECTOR, "a[href*='https://myaccount.nytimes.com/auth/login']")
EMAIL_INPUT = (By.ID, "email")
CONTINUE_EMAIL = (By.CSS_SELECTOR, "button[type=submit]")
PASSWORD_INPUT = (By.ID, "password")
LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
TECH_HEADER = (By.CSS_SELECTOR, 'a[href="/section/technology"]')

# technoloty page
SCROLL_TO_TECH_HEADER_LINK = (By.CSS_SELECTOR, 'a[data-id="latest"]')
TOP_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button[data-testid=user-settings-button]')
ACCOUNT_LINK = (
    By.CSS_SELECTOR, 'a[href="https://myaccount.nytimes.com/seg#source=masthead-user-modal"]'
)

# account page
ACCOUNT_ACC_NO = (By.CSS_SELECTOR, 'span[data-testid="account-number:list-item-body"]')
ACCOUNT_EMAIL = (By.CSS_SELECTOR, 'span[data-testid="email-address:list-item-body"]')
