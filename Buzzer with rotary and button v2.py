import machine
import time
from machine import ADC
from time import sleep
from machine import Pin
from gpio_lcd import GpioLcd
#GPIO_LCD hentes fra Kevin's Github


def tone(pin, frequency, duration):#Definere vores tone function, men pin på buzzer, frekvens og hvor tit den holder pause i milisekunder
    pin.freq(frequency) # Sætter frekvensen som er defineret af vores potentiumeter
    pin.duty(512) # max bit duty
    time.sleep_ms(duration) # pause længe i milliseconds
    pin.duty(0) # Definere hvis man sætter buzzer duty til 0 slukker den lyd

buzzer = machine.PWM(machine.Pin(14)) # Buzzer definition
adcpin = 34 #Pin på potentometer
pot = ADC(adcpin) #Adc Value er vores analog value fra potentiometer 
buzzer.duty(0) #Slukker buzzeren fra start til man begynder at rode med encoder

BUTTON1_PIN = 4 #bruges til at skifte tonen på buzzeren
pb1 = Pin(BUTTON1_PIN, Pin.IN) # definere knappen

lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),#Vores pin setup til skærmen
              d4_pin=Pin(33), d5_pin=Pin(32), d6_pin=Pin(21), d7_pin=Pin(22),
              num_lines=4, num_columns=20) #Max linjer på skærmen, samt maks column af karaktere

while True:
    first = pb1.value()
    if first == 1:
        buzzer.duty(0) #Starter ud med ingen lyd
        adc_value = pot.read_u16() #Læser value fra pot. meter
        turn =(10000/81000)*adc_value #Omregner pot. meter value fra 80k+ til maks 8100 da maks frekvensen på buzzeren er 40.000 hz
        sound = int(round(turn,2))#Laver vores værdi fra den analog pot. meter om til en int værdi
        sound1 = (sound + 1)#Tillæger +1 til vores analog værdi, således at koden ikke crasher når man kører buzzer til 0, da minimums frekvense er 1Hz
        skaerm= str(sound1) #Skærm, printer frekvensen på skærmen
        lcd.move_to(1, 1) #Flytter det ned i midten af skærmen
        lcd.putstr(skaerm) #
        print(sound1)#Printer værdien fra pot. meter i Shell, så man kan følge med i frekvens på buzzer
        tone(buzzer, sound1, 100)#Tone definitionen på buzzer, vi vælger at vores 'buzzer' skal afgive lyd, at 'sound1' er vores frekvens og 100ms er hvor tit den skal 'opdatere' lyd
        sleep(0.1)#Sleep til at repeat koden
    elif first == 0:
        buzzer.duty(0) #Starter ud med ingen lyd
        adc_value = pot.read_u16() #Læser value fra pot. meter
        turn =(10000/81000)*adc_value #Omregner pot. meter value fra 80k+ til maks 8100 da maks frekvensen på buzzeren er 40.000 hz
        sound = int(round(turn,2))#Laver vores værdi fra den analog pot. meter om til en int værdi
        sound1 = (sound + 100)#Tillæger +100 til vores analog værdi, ved knap tryk
        skaerm = str(sound1)
        lcd.move_to(1, 1)
        lcd.putstr(skaerm)
        print(sound1)#Printer værdien fra pot. meter i Shell, så man kan følge med i frekvens på buzzer
        tone(buzzer, sound1, 100)#Tone definitionen på buzzer, vi vælger at vores 'buzzer' skal afgive lyd, at 'sound1' er vores frekvens og 100ms er hvor tit den skal 'opdatere' lyd
        sleep(0.1)#Sleep til at repeat koden
        
