from selenium import webdriver
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
# 无头模式
option.add_argument('--headless')
# 隐藏webdriver提示条
option.add_experimental_option('excludeSwitches', ['enable-automation'])
# 隐藏自动化信息
option.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(executable_path='../utils/chromedriver_win32/chromedriver.exe', options=option)
# 将window.navigator中的webdriver属性设置为undefined
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get:()=>undefined})'
})

browser.get('https://antispider1.scrape.center/')

