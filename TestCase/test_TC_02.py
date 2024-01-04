import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_02():
    # Khởi tạo trình duyệt Edge
    driver = webdriver.Edge()

    # Mở trang web của bạn
    path = "http://127.0.0.1:5000/"
    driver.get(path)

    # Đợi 1 giây để trang web tải
    time.sleep(1)

        # Simulate selecting an image file
    image_input = driver.find_element(By.ID, 'imageInput')
    image_input.send_keys("E:\download\PBL6_CT_reconstruction\TestCase\X_test_0.png") 

    # Wait for a short time to allow the image preview to be updated
    time.sleep(2)

    # Check if the image preview is displayed
    image_preview = driver.find_element(By.ID, 'imagePreview')
    assert image_preview.is_displayed()

    # Đóng trình duyệt
    driver.quit()

# Gọi hàm kiểm thử
test_02()
