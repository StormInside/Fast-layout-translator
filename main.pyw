from translator import Translator
from pynput.keyboard import Key, KeyCode, Listener
import pyperclip

def get_input():
    # print("\n"+"Write text to translate \n")
    # text  = input("-->")
    # # text = "GNSDJLGNS>:"
    # output = Translator().translate(text)
    # print(output)
    cb = pyperclip.paste()
    output = Translator().translate(cb)
    pyperclip.copy(output)



combination_to_function = {
    frozenset([Key.ctrl_l, Key.space]): get_input, 
}

# Currently pressed keys
current_keys = set()

def on_press(key):
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        combination_to_function[frozenset(current_keys)]()

def on_release(key):
        current_keys.clear()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()