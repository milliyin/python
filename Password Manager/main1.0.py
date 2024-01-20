from cryptography.fernet import Fernet
import json
from prettytable import PrettyTable
import random
import string

print("""
$$\     $$\                         $$$$$$$\                                     $$\      $$\                                                             
\$$\   $$  |                        $$  __$$\                                    $$$\    $$$ |                                                            
 \$$\ $$  /$$$$$$\  $$$$$$$\        $$ |  $$ |$$$$$$\   $$$$$$$\  $$$$$$$\       $$$$\  $$$$ | $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  
  \$$$$  /$$  __$$\ $$  __$$\       $$$$$$$  |\____$$\ $$  _____|$$  _____|      $$\$$\$$ $$ | \____$$\ $$  __$$\  \____$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
   \$$  / $$$$$$$$ |$$ |  $$ |      $$  ____/ $$$$$$$ |\$$$$$$\  \$$$$$$\        $$ \$$$  $$ | $$$$$$$ |$$ |  $$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
    $$ |  $$   ____|$$ |  $$ |      $$ |     $$  __$$ | \____$$\  \____$$\       $$ |\$  /$$ |$$  __$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$   ____|$$ |      
    $$ |  \$$$$$$$\ $$ |  $$ |      $$ |     \$$$$$$$ |$$$$$$$  |$$$$$$$  |      $$ | \_/ $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ $$ |      
    \__|   \_______|\__|  \__|      \__|      \_______|\_______/ \_______/       \__|     \__| \_______|\__|  \__| \_______| \____$$ | \_______|\__|      
                                                                                                                            $$\   $$ |                    
                                                                                                                            \$$$$$$  |                    
                                                                                                                             \______/                     
""")
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
special = string.punctuation
all = upper + lower + num + special
try:
    with open('config.json','r') as f:
        config=json.loads(f.read())
        # print(data)
except Exception as ex:
        print(f'Error: {str(ex)}')

try:
    with open('database.json','r') as f:
        data=json.loads(f.read())
        # print(data)
except Exception as ex:
        print(f'Error: {str(ex)}')
lastnum = 0
for obj in data:
        lastnum = obj["sr"]

def addtodata(note,username,password,data):

    note = str(note)
    username = str(username)
    password = str(password)
    global lastnum
    lastnum=lastnum+1
    data.append({
    "sr": lastnum,
    "note": note,
    "username": username,
    "password": password
    })
def updatetodata(update,sr,updateto,data):
    updateto = str(updateto)
    for obj in data:
        if obj["sr"] == sr:
                obj[update] = updateto
def deletetodata(sr,data):
    global lastnum
    for i in range(len(data)):
        if data[i]["sr"] == sr:
            data.pop(i)
            break
    for i in range(len(data)):
        data[i]["sr"] = i
        if i == range(len(data)):
            lastnum = i
def showdata(data):
    table = PrettyTable()
    table.field_names = ["Sr",  "Username", "Password","Note"]
    for item in data:
        table.add_row([item["sr"], item["username"], item["password"],item["note"]])
    print(table)
    
def savedata(data):
    with open("database.json", 'w') as json_file:
        json.dump(data, json_file, 
                    indent=4,  
                       separators=(',',': '))   
               
pin = int(config[0]["pin"])
menu = "\n\n[1] Show Password\n[2] Add\n[3] Update\n[4] Delete\n[x] Quite"
while True:
    print("Enter the Pin")
    inpin = input(">>")
    if int(inpin) == pin:
        ft = Fernet(config[0]["key"])
        break
    else:
        print("WRONG PIN")    


for obj in data:
    enc = obj["password"]
    enc = enc[2:-1]
    # print(enc)
    de = str(ft.decrypt(enc))
    obj["password"] = de[2:-1]


while True:
    print(menu)
    m = input(">>")
    print("---------------------")
    if m == 'x':
        break
    elif m == '1':
        showdata(data)
    elif m == '2':
        username = input("Username:")
        print("Generate a password? yes/no")
        asking = input(">")
        if asking == "yes":
            lenght = 17
            temp = random.sample(all,lenght)
            password = "".join(temp) 
        else:
            password = input("Password:")
        note = input("Note:")
        addtodata(note,username,password,data)
    elif m =='3':
        sr = int(input("Sr NO. to update:"))
        update = input("username | password | note:")
        if update == "password":
            print("Generate a password? yes/no")
            asking = input(">")
            if asking == "yes":
                lenght = 17
                temp = random.sample(all,lenght)
                updateto = "".join(temp) 
            else:
                updateto = input("to:") 
        else:
            updateto = input("to:")        
        updatetodata(update,sr,updateto,data)   
    elif m == '4':
        sr = int(input("Sr NO. to Delete:"))
        confirm = input("Are you sure? 1/0: ")
        if confirm == '1':
            deletetodata(sr,data)
        else:
            continue

for obj in data:
    token = ft.encrypt(bytes(obj["password"], encoding='utf-8'))
    obj["password"] = str(token)
savedata(data)
