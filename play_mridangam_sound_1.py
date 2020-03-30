import winsound
import msvcrt
'''
print ('Press s or n to continue:\n')
while(True):
    input_char = msvcrt.getch()
    if input_char == 's': 
       print ('YES')
       
if msvcrt.kbhit():
    key = msvcrt.getch().decode("utf-8").lower() # getch() returns bytes data that we need to decode in order to read properly. i also forced lowercase which is optional but recommended
    if key == "w": 
          winsound.PlaySound("sound1",winsound.SND_FILENAME)


while(True):
    msg=input('press sound:')
    if(msg=='s'):
        winsound.PlaySound("sound1",winsound.SND_FILENAME)
        
'''

from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    print(letter)
    if(letter=='a'):
         winsound.PlaySound("sound_1",winsound.SND_FILENAME)
    elif(letter=='s'):
         winsound.PlaySound("sound_2",winsound.SND_FILENAME)
    elif(letter=='d'):
         winsound.PlaySound("sound_3",winsound.SND_FILENAME)

    #with open("log.txt", 'a') as f:
       #f.write(letter)

# Collecting events until stopped

with Listener(on_press=write_to_file) as l:
    l.join()
    #print(l)
    
