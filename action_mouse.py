#coding：utf-8from selenium import webdriverimport timefrom selenium.webdriver.common.action_chains import ActionChainsbrowser = webdriver.Chrome()browser.implicitly_wait(10)'''browser.get('https://www.baidu.com/?tn=94855285_hao_pg')browser.maximize_window()time.sleep(7)target1 = browser.find_element_by_link_text('设置')ActionChains(browser).move_to_element(target1).perform()'''browser.get('http://nj.ganji.com/')browser.maximize_window()time.sleep(5)handle1 = browser.current_window_handleprint('首页的句柄是：%s' % handle1)browser.find_element_by_xpath('//*[contains(@class,"dt-t") and text()="工作"]').click()  #这句牛逼了，居然用xpath逻辑运算time.sleep(10)all_handle = browser.window_handlesprint('当前所有的句柄是：%s' % all_handle)for h in all_handle:    if h != handle1:        browser.switch_to.window(h)    else:        passtitle = browser.titleprint('这是新窗口：%s' % title)browser.close()browser.switch_to.window(handle1)print('这应该是首页：%s' % browser.title)browser.quit()