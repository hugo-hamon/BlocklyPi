from adafruit_servokit import ServoKit
from time import sleep
from gpiozero import Motor
import os
import random
from gtts import gTTS
import pygame

kit = None


def francaster_speak(audio_string):
    print(audio_string)
    pygame.mixer.init()
    tts = gTTS(text=audio_string, lang='fr')
    r = random.randint(1, 1000)
    audio_file = "file-" + str(r) + ".mp3"
    tts.save(audio_file)
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    os.remove(audio_file)


# set the range of motion for each motor. The index of the list is the motor's number
motors_range = [(0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 170), (0, 180),
                (0, 135), (0, 120), (0, 180), (45, 180), (0, 120), (0, 180), (35, 140)]


def init():
    global kit
    kit = ServoKit(channels=16)
    sleep(.1)
    kit.servo[0].angle = 180
    sleep(.1)
    kit.servo[1].angle = 90
    sleep(.1)
    kit.servo[2].angle = 180
    sleep(.1)
    kit.servo[3].angle = 90
    sleep(.1)
    kit.servo[4].angle = 90
    sleep(.1)
    kit.servo[5].angle = 0
    sleep(.1)
    kit.servo[6].angle = 90
    sleep(.1)
    kit.servo[7].angle = 0
    sleep(.1)
    kit.servo[8].angle = 90
    sleep(.1)
    kit.servo[9].angle = 0
    sleep(.1)
    kit.servo[10].angle = 45
    sleep(.1)
    kit.servo[11].angle = 90
    sleep(.1)
    kit.servo[12].angle = 180
    sleep(.1)
    kit.servo[13].angle = 75
    sleep(.1)
    kit.servo[14].angle = 90
    sleep(.1)
    kit.servo[15].angle = 90


def verify_drange_min(motor, angle):
    mi, ma = motors_range[motor]
    return mi > angle


def verify_drange_max(motor, angle):
    mi, ma = motors_range[motor]
    return ma < angle


def verify_range(motor, angle):
    mi, ma = motors_range[motor]
    return mi <= angle and angle <= ma


def set(motor, angle):
    motor = int(motor)
    angle = int(angle)
    mi, ma = motors_range[motor]
    if verify_range(motor, angle):
        kit.servo[motor].angle = angle
    else:
        if (verify_drange_min(motor, angle)):
            kit.servo[motor].angle = int(mi)
        if (verify_drange_max(motor, angle)):
            kit.servo[motor].angle = int(ma)
    print(str(motor) + " " + str(mi) + " " + str(ma) + " " + str(kit.servo[int(motor)].angle))


def set2(motor, angle):
    x = kit.servo[int(motor)].angle + angle
    mi, ma = motors_range[motor]
    if (verify_range(motor, x)):
        kit.servo[int(motor)].angle += int(angle)
    else:

        if (verify_drange_min(motor, x)):
            kit.servo[int(motor)].angle = int(mi)
        if (verify_drange_max(motor, x)):
            kit.servo[int(motor)].angle = int(ma)
    print(str(motor) + " " + str(mi) + " " + str(ma) + " " + str(kit.servo[int(motor)].angle))


def delay(temps):
    sleep(float(temps))
    print("motor  posé" + temps)


def marche(ps):
    for _ in range(0, ps - 1):
        kit.servo[3].angle = 60
        sleep(.1)
        kit.servo[4].angle = 60
        sleep(.1)
        kit.servo[8].angle = 120
        sleep(.1)
        kit.servo[11].angle = 120
        sleep(0.5)
        kit.servo[3].angle = 120
        sleep(.1)
        kit.servo[4].angle = 120
        sleep(.1)
        kit.servo[8].angle = 60
        sleep(.1)
        kit.servo[11].angle = 60
        sleep(.5)
    init()


def do_hi(ps):
    kit.servo[5].angle = 130
    sleep(.1)
    kit.servo[6].angle = 180
    sleep(.1)
    for _ in range(0, ps - 1):
        kit.servo[7].angle = 90
        sleep(0.5)
        kit.servo[7].angle = 0
        sleep(0.5)
    init()


def marche_gn_cd(ps):
    kit.servo[2].angle = 170
    kit.servo[5].angle = 10
    for _ in range(0, ps - 1):
        kit.servo[0].angle = 150
        sleep(0.2)
        kit.servo[3].angle = 90
        sleep(0.2)
        kit.servo[4].angle = 60
        sleep(0.2)
        kit.servo[7].angle = 0
        sleep(0.2)
        kit.servo[8].angle = 100
        sleep(0.2)
        kit.servo[9].angle = 60
        sleep(0.2)
        kit.servo[11].angle = 120
        sleep(0.2)
        kit.servo[12].angle = 180
        sleep(0.2)
        kit.servo[0].angle = 180
        sleep(0.2)
        kit.servo[3].angle = 120
        sleep(0.2)
        kit.servo[4].angle = 90
        sleep(0.2)
        kit.servo[7].angle = 30
        sleep(0.2)
        kit.servo[8].angle = 50
        sleep(0.2)
        kit.servo[9].angle = 0
        sleep(0.2)
        kit.servo[11].angle = 80
        sleep(0.2)
        kit.servo[12].angle = 120
        sleep(0.2)
    init()


def say_no():
    for _ in range(0, 2):
        sleep(.5)
        kit.servo[14].angle = 120
        sleep(.5)
        kit.servo[14].angle = 60
    init()


def say_yes():
    for _ in range(0, 2):
        sleep(.5)
        kit.servo[15].angle = 45
        sleep(.5)
        kit.servo[15].angle = 90
    init()


def motor_dc(speed=1):
    moteur = Motor(pinA, pinB)
    moteur.forward(speed)


def motor_dc_backward(speed=1):
    moteur = Motor(pinA, pinB)
    moteur.backward(speed)


def motor_dc_reverse(speed=1):
    moteur = Motor(pinA, pinB)
    moteur.reverse(speed)


def motor_dc_stop():
    moteur = Motor(pinA, pinB)
    moteur.stop()
