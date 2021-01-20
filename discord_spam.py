import clipboard, time
from pynput import mouse, keyboard
mousee = mouse.Controller()
keyboardd = keyboard.Controller()
time.sleep(10) # TIME TILL GO TO APP
le_num = 1
while True: # LOOP DE LOOP
    if not le_num == 1:
        keyboardd.press(keyboard.Key.up)
        keyboardd.release(keyboard.Key.enter)
        keyboardd.press(keyboard.Key.space)
        keyboardd.release(keyboard.Key.space)
    keyboardd.type(str(le_num))
    keyboardd.press(keyboard.Key.enter)
    keyboardd.release(keyboard.Key.enter)
    time.sleep(1.5) # ADJUST ACCORGINGLY
    le_num += 1
    if le_num == 101: # TILL.....
        break
