from pathlib import Path
import allure
from selene import browser, have, command


class RegistrationPage:
    def open(self):
            browser.open('/automation-practice-form')

    def type_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def type_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def type_email(self, email):
        browser.element('#userEmail').type(email)

    def choose_gander(self):
        browser.element('[for="gender-radio-1"]').click()

    def type_phone_number(self, number):
        browser.element('#userNumber').type(number)

    def type_birth_date(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').element(f'[value = "{year}"]').click()
        browser.element('.react-datepicker__month-select').element(f'[value = "{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def type_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def scroll_down(self):
        browser.element('#subjectsInput').perform(command.js.scroll_into_view)

    def select_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()

    def upload_picture(self):
        browser.element('[type="file"]').send_keys(str(Path(__file__).parent.parent.joinpath(
            f'resources/image.jpeg')))

    def type_current_address(self, address):
        browser.element('#currentAddress').type(address)

    def type_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def type_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def click_submit_button(self):
        browser.element('#submit').click()

    def assert_user_data_form(self, full_name, email, gander, phone_number, date_of_birth, subjects, hobbies,
                              picture, address, state_and_city):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{full_name}',
            f'{email}',
            f'{gander}',
            f'{phone_number}',
            f'{date_of_birth}',
            f'{subjects}',
            f'{hobbies}',
            f'{picture}',
            f'{address}',
            f'{state_and_city}'))