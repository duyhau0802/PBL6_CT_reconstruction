import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_01():
    # Khởi tạo trình duyệt Edge
    driver = webdriver.Edge()

    # Mở trang web của bạn
    path = "http://127.0.0.1:5000/"
    driver.get(path)

    # Đợi 1 giây để trang web tải
    time.sleep(1)

    # Tìm nút Submit và nhấn
    submit_button = driver.find_element(By.ID, 'button')
    submit_button.click()

    # Đợi 1 giây để trang web xử lý
    time.sleep(1)

    # Tìm thông báo lỗi và kiểm tra hiển thị
    error_message = driver.find_element(By.ID, 'error-missingfile')
    assert error_message.is_displayed()

    # Đóng trình duyệt
    driver.quit()
