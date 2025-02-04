import math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators, MainPageLocators


class BasePage(object):
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.HEADER_BASKET)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_clickable(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False

        return True

    def is_elements_match(self, el1, el2):
        assert str.strip(el1) == str.strip(el2), f"{el1} and {el2} don't match"
        assert True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_clickable(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return True

        return False

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        assert True

    def should_be_registration_link(self):
        assert self.is_element_present(*MainPageLocators.REGISTRATION_LINK), "Registration link is not presented"
        assert True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

