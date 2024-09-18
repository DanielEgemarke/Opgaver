from machine import Pin, PWM
from time import sleep
from time import sleep_ms

BUZZER_PIN = 14
buzzer_pin = Pin(BUZZER_PIN, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin, duty=0)
#Tone Variabler

pause = int(1.3) # Pausen på 1.3 gange melodiens spilletid bliver konveteret fra en float til en integer
speed = int(1.8) #Skibidi

def buzzer(pwm_object, frequency, tone_duration):#Definere vores tone function, men pin på buzzer, frekvens og hvor tit den holder pause i milisekunder
    pwm_object.duty(512) # Sætter frekvensen som er defineret af vores potentiumeter
    pwm_object.freq(frequency) # Bruges ikke
    sleep_ms(tone_duration * speed) # pause længe i milliseconds
    pwm_object.duty(0)
    sleep_ms(tone_duration * pause)
    
A5 = 932
C5 = 523
C6 = 1046
G5 = 784
GH5 = 831
E5 = 659
F5 = 698
FH5 = 740
CH5 = 554
CH6 = 1109

BUTTON1_PIN = 4 #Bruges ikke, kan evt kodes ind til at kunne 'tænde' buzzeren
pb1 = Pin(BUTTON1_PIN, Pin.IN) # Se ovenfor

while True:
    buzzer(buzzer_pwm, C5, 80)
    buzzer(buzzer_pwm, C5, 80)
    buzzer(buzzer_pwm, C5, 80)
    buzzer(buzzer_pwm, C5, 80)
    buzzer(buzzer_pwm, E5, 80)
    buzzer(buzzer_pwm, C6, 80)
    buzzer(buzzer_pwm, G5, 80)
    buzzer(buzzer_pwm, E5, 80)
    buzzer(buzzer_pwm, CH5, 80)
    buzzer(buzzer_pwm, CH6, 80)
    buzzer(buzzer_pwm, CH5, 80)
    buzzer(buzzer_pwm, F5, 80)
    buzzer(buzzer_pwm, CH6, 80)
    buzzer(buzzer_pwm, GH5, 80)
    buzzer(buzzer_pwm, F5, 80)
    buzzer(buzzer_pwm, C5, 80)
    buzzer(buzzer_pwm, C6, 80)
    buzzer(buzzer_pwm, G5, 80)
    buzzer(buzzer_pwm, E5, 80)
    buzzer(buzzer_pwm, C6, 80)
    buzzer(buzzer_pwm, G5, 80)
    buzzer(buzzer_pwm, E5, 80)
    buzzer(buzzer_pwm, G5, 80)
    buzzer(buzzer_pwm, F5, 80)
    buzzer(buzzer_pwm, GH5, 80)  
    buzzer(buzzer_pwm, A5, 40)
    buzzer(buzzer_pwm, GH5, 80)
    buzzer(buzzer_pwm, A5, 40)
    buzzer(buzzer_pwm, C6, 140)
    buzzer(buzzer_pwm, C6, 140)
