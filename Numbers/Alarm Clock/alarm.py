import sys
import time


def alarm(n):
    for i in range(n):
        print('\a')
        time.sleep(0.2)
    print()
        

def main():
    global input
    try: input = raw_input
    except NameError: pass
    seconds = int(input("seconds:"))
    time.sleep(seconds)
    alarm(20)
    
    return 0

if __name__=="__main__":
    status = main()
    sys.exit(status)