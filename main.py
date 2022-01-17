from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        self.mensagem = "Mensagem automática"
        self.groups = ["Grupo 1", "Grupo 2"]
        options = webdriver.ChromeOptions()
        # Caminho do driver e onde sessão do chrome será cacheada (evitando ler o qr code toda vez que for executado)
        options.add_argument(r"user-data-dir=./driver/data")
        options.add_argument('lang=pt-br')  # Definindo idioma
        self.driver = webdriver.Chrome(
            executable_path=r'./driver/chromedriver', options=options)  # Definindo o caminho do chromedriver

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)
        for group in self.groups:
            group = self.driver.find_element_by_xpath(
                f"//span[@title='{group}']")
            time.sleep(2)
            group.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(2)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            button_send = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(2)
            button_send.click()
            time.sleep(2)


bot = WhatsappBot()
bot.EnviarMensagens()
