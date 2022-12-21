# Imports
from machine import Pin, PWM
import time

# Set up the Buzzer pin as PWM
buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode

# Create our library of tone variables for "Among us drip"
A = 440
As = 466
B = 494
C = 523
Cs = 554
D = 587
Ds = 622
E = 659
F = 698
Fs = 740
G = 784
Gs = 830

# Create volume variable (Duty cycle)
volume = 10000

# Create our function with arguments
def playtone(note,vol,delay1,delay2):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay1)
    buzzer.duty_u16(0)
    time.sleep(delay2)
    
# Play the tune
playtone(D,volume,0.1,0.2)
playtone(F,volume,0.1,0.2)
playtone(G,volume,0.1,0.2) 
playtone(Gs,volume,0.1,0.2)
playtone(G,volume,0.1,0.2)
playtone(F,volume,0.1,0.2) 
playtone(D,volume,0.1,0.5)

playtone(C,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)
playtone(D,volume,0.1,0.5)

playtone(A,volume,0.1,0.2)
playtone(D,volume,0.1,0.5)

playtone(D,volume,0.1,0.2)
playtone(F,volume,0.1,0.2)
playtone(G,volume,0.1,0.2)
playtone(Gs,volume,0.1,0.2)

playtone(G,volume,0.1,0.2)
playtone(F,volume,0.1,0.2)
playtone(Gs,volume,0.1,0.5)

playtone(Gs,volume,0.1,0.1)
playtone(G,volume,0.1,0.1)
playtone(F,volume,0.1,0.1)
playtone(Gs,volume,0.1,0.1)
playtone(G,volume,0.1,0.1)
playtone(F,volume,0.1,0.1)

playtone(D,volume,0.5,0.5)


# Duty to 0 to turn the buzzer off
buzzer.duty_u16(0)