from time import sleep
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait as wait 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
import winsound

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/Users/TeamSwitch/Desktop/매크로/갤캠스 매크로/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
caps = DesiredCapabilities().CHROME 
caps["pageLoadStrategy"] = "none"

#전체화면으로하기
#driver.maximize_window()

driver.get('https://www.samsungebiz.com/event/galaxycampus/smartphones/galaxy-s22-s901/SM-S901NIDWKOO/')

#갤럭시 트레이드인 코드
#driver.find_element_by_xpath('//*[@id="goods_detail_wrap"]/div/div[2]/div[1]/div[6]/div[1]/div/label').click()

for i in range(999999999999999999999999999999999):
    check = driver.find_element_by_css_selector('.flag-tag')
    if check.text == '일시품절':
        driver.refresh()
        sleep(0.5)
        driver.implicitly_wait(10)
    else:
        buy = driver.find_element_by_id("btnDirect")
        driver.execute_script("arguments[0].click();", buy)
        winsound.Beep(500 , 1000)
        break

driver.implicitly_wait(10)

#배송일자 선택까지 스크롤
#driver.execute_script("window.scrollTo(0, 850)")

#달력 아이콘 클릭
driver.find_element_by_xpath('//*[@id="extIstHopeDate"]').click()
#배송일자 선택
driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[2]/a').click()
#동의버튼 클릭
driver.find_element_by_xpath('//*[@id="order_payment_form"]/div[4]/div[6]/div/div[1]/label').click()
#동의버튼 클릭
driver.find_element_by_xpath('//*[@id="order_payment_form"]/div[4]/div[6]/div/div[2]/label').click()
#결제하기버튼 클릭
driver.find_element_by_xpath('//*[@id="orderPaymentBtn"]').click()
#주문하시겠습니까?팝업 뜰때까지 대기
sleep(0.5)
#주문확인버튼 클릭
driver.find_element_by_xpath('//*[@id="commonConfirmOkBtn"]').click()