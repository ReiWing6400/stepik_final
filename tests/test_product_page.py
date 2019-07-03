from ..pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_main_form()

    item_price = page.get_item_price()
    item_name = page.get_item_name()

    page.click_add_to_basket()
    page.solve_quiz_and_get_code()

    header_basket_total_price = page.get_header_basket_total_price()

    page.should_be_messages()
    messages_added_item_name = page.get_messages_added_item_name()
    messages_add_item_price = page.get_messages_added_item_price()

    page.is_elements_match(item_name, messages_added_item_name)
    page.is_elements_match(item_price, messages_add_item_price)
    page.is_elements_match(item_price, header_basket_total_price)
