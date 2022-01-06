import pyautogui
import time
import pydirectinput
def check_for_pokemon_catch():
    pydirectinput.press('x')
    pydirectinput.keyDown('space')
    time.sleep(2)
    print('Checking If a Pkmn Was Caught')
    got_pokemon = pyautogui.locateOnScreen('got_a_pkmn.png', confidence=0.9)
    pydirectinput.keyUp('space')
    if(got_pokemon):
        print('Got a pokemon, Entering Battle!')
        pydirectinput.press('enter')
        return True
    else:
        print('Got nothing on the rod, restarting')
        pydirectinput.press('f1')
        return False

def check_for_start_button(attemps):
    if(attemps == 0):
        count = 1
    else:
        count = attemps
        
   
    start_button = pyautogui.locateOnScreen('start_button.png', confidence=0.9)
    if(start_button):
        print('Found Start Key...')
        pyautogui.click(start_button)
        time.sleep(1)
        pydirectinput.press('x')
        print('Moving to check if a Pkmn was caught')
        while(not check_for_pokemon_catch()):
            check_for_pokemon_catch()
        return True
    else:
        print(f'Start Key Not Found... Retrying({count})')
        count +=1
        if(count >= 6):
            print('Closing program...')
            return False
        else: 
            check_for_start_button(count)
        return False


check_for_start_button(0)
