print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.encoder import RotaryioEncoder
from kmk.modules.mouse_keys import MouseKeys

_KEY_CFG = [
    board.GP2,  board.GP3,  board.GP4, board.G5 
]

# Keyboard implementation class
class MyKeyboard(KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = [
                KeysScanner(
                    # require argument:
                    pins=_KEY_CFG,
                    # optional arguments with defaults:
                    value_when_pressed=False,
                    pull=True,
                    interval=0.02,
                    max_events=64
                )
#                ,
#                RotaryioEncoder(
#                    pin_a=board.GP2,
#                    pin_b=board.GP3,
#                    # optional
#                    divisor=4
#               )
#                ,
#                RotaryioEncoder(
#                    pin_a=board.GP17,
#                    pin_b=board.GP18,
#                    # optional
#                    divisor=4
#               )
#                ,
#                RotaryioEncoder(
#                    pin_a=board.GP5,
#                    pin_b=board.GP6,
#                    # optional
#                    divisor=4
#               )
        ]

keyboard = MyKeyboard()
keyboard.modules.append(MouseKeys())
keyboard.keymap = [
    [ KC.N1, KC.N2, KC.N3, KC.N4 ] #, KC.SPACE, KC.MW_UP, KC.MW_DOWN, KC.N5, KC.N6, KC.N7, KC.N8 ]
]

# keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()

