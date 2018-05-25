from subprocess import call
from time import sleep
user = input("User name: ")
password = input("Password: ")
commits = int(input("Number of Commits: "))
filename = "delete"
extention = ".me"
pusher = "https://"+user+":"+password+"@github.com/suarezluis/gitCommiter"
commited = 0

def git():
    call(["git", "add", "."])
    print("Added all files")
    print("================================================================")
    call(["git", "commit", "-m",'"commiter auto"']) 
    print("================================================================")
    print("Git commited" + str(commited))
    print("================================================================")
    print("Pushing...")
    print("================================================================")
    call(["git", "push", pusher])
    print("================================================================")
    print("Pushed!")
    print("Waiting 3 seconds")
    print("================================================================")
    sleep(0)




for i in range(1,commits+1):
    commited = i
    call(["rm", "*.me"])
    file = filename + str(i) + extention
    call(["touch", file])
    call(["clear"])
    git()
    
call(["rm", "*.me"])
git()
