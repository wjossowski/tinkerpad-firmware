import board

from kmk.kmk_keyboard import KMKKeyboard as KMKKeyboard
from kmk.scanners import DiodeOrientation

class Macropad(KMKKeyboard):
    diode_orientation = DiodeOrientation.COL2ROW

    col_pins = (board.GP28, board.GP12, board.GP5, board.GP6)
    row_pins = (board.GP0, board.GP18, board.GP13, board.GP14, board.GP15)

    enc_1_pins = (board.GP27, board.GP26, None)
    enc_2_pins = (board.GP1, board.GP4, None)

    SDA=board.GP2
    SCL=board.GP3
