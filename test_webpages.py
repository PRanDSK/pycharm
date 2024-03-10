import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSimple:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_python_org(self):
        self.driver.get("https://www.python.org")

        print()
        print()

        print(self.driver.title)

        searchbar = self.driver.find_element(By.NAME, "q")
        searchbar.clear()
        searchbar.send_keys("getting started with python")
        searchbar.send_keys(Keys.ENTER)

        self.driver.find_element(By.LINK_TEXT, "PyTraining: Getting Started with API Design using Python").click()

        # Alternative using a variable to separate the actions:
        # first_link = self.driver.find_element(By.LINK_TEXT, "PyTraining: Getting Started with API Design using Python")
        # first_link.click()

        exact_date = self.driver.find_element(By.CLASS_NAME, "single-date").text
        assert exact_date == "16 Sept."

        time.sleep(3)


    def test_selenium_site(self):
        self.driver.get("https://web.archive.org/web/20180926132852/http://www.seleniumeasy.com/test/basic-first-form-demo.html")
        self.driver.maximize_window()

        # Variable definitions

        message1 = "Hello Hello"
        number1 = "5"
        number2 = "5"

        # Second excercise

        self.driver.find_element(By.ID, "user-message").send_keys(message1)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Show Message']").click()
        message_element = self.driver.find_element(By.ID, "display")
        assert message_element.text == message1

        # Third excercise

        self.driver.find_element(By.ID, "sum1").send_keys(number1)
        self.driver.find_element(By.ID, "sum2").send_keys(number2)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Get Total']").click()
        sum_element = self.driver.find_element(By.ID, "displayvalue")
        assert sum_element.text == str(int(number1) + int(number2))

        # Fourth excercise

    def test_selenium_checkbox(self):
        self.driver.get("https://web.archive.org/web/20180911154259/http://www.seleniumeasy.com/test/basic-checkbox-demo.html")

        self.driver.find_element(By.ID, "isAgeSelected").click()
        text_element = self.driver.find_element(By.ID, "txtAge")
        # print()
        # print(text_element)
        assert text_element.text == "Success - Check box is checked"

        self.driver.find_element(By.ID, "check1").click()

        checkbox1 = self.driver.find_element(By.XPATH, "//label[normalize-space()='Option 1']//input[@type='checkbox']")
        if checkbox1.is_selected():
            print("Checkbox is selected")
        else:
            print("Checkbox is not selected")


        time.sleep(3)


    def test_tablesort(self):
        self.driver.get("https://web.archive.org/web/20180920023230/http://www.seleniumeasy.com/test/table-sort-search-demo.html")

        self.driver.find_element(By.XPATH, "//select[@name='example_length']").click()
        self.driver.find_element(By.XPATH, "//select[@name='example_length']").send_keys("1")
        self.driver.find_element(By.XPATH, "//select[@name='example_length']").send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//th[@aria-label='Age: activate to sort column ascending']").click()

        value1 = self.driver.find_element(By.XPATH, "(//tr[@role='row'])[9]")
        print()
        print(value1)





        time.sleep(3)

    def test_qa_site(self):
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//button[@aria-label='Consent']").click()

        firstName = "Joe"
        lastName = "Doe"
        email = "petkoran@gmail.com"
        gender = "Male"
        phoneNumber = "1234567890"
        birthDate = "06 Nov 1982"
        address1 = "Sofia"
        address2 = "Nice Street 5"

        self.driver.find_element(By.ID, "firstName").send_keys(firstName)
        self.driver.find_element(By.ID, "lastName").send_keys(lastName)
        self.driver.find_element(By.ID, "userEmail").send_keys(email)
        self.driver.find_element(By.XPATH, f"//label[normalize-space()='{gender}']").click()
        self.driver.find_element(By.ID, "userNumber").send_keys(phoneNumber)

        # Entering birth date by typing in the field:
        # self.driver.find_element(By.ID, "dateOfBirthInput").send_keys(Keys.CONTROL, "A")
        # self.driver.find_element(By.ID, "dateOfBirthInput").send_keys(birthDate)


        # Alternative way to select Birth date

        self.driver.find_element(By.ID, "dateOfBirthInput").click()
        select_element_year = self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']")
        select_year = Select(select_element_year)
        select_year.select_by_visible_text("1982")

        select_element_month = self.driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']")
        select_month = Select(select_element_month)
        select_month.select_by_visible_text("November")

        self.driver.find_element(By.CLASS_NAME, "react-datepicker__day--006").click()

        self.driver.find_element(By.ID, "subjectsInput").send_keys("Math")
        self.driver.find_element(By.ID, "subjectsInput").send_keys(Keys.ENTER)


        # Implementing explicit wait
        elements_sport = (WebDriverWait(self.driver, 10).
                          until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Sports']"))))
        elements_sport.click()

        # self.driver.find_element(By.XPATH,"//label[normalize-space()='Sports']").click()
        # self.driver.find_element(By.XPATH,"//label[normalize-space()='Reading']").click()

        self.driver.find_element(By.ID, "currentAddress").send_keys(f"{address1}{Keys.ENTER}{address2}")

        self.driver.find_element(By.XPATH, "//div[contains(text(),'Select State')]").click()
        self.driver.find_element(By.ID, "react-select-3-input").send_keys("Haryana")
        self.driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.ENTER)

        self.driver.find_element(By.XPATH, "//div[contains(text(),'Select City')]").click()
        self.driver.find_element(By.ID, "react-select-4-input").send_keys("Panipat")
        self.driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.ENTER)

        self.driver.find_element(By.ID, "submit").click()

        name_element = self.driver.find_element(By.XPATH, "//td[normalize-space()='Student Name']//following-sibling::td")
        assert name_element.text == f"{firstName} {lastName}"

        mail_element = self.driver.find_element(By.XPATH, "//td[normalize-space()='Student Email']//following-sibling::td")
        assert mail_element.text == email

        gender_element = self.driver.find_element(By.XPATH, "//td[normalize-space()='Gender']//following-sibling::td")
        assert gender_element == gender



        time.sleep(5)
