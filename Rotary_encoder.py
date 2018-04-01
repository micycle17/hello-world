# taken from (and then altered) :
#http://www.ozeki.hu/index.php?owpn=3054


import RPi.GPIO as GPIO
from time import sleep
 
counter = 10
 
Enc_A = 26
Enc_B = 19
Enc_Switch = 13

ControlPin = [26,19,13,6]

Seq = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1]]
 
 def init_enc():
    print "Rotary Encoder Test Program"
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Enc_A, GPIO.IN)
    GPIO.setup(Enc_B, GPIO.IN)
    GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=10)
    # in the event of a leading edge on line A the code jumps to rotation_decode function
    return
 
 
def init_stepper():
    for pin in ControlPin:
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin,0)
   return
  
  
def stepper_rotation(direction):
    if (direction==1):
      for i in range(17):
        for halfstep in range(8):
          for pin in range(4):
            GPIO.output(ControlPin[pin], seq[halfstep] [pin])
          time.sleep(.001)
    elif (direction=-1):
       for i in range(17):
        for halfstep in range(8):
          for pin in range(4):
            GPIO.output(ControlPin[pin], seq[halfstep] [pin])
          time.sleep(.001)
    return
  
 
def rotation_decode(Enc_A):
    global counter
    sleep(0.002)
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)
 
    if (Switch_A == 1) and (Switch_B == 0):
        counter += 1
        print "direction -> ", counter
        while Switch_B == 0:
            Switch_B = GPIO.input(Enc_B)
        while Switch_B == 1:
            Switch_B = GPIO.input(Enc_B)
        stepper_rotation(1)
        return
 
    elif (Switch_A == 1) and (Switch_B == 1):
        counter -= 1
        print "direction <- ", counter
        while Switch_A == 1:
            Switch_A = GPIO.input(Enc_A)
        stepper_rotation(-1)
        return
    else:
        return
 
 
 
 
 
def main():
    try:
        init_enc() ### calling rotation not required as the edge triggering does that for us
        init_stepper()
        while True :
            sleep(1)
 
    except KeyboardInterrupt:
        GPIO.cleanup()
 
if __name__ == '__main__':
    main()
