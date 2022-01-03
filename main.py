import subprocess
f = open("state", "r")
global STATE
STATE = f.read()
f.close()


def togglenotification():
    global STATE
    if STATE == 'unpaused':
        subprocess.call("./pause.sh")
        f = open("state", "w")
        f.write("paused")
        f.close()
        STATE = 'paused'

    elif STATE == 'paused':
        subprocess.call("./unpause.sh")
        f = open("state", "w")
        f.write("unpaused")
        f.close()
        STATE = 'unpaused'


if __name__ == '__main__':
    togglenotification()
    print(STATE)
