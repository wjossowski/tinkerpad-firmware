import board

from kmk.kmk_keyboard import KMKKeyboard as KMKKeyboard
from kmk.scanners import DiodeOrientation

class Macropad(KMKKeyboard):
    diode_orientation = DiodeOrientation.COL2ROW

    col_pins = ( board.GP20, board.GP19, board.GP12, board.GP11 )
    row_pins = ( board.GP17, board.GP16, board.GP15, board.GP14 )

    enc1_pins = ( board.GP6, board.GP7, board.GP5 )
    enc2_pins = ( board.GP27, board.GP26, board.GP28 )

    SDA=board.GP0
    SCL=board.GP1
