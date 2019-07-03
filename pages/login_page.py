from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_INPUT), "Login email input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT), "Login password input is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_RESET_PASSWORD), "Login reset password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT_BUTTON), "Login submit button is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_INPUT), \
            "Registration email input is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1_INPUT), \
            "Registration password input_1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2_INPUT), \
            "Registration password input_2 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), \
            "Registration submit button is not presented"
        assert True
