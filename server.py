#server.py
import socket
import random
import time


print("\nThe IP adress is by defult set to 'localhost' on the server side")
Host = "localhost"

Clients = []
recv_message = []

try:

     #port = 4242
     print("\nType in a preferred port number here in the command line, to start running the Chat room on this port: ( Eks: 4242 ) ")
     port = int(input("Inputt port number here: "))

except Exception as e:
    time.sleep(1)
    print("\nERROR! - A port number can only contain numbers \n(Run the server again)\n")

def server_broadcast(Client_message, client_index):
    if client_index:
        for bots_msg in Clients: # den clienten vi er ved i start

            if bots_msg != client_index: #Hvis meldingen som har blitt motatt ikke befinner seg i de andre botne

                bots_msg.send(Client_message.encode()) #sender ut meldingen vi mottok fra clienten vi er på nå til de andre clientene

            else:  #boten som sendte sin melding vil ikke for denne tilbake, men serveren vil ha motatt den

                bots_msg.send("This clients response has been sendt to the server\n".encode()) #motatt melding

    else: # broadcaster reseterende meldinger som er motatt i serveren tilbake til alle clienter
        for bots_msg in Clients:
            bots_msg.send(Client_message.encode())

def server():
    global Clients
    global recv_message
    global bots

#dette er greit
    action_event = random.choice(["hug", "play", "eat", "shop", "yell", "steal", "fight"])

    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # generell kode for å sette opp Socket
    Socket.bind((Host, port)) # binder socket til adresse - localhost og valfrlitt port nummer
    Socket.listen() # vente på kobling til clienter - da 4 boter

    print("\nThe TCP server chat rom is opperating on port number {}".format(port))
    print("Now the server is waiting to connect to the clients")

    print("\n(REMEMBER TO START THE CLIENTS NOW!!!) - NB! Start each new client in paralell:")
    print("0/4 bots has connected to the chat room at this point \n")

    while True:

        # Connection = Socket.accept() # går ikke
        # address = Socket.accept() ¤ går ikke
        Connection , address  = Socket.accept()  # gikk fordi scoket tar imot '2 inputs'
        Clients.append(Connection) # legger til koblingen som vi mottok fra socket til å finne ut hvor hvilkn client som blir koblet til serveren

        client_names = Connection.recv(500).decode() # Får tilsendt det definerte 'navnet som ble satt for botten' fra client siden
        print("{} - {} - {} / 4 bots connected ".format(client_names, address, len(Clients))) #printer ut bot_navn, (ip adresse og port number), samt rekkefølgen av boter som blir koblet til først og sist



        connected_bots = "\nBot: {} has been sucessfully connected\n{}/4 bots have been connected soo far\n \nwaiting for the rest of the bots to be connected before starting the chat room....".format(client_names, len(Clients))

        Connection.send(connected_bots.encode())

        if len(Clients) == 4: # if all bots are connected

            print("\n{}/4 bots have connected successfully".format(len(Clients))) # får et nummer på hvor mange clienter/boter vi har
            print("The chat rom will noe proceed to run with {}/4 bots fully connected\n".format(len(Clients)))

            time.sleep(1)
            server_broadcast("\nBatman: Do you want to {}?".format(action_event), "") #sending to every bot that is connected

            print("A new suggestion!")
            print("Batman sugessted: Do you want to {}? \n".format(action_event))



            bot_index = 0 # starter på index 0 of forsetter videre for hver bot slik at vi mottar alle meldingene fra den som connected først til sist

            for bots in range(4): #loop over alle 4 bots
                #bot_index = 0 # printer kun ut svar med bot1 som sender selv om vi får meldinene til de andre botene
                if bot_index > 3:
                    time.sleep(2)
                    bot_index = 0 # stopper loopen etter at vi har fått loppet over alle 4 boter
                time.sleep(1.2)

                for C in range(len(Clients)):  # definer client nummer med en index av C
                  Client_msg = (Clients[C].recv(500).decode()) # get message from alle clients basert på hvilken bot som sender melding først og decoder dete fra bites til leselig tekst
                  recv_message.append(Client_msg) # vi bruker her index C for å holde styr på hvilken bot det er som sender melding først til sist
                time.sleep(0.7)

                print(recv_message[bot_index]) #printer alle meldingene fra botene i serveren etter at de har blitt motatt
                server_broadcast(recv_message[bot_index], Clients[bot_index]) # Broadcastet alle meldingene som har blitt motatt av serveren tilbake til clientene med untakk av den som sendte meldingen
                time.sleep(0.3)
                recv_message.clear() # clearer den motatte meldingen i for loopen fra den første som sendte meldingen bot1/index0 å går videre til å bli neste bot
                bot_index+=1 # øker indeksen for å definere hvilken bot sin melding vi mottar for hver itterasjon


            Socket.close() #avslutter socket

            end = str(input("\nThe clients have automatically been diconnected\nInput ( 'end' ) into the terminal to end the Chat rom: ")) #Avslutter chat rommet fra serveren sin side

            if end == "end": #avslutte serveren
                time.sleep(1)
                print("\nThe chat room has been disconnected sucesfully")
                exit()

            else:
                print("\nERROR! you did not disconnect from the server in the proper way!!!")
                print("REMEMBER TO TYPE 'end' into the terminal and press enter to end the Chat room in the 'correct way' next time\n")
                exit()



server()
