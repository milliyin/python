import os
import time
import json
try:
    with open('config.json','r') as f:
        config=json.loads(f.read())
except Exception as ex:
        print(f'Error: {str(ex)}')
version = 1
os.chdir(config["file"]) 
cwd = os.getcwd() 
print("Current working directory:", cwd)
os.system("git init")

while(1):
    check = os.system("git status")
    print(check)
    check = os.system("git lfs track *")
    os.system("git add .")
    os.system(f"""git commit -m {version} """)
    os.system(f"""git branch {version} """)
    if(version == 1):
        repo = config["git-repo"]
        os.system(f"git remote add origin {repo}")
    u_responce = os.system(f"git push -u origin {version}")
    version = version + 1
    time.sleep(int(config["time"]))
