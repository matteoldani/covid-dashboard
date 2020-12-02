import os
import signal


f = open("ipid.txt", "r");

for x in f:
    os.kill(int(x), signal.SIGSTOP)

    print("done")
