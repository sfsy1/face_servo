# rabbitmq installed using this link: https://gist.github.com/fahminurfadilah/05dace422366afb3c18078d260055a54
# to run this, type this in terminal $ python3.8 servo_control.py
import pika
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)


"""
RabbitMQ
"""
channel.queue_declare(queue='hello')


"""
raspberry pi 4 model B
servo model: SM-S2309S, 5V
"""

# duty goes from 36 - 99 @60hz PWM, maybe change PWM hz?
# angle goes from ...
def SetAngle(signal_pin, angle):
	duty = angle
	GPIO.output(signal_pin, True)
	pwm.ChangeDutyCycle(duty)
	sleep(0.3)
	GPIO.output(signal_pin, False)
	pwm.ChangeDutyCycle(0)


GPIO.setmode(GPIO.BOARD)
# signal (white wire) must be on PWM pins 32/33(refer to Pinout diagram)
signal_pin = 32 

while True:
	angle = input('Set angle: ')
	# Servo angle control
	GPIO.setup(signal_pin, GPIO.OUT)
	pwm=GPIO.PWM(signal_pin, 60)
	
	pwm.start(0)
	SetAngle(signal_pin, float(angle))
	pwm.stop()
	
	print("Pin{}: setting angle to {}".format(signal_pin, angle))



sleep(2)
pwm.stop()
GPIO.cleanup()
