from subprocess import call
from time import sleep
user = "suarezluis"
password = "makemoney2903"
commits = 100
filename = "delete"
extention = ".me"
pusher = "https://"+user+":"+password+"@github.com/suarezluis/gitCommiter"

def git():
    call(["git", "add", "."])
    print("Added all files")
    print("================================================================")
    call(["git", "commit", "-m",'"commiter auto"']) 
    print("================================================================")
    print("Git commited")
    print("================================================================")
    print("Pushing...")
    print("================================================================")
    call(["git", "push", pusher])
    print("================================================================")
    print("Pushed!")
    print("Waiting 3 seconds")
    print("================================================================")
    sleep(0)




for i in range(0,commits):
    call(["rm", "*.me"])
    file = filename + str(i) + extention
    call(["touch", file])
    git()
    
call(["rm", "*.me"])
git()
