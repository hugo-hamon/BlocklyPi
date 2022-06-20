import time
from time import sleep
from robotMotor import RobotMotor
from francasterSpeech import francaster_speak
import speech_recognition as sr



# set of constants used to replace the motor numbers by more meaningful names
LEFT_ELBOW = RobotMotor(0, 0, 180)     #coude gauche
LEFT_SHOULDER_ABDUCTOR = RobotMotor(1, 0, 180)    #rotation bras gauche
LEFT_SHOULDER_ROTATOR = RobotMotor(2, 0, 160)         #epaule gauche
LEFT_SHOULDER_FLEXOR = RobotMotor(3, 0, 180)     #rotation epaule gauche
RIGHT_SHOULDER_FLEXOR = RobotMotor(4, 0, 180)     #rotation epaule droite
RIGHT_SHOULDER_ABDUCTOR = RobotMotor(5, 0, 180)     #rotation bras droit
RIGHT_SHOULDER_ROTATOR = RobotMotor(6, 0, 180)     #epaule droite
RIGHT_ELBOW = RobotMotor(7, 0, 170)    #coude droit
LEFT_HIP = RobotMotor(8, 0, 180)   #hanche gauche
LEFT_KNEE = RobotMotor(9, 0, 135)   #genou gauche
LEFT_ANKLE = RobotMotor(10, 0, 120)    #chevile gauche
RIGHT_HIP = RobotMotor(11, 0, 180)   #hanche droite
RIGHT_KNEE = RobotMotor(12, 45, 180)  #genou droit
RIGHT_ANKLE = RobotMotor(13, 0, 120)   #cheville droite
HEAD_YAW = RobotMotor(14, 0, 180)    #tete gauche droite
HEAD_PITCH = RobotMotor(15, 35, 140)   #tete haut bas



def reset_position():
    LEFT_ELBOW.set_motor_position(180)
    sleep(0.2)
    LEFT_SHOULDER_ABDUCTOR.set_motor_position(90)
    sleep(0.2)
    LEFT_SHOULDER_ROTATOR.set_motor_position(180)
    sleep(0.2)
    LEFT_SHOULDER_FLEXOR.set_motor_position(90)
    sleep(0.2)
    RIGHT_SHOULDER_FLEXOR.set_motor_position(90)
    sleep(0.2)
    RIGHT_SHOULDER_ABDUCTOR.set_motor_position(0)
    sleep(0.2)
    RIGHT_SHOULDER_ROTATOR.set_motor_position(90)
    sleep(0.2)
    RIGHT_ELBOW.set_motor_position(0)
    sleep(0.2)
    LEFT_HIP.set_motor_position(90)
    sleep(0.2)
    LEFT_KNEE.set_motor_position(0)
    sleep(0.2)
    LEFT_ANKLE.set_motor_position(45)
    sleep(0.2)
    RIGHT_HIP.set_motor_position(90)
    sleep(0.2)
    RIGHT_KNEE.set_motor_position(180)
    sleep(0.2)
    RIGHT_ANKLE.set_motor_position(75)
    sleep(0.2)
    HEAD_YAW.set_motor_position(90)
    sleep(0.2)
    HEAD_PITCH.set_motor_position(90)

def set_delay():#seconds: int):
    time.sleep(1)#seconds)


def walk_n_steps(n):
    for _ in range(0, n - 1):
        LEFT_SHOULDER_FLEXOR.set_motor_position(60)
        sleep(.1)
        RIGHT_SHOULDER_FLEXOR.set_motor_position(60)
        sleep(.1)
        LEFT_HIP.set_motor_position(120)
        sleep(.1)
        RIGHT_HIP.set_motor_position(120)
        sleep(0.5)
        LEFT_SHOULDER_FLEXOR.set_motor_position(120)
        sleep(.1)
        RIGHT_SHOULDER_FLEXOR.set_motor_position(120)
        sleep(.1)
        LEFT_HIP.set_motor_position(60)
        sleep(.1)
        RIGHT_HIP.set_motor_position(60)
        sleep(.5)
        


def do_hi(ps):
    RIGHT_SHOULDER_ABDUCTOR.set_motor_position(130)
    sleep(0.5)
    RIGHT_SHOULDER_ROTATOR.set_motor_position(180)
    sleep(0.1)
    for _ in range(ps):
        RIGHT_ELBOW.set_motor_position(90)
        sleep(0.5)
        RIGHT_ELBOW.set_motor_position(0)
        sleep(0.5)
    RIGHT_SHOULDER_ROTATOR.set_motor_position(90)
    sleep(0.5)
    RIGHT_SHOULDER_ABDUCTOR.set_motor_position(0)



def walk_n_steps_with_knee_lift(ps):
    LEFT_SHOULDER_ROTATOR.set_motor_position(170)
    RIGHT_SHOULDER_ABDUCTOR.set_motor_position(10)
    for _ in range(0, ps - 1):
        LEFT_ELBOW.set_motor_position(150)
        sleep(0.2)
        LEFT_SHOULDER_FLEXOR.set_motor_position(90)
        sleep(0.2)
        RIGHT_SHOULDER_FLEXOR.set_motor_position(60)
        sleep(0.2)
        RIGHT_ELBOW.set_motor_position(0)
        sleep(0.2)
        LEFT_HIP.set_motor_position(100)
        sleep(0.2)
        LEFT_KNEE.set_motor_position(60)
        sleep(0.2)
        RIGHT_HIP.set_motor_position(120)
        sleep(0.2)
        RIGHT_KNEE.set_motor_position(180)
        sleep(0.2)
        LEFT_ELBOW.set_motor_position(180)
        sleep(0.2)
        LEFT_SHOULDER_FLEXOR.set_motor_position(120)
        sleep(0.2)
        RIGHT_SHOULDER_FLEXOR.set_motor_position(90)
        sleep(0.2)
        RIGHT_ELBOW.set_motor_position(30)
        sleep(0.2)
        LEFT_HIP.set_motor_position(50)
        sleep(0.2)
        LEFT_KNEE.set_motor_position(0)
        sleep(0.2)
        RIGHT_HIP.set_motor_position(80)
        sleep(0.2)
        RIGHT_KNEE.set_motor_position(120)
        sleep(0.2)


def do_no():
    for _ in range(0, 2):
        sleep(.5)
        HEAD_YAW.set_motor_position(120)
        sleep(.5)
        HEAD_YAW.set_motor_position(60)



def do_yes():
    for _ in range(0, 2):
        sleep(.5)
        HEAD_PITCH.set_motor_position(45)
        sleep(.5)
        HEAD_PITCH.set_motor_position(90)



def record_au():
    r = sr.Recognizer()
    micro = sr.Microphone()
    with micro as source:
        r.adjust_for_ambient_noise(source)
        
        print("vas-y")
        audio = r.listen(source)
        print("attend")
        voice_data = ''
    try:   
        voice_data = r.recognize_google(audio,language="fr-FR")
        print(voice_data)
        if(voice_data == "fais coucou"):
            do_hi(2)
    except sr.UnknownValueError:
        print("Désolé je n'ai pas compris")
    except sr.RequestError:
        print("Une erreur c'est produite")
    return voice_data
    



    


def action():
    b = record_au()
    if "fais coucou" in b :
        do_hi(1)
        print("j'ai fait coucou")
        francaster_speak("j'ai fait coucou", 'fr')
        
    elif "fais oui" in b:
        do_yes()
        francaster_speak("j'ai fait oui")
        
    elif "fais non" in b:
        do_no()
        francaster_speak("j'ai fait non")
        
    elif "arrete" in b:
        reset_position()
        exit()
        
    else : exit()


def gifle_g():
    LEFT_ELBOW.set_motor_position(100)
    sleep(0.3)
    LEFT_SHOULDER_ROTATOR.set_motor_position(0)
    sleep(0.3)
    LEFT_SHOULDER_FLEXOR.set_motor_position(0)
    sleep(0.3)
    LEFT_SHOULDER_ROTATOR.set_motor_position(180)
    sleep(2)
    reset_position()

def leve_le_pied_droit():
    RIGHT_HIP.set_motor_posion(180)
    RIGHT_KNEE.set_motor_posion(90)
    
#action()
#walk_n_steps_with_knee_lift(5)
