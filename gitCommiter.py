from subprocess import call
from time import sleep

commits = 16
filename = "delete"
extention = ".me"
pusher = "git push https://suarezluis:makemoney2903@github.com/suarezluis/gitCommiter"

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
    call(["git", "push", "https://suarezluis:makemoney2903@github.com/suarezluis/gitCommiter"])
    print("================================================================")
    print("Pushed!")
    print("Waiting 3 seconds")
    print("================================================================")
    sleep(3)




for i in range(0,commits):
    file = filename + str(i) + extention
    call(["touch", file])
    git()
    
call(["rm", "*.me"])
git()
