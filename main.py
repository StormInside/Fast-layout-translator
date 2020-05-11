from translator import Translator
from pynput.keyboard import Key, KeyCode, Listener
import pyperclip

def changeLayout():

    cb = pyperclip.paste()
    output = Translator().translate(cb)
    pyperclip.copy(output)


def changeCapitalise():

    cb = pyperclip.paste()
    output = Translator().change_cap(cb)
    pyperclip.copy(output)


combination_to_function = {
    frozenset([Key.ctrl_l, Key.space]): changeLayout,
    frozenset([Key.ctrl_l, Key.alt_l, Key.space]): changeCapitalise,
}

current_keys = set()

def on_press(key):
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        combination_to_function[frozenset(current_keys)]()

def on_release(key):
        current_keys.clear()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()