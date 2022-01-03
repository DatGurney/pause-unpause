import os
import subprocess

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def unpause():
    f = open("state", "w")
    f.write("unpaused")
    f.close()
    subprocess.call("./unpause.sh")


if __name__ == '__main__':
    unpause()
