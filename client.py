#client.py
import socket
import time


print("\n(The ip address is by defult set to 'localhost on the client side)")
port = print("\nType in the same port number that is set for the server to connect you're bot to the Chat room: (Eks: 4242)")

try:
     #port = 4242
     port = int(input("Inputt port number here: "))

except Exception as e:
    time.sleep(1)
    print("\nERROR! - A port number can only contain numbers \n(Run the client again)\n")
    socket.close()

print("\nType in a Alias/name for this chat Bot into the terminal (Eks: Lars) ")
client_navn = input("Inputt a Alias/name: ")

if not client_navn:
    print("\nERROR!! You did not enter a NAME into the terminal\nPlease try to start the client again and input a name into the terminal\n")
    socket.close()


ip = "localhost"
Socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket for TCP server
Socket.connect((ip, port)) # koble til server med ip - localhost og valgfri port

Socket.send(client_navn.encode()) # send clientnavn til server
print(Socket.recv(500).decode()) #print meldingen fra serveren om at jeg er koblet til


b = None # må resette variabelen action hver gang så vi kan velge ut det siste ordet i host meldingen
              #eller så velges bare det siste ordet i botene sin setingen ut



#se på denne delen som er definert
def Client_bots(botName, action, recv_message):

    bad_words = ["yell", "steal", "fight"]
    good_words = ["hug", "play", "eat", "shop"]

    global b # Siste ordet som ble tatt fra Host sin melding
    global boolean_badWord # boolean verdi for dårlig ord - action
    global boolean_goodWord #boolean verdi for god ord - action
    global bot_index #kjør bot og gå videre til neste bot


    if recv_message == "Batman": #Hvis serveren sender melding til clitenten og stringen inneholder navnet 'Admin', så skal bot 1 svare
        bot_index = 1 #bot 1 sin response
        b = action  # velger det siste ordet i Host sin melding

        if action in bad_words: # Hvis action blir tatt ut i bad_words

            boolean_badWord = True
            boolean_goodWord = False

            return "{} responded: So {}ing it is then. I don't mind! \n".format(botName, b)

        elif action in good_words: # Hvis action blir tatt ut fra good_words

            boolean_goodWord = True
            boolean_badWord = False

            return "{} responded: I think {}ing sounds great! Awesome! \n".format(botName, b)


    elif bot_index == 1: #bot 2 sin response
        bot_index = 2

        if boolean_badWord: #Hvis action blir tatt ut i bad_words
            return "{} responded: {}ing seems horrible. And I wanted more choices! \n".format(botName, b)

        elif boolean_goodWord: #  Hvis action blir tatt ut fra good_words
            return "{} responded: {}ing seems great!\n".format(botName, b)

    elif bot_index == 2: #bot 3 sin response
        bot_index = 3

        if boolean_badWord: # Hvis action blir tatt ut i bad_words
            return "{} responded: Again with the {}ing! \n".format(botName, b)

        elif boolean_goodWord: #  Hvis action blir tatt ut fra good_words
            return "{} responded: Are you serious? {}ing is the last thing we need \n".format(botName, b)

    elif bot_index == 3:  # bot 4 sin response
        bot_index = 4

        if boolean_badWord:  # Hvis action blir tatt ut i bad_words
            return "{} responded: Yess, Time to {} \n".format(botName, b)

        elif boolean_goodWord:  #  Hvis action blir tatt ut fra good_words
            return "{} responded: Somebody suggested {}ing? Sure, I'm up for anything! \n".format(botName, b)


while True:
    try:
        server_msg = Socket.recv(500).decode()  # få host melding
        print(server_msg)  # print meldingene som blir broadcastet tilbake fra serveren fra de andre clientene

        splitt_String = server_msg.split()  # split string som vi får tilsent

        action_event = splitt_String[-1]  # velg ut det siste ordet i stringen
        action_event = action_event[:-1]  # starter med å se det siste ordet i stringen for å finne action_event - (good word or bad word)

        sender = splitt_String[0]  # sett stringen mottat fra server i index 0
        sender = sender[:-1]  # #ser det første ordet i stringen for å finne ut hvem som sendte meldingen - Admin

        resp = Client_bots(client_navn, action_event, sender)  # svar Server som sendte server_msg med Action_event
        Socket.send(resp.encode())  # send svar/rsponse fra botes igjennom socket til server som - bites

    except Exception as e: #avslutter clienten
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("you have been disconnected from the chat room -- Bye")
        break
