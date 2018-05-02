from subprocess import call

commits = 3
filename = "gitter"
pusher = "git push https://suarezluis:makemoney2903@github.com/suarezluis/gitCommiter"

def git():
    call(["git", "add", "."])
    call(["git", "commit", "-m",'"commiter auto"']) 
    call(["git", "push", "https://suarezluis:makemoney2903@github.com/suarezluis/gitCommiter"])
 




for i in range(1,commits):
    f= open(filename + "a","w+")
    f.close()
    git()   
