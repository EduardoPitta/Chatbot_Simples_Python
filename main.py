import pyautogui as pt
from time import sleep
import pyperclip
import random



sleep(3)

position1 = pt.locateOnScreen("whatsapp/smile_clip.png", confidence=.85)
print(position1)
x = position1[0]
y = position1[1]

def initialize_contacts():
    with open("contatos.txt", "r") as f:
        contatos = f.readlines()
    contatos = [x.strip() for x in contatos]
    f.close()
    return contatos

def add_contact(contato):
    f = open("contatos.txt","a")
    f.write( "\n" + contato)
    f.close()


def get_message():
    global x, y

    position = pt.locateOnScreen("whatsapp/smile_clip.png", confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=1)
    pt.moveTo(x + 85, y - 45, duration=1)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    return whatsapp_message

# Posts
def post_response(message):
    global x,y
    position = pt.locateOnScreen("whatsapp/smile_clip.png", confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 107, y + 23, duration= 0.5)
    pt.click()
    pt.typewrite(message, interval=0.05)

    pt.typewrite("\n", interval=0.5)

# Processes

def process_response(message):

    if "1" in str(message).lower():
        return "Ok, entendi! Tchau tchau!"
    else:
        add_contact()
        return "Oi! Sou o robozinho! Para me desligar mande '1'."

def check_for_new_messages():  
    pt.moveTo(x+80,y-35)

    while True:
        #Continuously checks for green dot
        try:
            position = pt.locateOnScreen("whatsapp/verde.png", confidence = 0.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-10,0)
                pt.click()
                sleep(.5)

        except(Exception):
            print("No new other users with new messages.")
        #Checks for new messages
        try :
            cor = pt.pixelMatchesColor(int(x + 80), int(y - 35), (255,255,255), tolerance=0)
            if cor == True:

                processed_message = process_response(get_message())
                post_response(processed_message)
            else:
                print("No new messages")
        except(Exception):
            print("Nada novo.")
    sleep(5)


# Check User

def check_contact():
    with open("contatos.txt", "r") as f:
        contatos = f.readlines()
    contatos = [x.strip() for x in contatos]
    f.close()

    global x,y
    position = pt.locateOnScreen("whatsapp/smile_clip.png", confidence=0.6)
    x = position[0]
    y = position[1]

#clica no nome em cima
    pt.moveTo(x, y, duration=1)
    pt.moveTo(x + 94, y - 852, duration=1)
    pt.click()
    
#clica e copia nome do lado
    pt.moveTo(x, y, duration=1)
    pt.moveTo(x + 649, y - 556, duration=1)
    pt.tripleClick()
    pt.rightClick()
    pt.moveTo(x + 661, y - 551, duration=1)
    pt.click()
    contato = pyperclip.paste()
    pt.moveTo(x + 648, y - 851, duration=1)
    pt.click()
    print(contato)
#se número ou nome está na lista, voltar False e colocar como não lida
    for name in contatos:
        if name == contato:
            return False

    return True

#print(check_contact())
