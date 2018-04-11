import serial
import RPi.GPIO as GPIO
import time
from ubidots import ApiClient

api = ApiClient(token='<su token de cuenta Ubidots>')
ser = serial.Serial("/dev/ttyACM0",baudrate=9600,timeout=2.0);

RPi_pinled = 11;

ubi_pot = api.get_variable('<ID de su variable para el potenciomentro>')
ubi_led_rpi = api.get_variable('<ID de su variable para el led de raspberry>')
ubi_led_ard = api.get_variable('<ID de su variable para el led arduino>')

GPIO.setmode(GPIO.BOARD);
GPIO.setup(RPi_pinled,GPIO.OUT);
while True:
	time.sleep(2)
	led_rpi_st = ubi_led_rpi.get_values(1);
	if led_rpi_st[0]['value']:
            print "encendido led RPi"
            GPIO.output(RPi_pinled,GPIO.HIGH)
        else:
            print "apagado led RPi"
            GPIO.output(RPi_pinled,GPIO.LOW)
        led_ard_st = ubi_led_ard.get_values(1)
        if led_ard_st[0]['value']:
            print "encendido led arduino"
            ser.write('A')
	else:
            print "apagado led arduino"
            ser.write('B')
	ser.reset_input_buffer();
	ser.write('C')
	sen = ser.readline();
	ubi_pot.save_value({'value': int(sen)});
	print ("lectura arduino pin A0: "+ sen)
	print "loop..."
