from subprocess import call

commits = 2
filename = "gitter.txt"
pusher = "git pull https://suarezluis:makemoney2903@github.com/suarezluis/gitCommiter/ master"
for i in range(1,commits):
    f= open(filename,"w+")
    f.close()
    call(["git", "add", "."])
    call(["git", "commit", "-m",'"commiter auto"'])
    call(["git", "push"])
    call(pusher)
    
