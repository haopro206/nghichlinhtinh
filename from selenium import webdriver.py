from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os
import time

# Tải thông tin từ tệp .env
load_dotenv()
EMAIL = os.getenv("FB_EMAIL")
PASSWORD = os.getenv("FB_PASS")

# Đường dẫn đến ChromeDriver
CHROMEDRIVER_PATH = "/path/to/chromedriver"  # Thay bằng đường dẫn thật

# Khởi tạo trình duyệt Chrome
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

try:
    # Truy cập Facebook
    driver.get("https://www.facebook.com/")
    time.sleep(2)

    # Đăng nhập
    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "pass")

    email_input.send_keys(EMAIL)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # Mở Messenger
    driver.get("https://www.facebook.com/messages/t/")
    time.sleep(5)

    # Tìm bạn bè
    friend_name = "Tên bạn bè"  # Thay bằng tên người bạn muốn nhắn tin
    search_box = driver.find_element(By.XPATH, '//input[@aria-label="Tìm kiếm trên Messenger"]')
    search_box.send_keys(friend_name)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    # Gửi tin nhắn
    message = "Tin nhắn bạn muốn gửi"  # Nội dung tin nhắn
    repeat_count = 5  # Số lần gửi tin nhắn
    message_box = driver.find_element(By.XPATH, '//div[@aria-label="Nhập tin nhắn"]')

    for _ in range(repeat_count):
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)
        time.sleep(1)

    print("Tin nhắn đã được gửi thành công!")

except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

finally:
    # Đóng trình duyệt
    driver.quit()
    