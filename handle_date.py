#coding:utf-8from selenium import webdriverimport time#学习处理readonly属性的日期控件#用js去掉元素的属性 removeAttribute("readonly")方法删除属性browser = webdriver.Chrome()browser.maximize_window()browser.get('https://kyfw.12306.cn/otn/index/init')time.sleep(4)'''#这是第一种方法js = 'document.getElementById("train_date").removeAttribute("readonly")'browser.execute_script(js)browser.find_element_by_xpath('//input[@id="train_date"]').clear()  #要先清空输入框browser.find_element_by_xpath('//input[@id="train_date"]').send_keys('2018-02-02')'''#第二种方法就是直接用js方法改value的值js2 = 'document.getElementById("train_date").removeAttribute("readonly")'browser.execute_script(js2)js_sendvalue = 'document.getElementById("train_date").value="2018-01-31"'  #找到元素，赋值给这个元素的valuebrowser.execute_script(js_sendvalue)print('成功输入新日期')browser.close()browser.quit()