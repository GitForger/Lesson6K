from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    
    try:
        # Шаг 1: Открыть страницу в Edge
        print("🖥️ Открываю страницу в Edge...")
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        driver.maximize_window()
        
        # Ждем загрузки формы
        wait.until(EC.presence_of_element_located((By.NAME, "first-name")))
        
        # Шаг 2: Заполнить форму значениями
        print("📝 Заполняю форму...")
        
        # First name
        first_name = driver.find_element(By.NAME, "first-name")
        first_name.clear()
        first_name.send_keys("Иван")
        
        # Last name
        last_name = driver.find_element(By.NAME, "last-name")
        last_name.clear()
        last_name.send_keys("Петров")
        
        # Address
        address = driver.find_element(By.NAME, "address")
        address.clear()
        address.send_keys("Ленина, 55-3")
        
        # Email
        email = driver.find_element(By.NAME, "e-mail")
        email.clear()
        email.send_keys("test@skypro.com")
        
        # Phone number
        phone = driver.find_element(By.NAME, "phone")
        phone.clear()
        phone.send_keys("+7985899998787")
        
        # Zip code - оставить пустым
        zip_code = driver.find_element(By.NAME, "zip-code")
        zip_code.clear()
        
        # City
        city = driver.find_element(By.NAME, "city")
        city.clear()
        city.send_keys("Москва")
        
        # Country
        country = driver.find_element(By.NAME, "country")
        country.clear()
        country.send_keys("Россия")
        
        # Job position
        job_position = driver.find_element(By.NAME, "job-position")
        job_position.clear()
        job_position.send_keys("QA")
        
        # Company
        company = driver.find_element(By.NAME, "company")
        company.clear()
        company.send_keys("SkyPro")
        
        # Шаг 3: Нажать кнопку Submit
        print("🖱️ Нажимаю кнопку Submit...")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()
        
        # Шаг 4: Ждем, пока поле Zip code станет красным
        print("🔴 Ожидаю подсветку поля Zip code...")
        zip_code_field = wait.until(
            EC.presence_of_element_located((By.NAME, "zip-code"))
        )
        
        # Ждем, пока у поля Zip code появится класс is-invalid
        wait.until(
            lambda driver: "is-invalid" in driver.find_element(By.NAME, "zip-code").get_attribute("class")
        )
        print("✅ Поле Zip code подсвечено красным")
        
        # Шаг 5: Проверить, что остальные поля подсвечены зеленым
        print("🟢 Проверяю остальные поля...")
        fields_to_check = [
            "first-name", "last-name", "address", "e-mail", 
            "phone", "city", "country", "job-position", "company"
        ]
        
        for field_name in fields_to_check:
            field = driver.find_element(By.NAME, field_name)
            field_classes = field.get_attribute("class")
            assert "is-valid" in field_classes, f"Поле {field_name} должно быть подсвечено зеленым"
            print(f"✅ Поле {field_name} подсвечено зеленым")
        
        print("\n🎉 ТЕСТ УСПЕШНО ПРОЙДЕН!")
        print("✅ Все требования задачи выполнены!")
        
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        driver.save_screenshot("edge_test_error.png")
        print("📸 Скриншот ошибки сохранен")
        raise
        
    finally:
        driver.quit()
        print("🔚 Браузер закрыт.")


if __name__ == "__main__":
    test_form_validation()
