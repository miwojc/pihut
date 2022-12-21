from machine import  Pin

import time


red_ongus = Pin(18, Pin.OUT)

amber_bugus = Pin(19, Pin.OUT)

green_among = Pin(20, Pin.OUT)


# loop code

counter1 = 0

while counter1 < 5:

    counter = 1

    while counter < 5:
      
        red_ongus.value(1)
        amber_bugus.value(0)
        green_among.value(0)

        print(counter)
        time.sleep(0.5)
        
        red_ongus.value(0)
        amber_bugus.value(1)
        green_among.value(0)
        
        print(counter)
        time.sleep(0.5)
        
        red_ongus.value(0)
        amber_bugus.value(0)
        green_among.value(1)
        
        print(counter)
        time.sleep(0.5)

        counter=counter+1

    counter=0

    while counter < 5:

        red_ongus.value(1)
        amber_bugus.value(1)
        green_among.value(1)

        time.sleep(0.5)

        red_ongus.value(0)
        amber_bugus.value(0)
        green_among.value(0)

        time.sleep(0.5)

        counter=counter+1

    counter1+=1