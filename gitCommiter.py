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
    call(["clear"])
    call(["git", "add", "."])
    print("Added all files")
    print("================================================================")
    call(["git", "commit", "-m",'"commiter auto"']) 
    print("================================================================")
    print("Git commited! " + str(commited) + " / " + str(commits))
    print("================================================================")
    print("Pushing...")
    print("================================================================")
    ##call(["git", "push", pusher])
    print("================================================================")
    print("Commited!")
    print("Waiting 1 seconds")
    print("================================================================")
    sleep(1)




for i in range(1,commits+1):
    commited = i
    call(["rm", "*.me"])
    file = filename + str(i) + extention
    call(["touch", file])
    
    git()
    
call(["rm", "*.me"])
git()
call(["git", "push", pusher])
