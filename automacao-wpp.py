import pyautogui
import time

#entrar no chrome
pyautogui.press('win')
time.sleep(2)
pyautogui.write('chrome')
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)

#entrar no whatsapp
pyautogui.click(x=433, y=57)
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
time.sleep(13)

#enviar e entrar no contato que quero enviar a foto
pyautogui.click(x=129, y=209)#clicar nos arquivados do wpp
time.sleep(2)
pyautogui.click(x=149, y=343)#clilcar no primeiro contato dos arquivados
time.sleep(1)
while True:
    pyautogui.click(x=488, y=688)#cliclar nas opções de anexo
    time.sleep(1)
    pyautogui.click(x=529, y=491)#clilcar em fotos em videos
    time.sleep(2)
    pyautogui.click(x=248, y=292)#clicando na foto
    time.sleep(1)
    pyautogui.click(x=712, y=544)#clicando em abrir dentro da pasta de arquivos
    time.sleep(1)
    pyautogui.click(x=1337, y=663)#clicar em enviar a foto










