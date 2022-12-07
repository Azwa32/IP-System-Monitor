import os


def check_ip():
    # declare ip object
    ip = []

    # open text file and add each line to ip object set to False
    with open('ip.txt') as txt:    
        for line in txt:
            x = line[:-1]
            ip.append([x, False])


    # check each line of ip and see if they are online
    for i in ip:
        response = os.system("ping -n 1 " + i[0])

        # initialise each ip to False
        i[1] = False

        # process action for ip address if found online or not
        if response == 0:
            i[1] = True

            # update database with state of IP
        #    print(i[0], "is up")
        #else:
        #    print(i[0], "is down")

    
    # print result to text file
    # create result object to print
    result = []
    for p in ip:
        line = '%s %s' % (p[0], p[1])
        result.append(line)

    # print out result
    for line in result:
        print(line)

    # open file and overwrite contents, write result to file, close file
    with open("ip_result.txt", "w+") as ip_result:
        
        #write elements of list
        for line in result:
            ip_result.write('%s\n' %line)
    
    ip_result.close()

    # run function recursively
    check_ip()

    
# run program on startup
check_ip()
