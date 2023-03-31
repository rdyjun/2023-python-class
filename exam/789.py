import random as r
import time as t



while True :
    slot = [0]*3
    b = True
    for k in range(3) :
        slot[k] = r.randint(7, 9)
        if b == True :
            if slot[k] != 7 :
                b = False
        print('%d ' % slot[k], end = '')
        t.sleep(0)
    print("\n")
    if b :
        print("잭팟이 터졌네요")
        break
