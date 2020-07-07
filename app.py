import os






usr_input = int(input("Minutes untill pc shutdown: "))


os.popen("python3 func.py {} &".format(usr_input))

print('[+]done now you can close this window'.upper())
