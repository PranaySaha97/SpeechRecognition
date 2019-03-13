import speech_recognition as sr
import webbrowser
import os

while True:
    print("1.Normal  People\n2.Disabled People\n3.Control Your System")
    ch=int(input('Enter your choice: '))
    
    if (ch==1):
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print ("A moment of silence")
            r.adjust_for_ambient_noise(source, duration = 1)
            print("Say something!")
            audio = r.listen(source)
            print("Trying to recognize audio")

            try:
                t=r.recognize_google(audio)
                print ("You just said " ,t)
 
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
        
    elif (ch==2):
        try:
            final_string=""
            r = sr.Recognizer()
            while(True):
            
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration = 1)
                    print("Speak")
                    audio = r.listen(source)
                    print("Wait")
                    try:
                        t=r.recognize_google(audio)
                        final_string=final_string+" "+t
                
                    except sr.UnknownValueError:
                        print("Google Speech Recognition could not understand audio")
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except KeyboardInterrupt:
            print("Consolidated Result: ",final_string)
            print("Exited")
    elif (ch==3):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print ("A moment of silence")
            r.adjust_for_ambient_noise(source, duration = 1)
            print("Say something!")
            audio = r.listen(source)
            print("Trying to recognize audio")
        try:
            t=r.recognize_google(audio)
            print ("You just said " ,t)

            t=t.strip().lower()

            if t == 'show date':
                print("Showing Date")
                os.system('date')
            elif t == 'shut down':
                print('Shutting Down')
                os.system('shutdown /s')
            elif t == 'reboot now':
                print('Rebooting Now')
                os.system('shutdown /r')
            elif t== 'play my favourite video':
                print('Playing your video')
                webbrowser.open('https://www.youtube.com/watch?v=UhYRlI_bpJQ')
            elif t == 'which is my college':
                print('Your college is: SJCIT')
                webbrowser.open('http://sjcit.ac.in/')
            else:
                print("Command Not Recognised Yet!! Please Try Again")
                
        except sr.UnknownValueError:
            print("Audio Unknown (or not understood)")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    else: 
        print("Invalid Option")
    
    cnt= input("Do you want to continue (Y/N)? : ")
    if cnt == 'n' or cnt == 'N':
        exit()
    else: 
        pass
