import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_TC_03():
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

    # Tìm nút Submit và nhấn
    submit_button = driver.find_element(By.ID, 'button')
    submit_button.click()

    time.sleep(2)

    # Kiểm tra trạng thái hiển thị của div 'result'
    result_div = driver.find_element(By.ID, 'result')
    assert result_div.is_displayed()
    
    if result_div.is_displayed():
        print("Kiểm tra thành công: div 'result' có hiển thị (display là block)")
    else:
        print("Kiểm tra thất bại: div 'result' không hiển thị (display là none)")

    # Đóng trình duyệt
    driver.quit()

# Gọi hàm kiểm thử
test_TC_03()
