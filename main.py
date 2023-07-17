import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Эмуляция действий клавиатуры
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import config

# Определяем драйвер
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 30)
driver.get(config.rabbit)
driver.maximize_window()


# Функция для скролла в конец страницы
def scroll_down():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def creating_invoices():
    # Вводим логин
    user = driver.find_element(By.XPATH, "//input[@name='username']")
    user.send_keys(config.user_rabbit)
    # Вводим логин и жмем клавишу "ENTER"
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys(config.password_rabbit)
    password.send_keys(Keys.RETURN)
    # Переходим в нужную нам очередь
    driver.get(config.stock_balance_queue)

    # Скролл вниз и раскрытие списка
    time.sleep(1)
    scroll_down()
    driver.find_element(By.XPATH, "//*[@id='main']/div[4]/h2").click()
    scroll_down()

    # Заполнение поля отправки в очередь
    driver.find_element(By.XPATH, "//textarea[@name='payload']").send_keys(
        '''<?xml version="1.0" encoding="UTF-8"?>
<tag0:Message xmlns:tag0="http://www.t1-consulting.ru">
   <tag0:Body>
      <tag0:classData44>
         <tag0:invoiceId>2ded789e-1038-4f29-b614-19e15af8a90c</tag0:invoiceId>
         <tag0:invoiceNumber>730021</tag0:invoiceNumber>
         <tag0:updateId/>
         <tag0:updateVersion/>
         <tag0:invoiceDate>2023-04-20T00:00:00</tag0:invoiceDate>
         <tag0:invoiceVersion>958614</tag0:invoiceVersion>
         <tag0:partnerName>ПОЧТА РОССИИ АО</tag0:partnerName>
         <tag0:partnerId>e9ad273c-147b-11ec-ac9b-141877510b08</tag0:partnerId>
         <tag0:recipient>6c7458be-45cb-464a-83b9-51ba4ab43814</tag0:recipient>
         <tag0:invoiceAcceptanceStatus/>
         <tag0:invoiceRejectedComment/>
         <tag0:invoiceRejectedManager/>
         <tag0:tickets>
            <tag0:row>
               <tag0:productId>55cb4fb8-7bed-4617-bd02-b874e124326a</tag0:productId>
               <tag0:productName>Name Lottery</tag0:productName>
               <tag0:drawId/>
               <tag0:logisticType>coupon</tag0:logisticType>
               <tag0:drawNumber/>
               <tag0:series>010</tag0:series>
               <tag0:numberOrder/>
               <tag0:quant>1</tag0:quant>
               <tag0:lostQuant>0</tag0:lostQuant>
               <tag0:packaging>
                  <tag0:row>
                     <tag0:id>7e57a840-6c10-49f1-97be-afee1404ffb9</tag0:id>
                     <tag0:box>104011600000651</tag0:box>
                     <tag0:unit>6</tag0:unit>
                     <tag0:ticketInBox>100</tag0:ticketInBox>
                  </tag0:row>
               </tag0:packaging>
            </tag0:row>
         </tag0:tickets>
      </tag0:classData44>
   </tag0:Body>
   <tag0:ClassId>44</tag0:ClassId>
   <tag0:CreationTime>2023-05-16T12:47:22</tag0:CreationTime>
   <tag0:Id>6eb2d189-bf0e-47b8-a89e-774fa897490d</tag0:Id>
   <tag0:Receiver/>
   <tag0:Source>UT</tag0:Source>
   <tag0:Type>DTP</tag0:Type>
</tag0:Message>
    ''')
    # Отправка сообщения в очередь
    driver.find_element(By.XPATH, "//input[@value='Publish message']").click()


creating_invoices()
