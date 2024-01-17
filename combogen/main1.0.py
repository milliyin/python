import random
import string
import json
import time
try: 
    with open('first-names.json','r') as f:
        data=json.loads(f.read())
        # print(data)
except Exception as ex:
    print(f'Error: {str(ex)}')

print("""
██╗░░░██╗███████╗███╗░░██╗  ░█████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░  ██╗░░░░░██╗░██████╗████████╗
╚██╗░██╔╝██╔════╝████╗░██║  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗  ██║░░░░░██║██╔════╝╚══██╔══╝
░╚████╔╝░█████╗░░██╔██╗██║  ██║░░╚═╝██║░░██║██╔████╔██║██████╦╝██║░░██║  ██║░░░░░██║╚█████╗░░░░██║░░░
░░╚██╔╝░░██╔══╝░░██║╚████║  ██║░░██╗██║░░██║██║╚██╔╝██║██╔══██╗██║░░██║  ██║░░░░░██║░╚═══██╗░░░██║░░░
░░░██║░░░███████╗██║░╚███║  ╚█████╔╝╚█████╔╝██║░╚═╝░██║██████╦╝╚█████╔╝  ███████╗██║██████╔╝░░░██║░░░
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝  ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░░╚════╝░  ╚══════╝╚═╝╚═════╝░░░░╚═╝░░░

░██████╗░███████╗███╗░░██╗  ░░███╗░░░░░░█████╗░
██╔════╝░██╔════╝████╗░██║  ░████║░░░░░██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║  ██╔██║░░░░░██║░░██║
██║░░╚██╗██╔══╝░░██║╚████║  ╚═╝██║░░░░░██║░░██║
╚██████╔╝███████╗██║░╚███║  ███████╗██╗╚█████╔╝
░╚═════╝░╚══════╝╚═╝░░╚══╝  ╚══════╝╚═╝░╚════╝░
""")

acc = int(input("Enter the amount of account to generate:"))

start_time = time.time()
f = open("email_password.txt", 'w+')
lenght = 14
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
special = string.punctuation

mail = ['gmail.com','yahoo.com','hotmail.com']

all = upper + lower + num + special
for _ in range(acc):
    num = int(random.random()*len(data))
    name = data[num]
    temp = random.sample(all,lenght)
    password = "".join(temp)
    inmail = mail[int(random.random()*len(mail))]
    email = name + '@' + inmail
    ws = email + ':'+ password + '\n'
    f.write(ws)

end_time = time.time()
elapsed_time = end_time - start_time
succes = "Succelfully Gnerated: " + str(acc) +" with in " + str(round(elapsed_time,2)) + " seconds."
print(succes)
