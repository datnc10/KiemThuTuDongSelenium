import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Di đến trang chính của shopee
driver = webdriver.Chrome()
driver.get("https://www.shopee.vn")

#Tắt poppu quảng cáo
close_btn = driver.execute_script('return document.querySelector("#main shopee-banner-popup-stateful").shadowRoot''.querySelector("div.home-popup__close-area div.shopee-popup__close-btn")')
close_btn.click()

#Đăng nhập tài khoản shopee
driver.find_element(By.CSS_SELECTOR, 'a[href="/buyer/login?next=https%3A%2F%2Fshopee.vn%2F"]').click()
time.sleep(2)


#Nhập email tài khoản và mật khẩu
tai_khoan = driver.find_element(By.NAME ,"loginKey")
tai_khoan.send_keys("0335738469")
mat_khau = driver.find_element(By.NAME,"password")
mat_khau.send_keys("Dat114690")
time.sleep(2)
#Nhấn đăng nhập để hoàn tất
BtDangNhap = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div/div[2]/form/div/div[2]/button')
BtDangNhap.click()
time.sleep(2)
#Tìm kiếm 1 shop cụ thể
find_shop = driver.find_element(By.XPATH,'//*[@id="main"]/div/header/div[2]/div/div[1]/div[1]/div/form/input')
find_shop.send_keys("cosrxxx.vn")
find_shop = driver.find_element(By.XPATH,'//*[@id="main"]/div/header/div[2]/div/div[1]/div[1]/button')
find_shop.click()
time.sleep(2)

#Chọn shop cần mua hàng
shop_click = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/a[2]/div[1]')
shop_click.click()
time.sleep(3)

#Tìm kiếm sản phẩm trong shop
find_product = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/header/div[2]/div/div/div[4]/div[1]/div/form/input')
find_product.send_keys("sữa rửa mặt")
find_product.send_keys(Keys.ENTER)
time.sleep(2)

#click để tìm sản phẩm bán chạy
click_bc = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div[2]/div/div[1]/div[1]/div[3]')
click_bc.click()
time.sleep(2)

#chọn sản phẩm cần mua
choose_product = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/a/div/div/div[2]/div[1]/div/div')
choose_product.click()
time.sleep(3)

#chọn loại sản phẩm
choose_loai = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[3]/div/div[4]/div/div[3]/div/div[1]/div/button[2]')
choose_loai.click()
time.sleep(2)

#thêm vào giỏ hàng
add_product = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[3]/div/div[5]/div/div/button[1]')
add_product.click()
time.sleep(3)

#đến giỏ hàng
gioHang = driver.find_element(By.CSS_SELECTOR,'a[href="/cart"]')
gioHang.click()
time.sleep(3)

#Chọn sản phẩm cần mua trong giỏ hàng
chooseInCart = driver.find_element(by = By.XPATH,value =  '//*[@id="main"]/div/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/label/div')
chooseInCart.click()
time.sleep(3)

#mua hàng
choose_muahang = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div/div[3]/div[2]/div[7]/button[4]')
choose_muahang.click()
time.sleep(2)

#Thay đổi địa chỉ
choose_diachi = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]')
choose_diachi.click()
time.sleep(2)
choose_diachimoi = driver.find_element(By.XPATH,'//*[@id="modal"]/aside/div[1]/div/div/div[2]/button')
choose_diachimoi.click()
time.sleep(2)

#Điền thông tin
hoTen = driver.find_element(by = By.XPATH, value ='//*[@id="modal"]/aside/div[1]/div/div/form/div/div[1]/div[1]/div[1]/div/input')
hoTen.send_keys("Phạm Văn Kha")
time.sleep(2)
sDT = driver.find_element(by = By.XPATH, value ='//*[@id="modal"]/aside/div[1]/div/div/form/div/div[1]/div[1]/div[3]/div/input')
sDT.send_keys("0379702356")
time.sleep(2)
#
diaChi = driver.find_element(by = By.XPATH, value = '//*[@id="modal"]/aside/div[1]/div/div/form/div/div[1]/div[2]/div/div/div/input')
diaChi.send_keys('Hà Nội, Quận Hà Đông, Phường Văn Quán ')
time.sleep(5)
diaChiCuThe = driver.find_element(by = By.XPATH, value ='//*[@id="modal"]/aside/div[1]/div/div/form/div/div[1]/div[3]/div/div[1]/div/textarea')
diaChiCuThe.send_keys('188 Đường 19/5')
time.sleep(5)
hoanThanh = driver.find_element(by = By.XPATH, value ='//*[@id="modal"]/aside/div[1]/div/div/form/div/div[2]/button[2]')
hoanThanh.click()
time.sleep(1)
xacNhanViTri = driver.find_element(by = By.XPATH, value = '//*[@id="modal"]/aside[2]/div[1]/div/div[3]/button[2]')
xacNhanViTri.click()
time.sleep(1)
buttoNhaRieng= driver.find_element(by = By.XPATH, value ='//*[@id="modal"]/aside/div[1]/div/div/form/div/div[1]/div[5]/div[2]/div[1]')
buttoNhaRieng.click()
hoanThanh.click()





