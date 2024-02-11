from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from vlookup import vlookupTime , vlookupName , vlookupRest

# 初始化Edge瀏覽器驅動程式
driver = webdriver.Chrome()
actions = ActionChains(driver)
# driver.maximize_window()
 
# 前往網站
driver.get('https://smc.jubo.health/overview/dailyRecord')

# 等待直到登錄帳號輸入框出現
account_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login_account"))
)
# 輸入帳號
account_input.send_keys("22017")
 
 
# 等待直到登錄密碼輸入框出現
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login_password"))
)
# 輸入密碼
password_input.send_keys("00000000")

# 等待直到登錄按鈕出現
submit_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login_submit"))
)
# 點擊登錄按鈕
submit_button.click()

# # 點擊切換不需出席按鈕
# edit_button = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[1]/div/div/div[3]/div[1]/div[3]'))
# ).click()
# edit_button = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[2]'))
# ).click()3
# 點擊切換日期按鈕
# for _ in range(3):
#     edit_button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[1]/div/div/div[3]/div[1]/div[1]/div/div[3]'))
#     ).click()
#     sleep(5)

# 點擊總編輯按鈕
edit_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[1]/div/div/button'))
).click()

for _ in range(3):  # 整頁重複兩次  
    try:
        for i in range(4, 14):  # 每頁執行10次
            button_xpath = f'//*[@id="root"]/div[4]/div[1]/div/div/div[3]/div[2]/div[1]/div[{i}]/div[18]/button' #定位編輯按鈕
            button1_xpath = f'//*[@id="root"]/div[4]/div[1]/div/div/div[3]/div[2]/div[1]/div[{i}]/div[16]' #定位指標滾動位置
            text = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div[4]/div[1]/div/div/div[3]/div[2]/div[1]/div[{i}]/div[1]/div'))).text[:6]
            result = vlookupTime(text)
            name = vlookupName(text)
            rest = vlookupRest(text)
            print('開始登錄'+text+name)
            target_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, button1_xpath)))
            actions.move_to_element(target_button).perform()  # 移動到元素位置
            actions.send_keys_to_element(target_button, "\ue015").perform()  # 向下滾動
            try:
                if result == "半":
                    edit2_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, button_xpath))).click()
                    edit3_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))).click()
                    edit4_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[1]/div[2]/div/div[1]'))).click() #點擊出席按鈕
                    # 找到輸入框元素
                    input_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[2]/div[2]/div/div/div[2]/div'))).click()
                    actions = ActionChains(driver)
                    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                    actions.key_down("1").perform()
                    actions.key_down("2").perform()
                    actions.key_down("0").perform()
                    actions.key_down("0").perform()
                    input_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[3]/div[2]/div/div/div[2]/div'))).click()
                    actions = ActionChains(driver)
                    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                    actions.key_down("1").perform()
                    actions.key_down("6").perform()
                    actions.key_down('0').perform()
                    actions.key_down("0").perform()
                    #//*[@id="mui-component-select-serviceType"]
                    edit5_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, 'mui-component-select-serviceType'))).click()
                    edit6_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-serviceType"]/div[3]/ul/li[2]'))).click()
                    edit7_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[1]/form/div[4]/div/button[2]'))).click()
                    print("半日登錄完畢")
                    sleep(10)
                elif result == "病":
                    edit2_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, button_xpath))).click()
                    edit3_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))).click()
                    edit4_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[1]/div[2]/div/div[2]'))).click() #點擊全日請假按鈕
                    edit5_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[4]/div[2]/div/div/div'))).click() #點擊請假選擇框
                    edit6_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-awayReason"]/div[3]/ul/li[4]'))).click() #點擊請假選擇框//*[@id="menu-awayReason"]/div[3]/ul/li[4]
                    edit7_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[1]/form/div[4]/div/button[2]'))).click() #儲存按鈕
                    print("病假登錄完畢")
                    sleep(10)
                elif result == "事":
                    edit2_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, button_xpath))).click()
                    edit3_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))).click()
                    edit4_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[1]/div[2]/div/div[2]'))).click() #點擊全日請假按鈕
                    edit5_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[4]/div[2]/div/div/div'))).click() #點擊請假選擇框
                    edit6_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="menu-awayReason"]/div[3]/ul/li[3]'))).click() #點擊請假選擇框//*[@id="menu-awayReason"]/div[3]/ul/li[4]
                    edit7_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[1]/form/div[4]/div/button[2]'))).click() #儲存按鈕 
                    print("事假登錄完畢")   
                    sleep(10)
                else:
                    if rest == "Y":
                        # 點擊編輯按鈕2
                        edit2_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, button_xpath))).click()
                        sleep(0.5)
                        # 點擊個案簽到退按鈕
                        edit3_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))).click()
                        # 點擊出席按鈕
                        edit4_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[1]/div[2]/div/div[1]'))).click()
                        # 找到輸入框元素
                        input_element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[2]/div[2]/div/div/div[2]/div'))).click()
                        actions = ActionChains(driver)
                        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                        actions.key_down("0").perform()
                        actions.key_down("8").perform()
                        actions.key_down(str(result)).perform()
                        actions.key_down("0").perform()
                        input_element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[3]/div[2]/div/div/div[2]/div'))).click()
                        actions = ActionChains(driver)
                        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                        actions.key_down("1").perform()
                        actions.key_down("6").perform()
                        actions.key_down(str(result)).perform()
                        actions.key_down("0").perform()
                        #//*[@id="mui-component-select-serviceType"]
                        edit5_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.ID, 'mui-component-select-serviceType'))).click()
                        #//*[@id="menu-serviceType"]/div[3]/ul/li[3]
                        edit6_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="menu-serviceType"]/div[3]/ul/li[3]'))).click()
                        edit7_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[1]/form/div[4]/div/button[2]'))).click()
                        print("喘息登錄完畢")
                        sleep(10)
                    else:
                        # 點擊編輯按鈕2
                        edit2_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, button_xpath))).click()
                        sleep(0.5) 
                        # 點擊個案簽到退按鈕
                        edit3_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/ul/li[1]'))).click()
                        # 點擊出席按鈕
                        edit4_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[1]/div[2]/div/div[1]'))).click()
                        # 找到輸入框元素
                        input_element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[2]/div[2]/div/div/div[2]/div'))).click()
                        actions = ActionChains(driver)
                        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                        actions.key_down("0").perform()
                        actions.key_down("8").perform()
                        actions.key_down(str(result)).perform()
                        actions.key_down("0").perform()
                        input_element = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="body_content_scrollable"]/div/div[3]/div[2]/div/div/div[2]/div'))).click()
                        actions = ActionChains(driver)
                        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                        actions.key_down("1").perform()
                        actions.key_down("6").perform()
                        actions.key_down(str(result)).perform()
                        actions.key_down("0").perform() 
                        edit5_button = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[1]/form/div[4]/div/button[2]'))).click()
                    print("全日登錄完畢")
                    sleep(10)
            except:
                print("登錄失敗")
                continue
        edit6_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[1]/div/div/div[3]/td/div/div[2]/button[2]'))).click()
        print("已換頁")
    except:
        print("換頁失敗")
        
    