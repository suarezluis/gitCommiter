from subprocess import call

commits = 2
filename = "gitter.txt"
for i in range(1,commits):
    f= open(filename,"w+")
    f.close()
    call(["git", "add", "."])
    call(["git", "commit", "-m",'"commiter auto"'])
    call(["git", "push"])
    call(["makemoney"])
    
