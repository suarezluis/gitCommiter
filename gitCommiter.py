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
    print("Programmed by Luis Suarez May 2018")
    print("================================================================")
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
    sleep(0)




for i in range(1,commits):
    commited = i
    call(["rm", "*.me"])
    file = filename + str(i) + extention
    call(["touch", file])
    
    git()
    
call(["rm", "*.me"])
git()
call(["git", "push", pusher])
