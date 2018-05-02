from subprocess import call

commits = 3
filename = "delete"
extention = ".me"
pusher = "git push https://suarezluis:makemoney2903@github.com/suarezluis/gitCommiter"

def git():
    call(["git", "add", "."])
    call(["git", "commit", "-m",'"commiter auto"']) 
    call(["git", "push", "https://suarezluis:makemoney2903@github.com/suarezluis/gitCommiter"])
   




for i in range(1,commits):
    file = filename + str(i) + extention
    call(["touch", file])
    git()
    
call(["rm", "*.me"])

