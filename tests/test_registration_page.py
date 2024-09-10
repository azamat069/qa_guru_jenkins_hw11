from pages.registration_page import RegistrationPage
import allure


def test_registration_page():
    registration_page = RegistrationPage()
    with allure.step('Открываем браузер, на странице регистрации'):
        registration_page.open()
    with allure.step('Вводим ФИО пользователя'):
        registration_page.type_first_name('Azamat')
        registration_page.type_last_name('QA')
    with allure.step('Заполняем основную информацию'):
        registration_page.type_email('email@email.com')
        registration_page.choose_gander()
        registration_page.type_phone_number('1234567890')
        registration_page.type_birth_date(1999, 3, 17)
        registration_page.scroll_down()
        registration_page.type_subjects('Computer Science')
        registration_page.select_hobbies()
        registration_page.upload_picture()
        registration_page.type_current_address('Moscow\nLenina 124 street')
        registration_page.type_state('Haryana')
        registration_page.type_city('Karnal')
        registration_page.click_submit_button()
    with allure.step('Проверям данные'):
        registration_page.assert_user_data_form('Azamat QA', 'email@email.com', 'Male',
                                                '1234567890', '17 April,1999',
                                                'Computer Science', 'Sports, Music',
                                                'image.jpeg', 'Moscow Lenina 124 street', 'Haryana Karnal')
