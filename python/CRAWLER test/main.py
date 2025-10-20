import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login():
    driver = webdriver.Chrome() 
    driver.get("https://alumibras.nomus.com.br/")
    
    wait = WebDriverWait(driver, 15)
    
    wait = WebDriverWait(driver, 10)
    usuario_input = wait.until(
        EC.element_to_be_clickable((By.ID, "campologin"))
    )

    time.sleep(3)

    usuario_input.send_keys("Lucas")
    usuario_input.send_keys(Keys.TAB)

    senha_input = wait.until(
        EC.element_to_be_clickable((By.NAME, "senha"))
    )

    time.sleep(3)

    senha_input.send_keys("123")
    senha_input.send_keys(Keys.RETURN)

url = "https://alumibras.nomus.com.br/"
resposta = requests.get(url)

print(f"status de resposta da url: {resposta.status_code}")

if resposta.status_code == 200:
    login()
    time.sleep(3)
    input("Pressione enter para fechar o navegador.")
else:
    print("Encerrando programa...")