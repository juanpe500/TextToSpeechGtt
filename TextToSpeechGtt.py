from playsound import playsound
import gtts
import os

if not os.path.exists(os.getcwd()+'/Output/'): #Create output's folder
    os.makedirs(os.getcwd()+'/Output/')

JP="      ## ########  \n      ## ##     ## \n      ## ##     ## \n      ## ########  \n##    ## ##        \n##    ## ##        \n ######  ##        "
cln=lambda: os.system('cls')
op=os.getcwd()+'/Output/'

while True:
    cln()
    msg=input("Text to speech by \n\n"+JP+"\n\nEnter text or press enter to exit\n")
    if len(msg)>0:
        tts = gtts.gTTS(msg, lang="es-us")
        _,_,ff = next(os.walk(op))
        tts.save(op+str(len(ff)+1)+'.mp3')
        playsound(op+str(len(ff)+1)+'.mp3')
        os.startfile(op) #This open the output's folder, you can comment it
    else:
        cln()
        print("Text to speech by \n\n"+JP+"\n\nThanks for using me")
        exit() 

