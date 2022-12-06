import os

# initialise array with ip addresses and state
ip = [[ "192.168.105.161" , False] , [ "192.168.105.186", False ]]

# check ip's if they are online
for i in ip:
    response = os.system("ping -n 1 " + i[0])

    # initialise each ip to False
    i[1] = False

    # process action for ip address if found online or not
    if response == 0:
        i[1] = True
        print(i[0], "is up")
    else:
        print(i[0], "is down")
