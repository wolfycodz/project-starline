import os
os.system("python3 pkgdown.py")
print("version 0.03..")
print("Ustore connect...")

print("1:turbowarp or 2:scratch")
compiler = input()

if compiler == 1:
    print("turbowarp mode")
else:
    print("please enter your username, it so you can connect your os to the ustore, it will be saved for future reference.")
    username = input()
    print(username + ", enter your password")
    password = input()
    os.system("cls")




    import scratchattach as scratch3 # type: ignore
    print("imported scratch attach")

    session = scratch3.login(username, password)
    print("logged in to " + username )

    print("finding app-codes.txt(not implmented)")

    print("please enter your projects id (eg 12345678)")
    projectid = input()
    conn = session.connect_cloud(projectid)
    print("connected to scratch.mit.edu/projects/" + projectid )