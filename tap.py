from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import time
def tap():
    caps = {}
    caps["platformName"] = "ios"
    caps["platformVersion"] = "13.5"
    caps["udid"] = "07fde8b160e7a00dfd898b60def40016b91e96e4"
    caps["deviceName"] = "ipad"
    caps["automationName"] = "XCUITest"
    caps["xcodeOrgId"] = "33VQ5Q39H2"
    caps["xcodeSigningId"] = "iPhone Developer"

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    TouchAction(driver).tap(x=204, y=758).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=401, y=225).perform()
    time.sleep(0.8)
    
    TouchAction(driver).tap(x=380, y=275).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=401, y=225).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=235, y=735).perform()
    time.sleep(0.8)
    time.sleep(0.8)
    TouchAction(driver).tap(x=431, y=217).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=431, y=225).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=270, y=714).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=462, y=235).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=440, y=297).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=237, y=772).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=438, y=223).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=448, y=219).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=293, y=737).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=438, y=198).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=473, y=239).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=326, y=721).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=483, y=206).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=407, y=289).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=367, y=704).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=285, y=262).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=343, y=277).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=270, y=782).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=465, y=196).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=361, y=275).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=301, y=768).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=407, y=229).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=444, y=279).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=310, y=807).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=394, y=237).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=405, y=233).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=372, y=764).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=312, y=248).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=388, y=260).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=405, y=721).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=407, y=233).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=479, y=246).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=442, y=741).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=440, y=223).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=458, y=223).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=462, y=756).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=415, y=246).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=398, y=262).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=434, y=772).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=388, y=227).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=384, y=264).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=341, y=789).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=378, y=233).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=421, y=250).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=339, y=818).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=411, y=223).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=392, y=264).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=409, y=782).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=440, y=219).perform()
    time.sleep(0.8)
    TouchAction(driver).tap(x=382, y=279).perform()
    time.sleep(0.8)

    driver.quit()
