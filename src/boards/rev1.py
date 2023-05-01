import board

from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.kmk_keyboard import KMKKeyboard as KMKKeyboard

from layers.layer import Layer


class Macropad(KMKKeyboard):
    diode_orientation = DiodeOrientation.COL2ROW

    col_pins = (board.GP28, board.GP12, board.GP5, board.GP6)
    row_pins = (board.GP0, board.GP18, board.GP13, board.GP14, board.GP15)

    enc_1_pins = (board.GP27, board.GP26, None)
    enc_2_pins = (board.GP1, board.GP4, None)

    encoder_handler: EncoderHandler

    SDA = board.GP2
    SCL = board.GP3

    modules = [Layers()]
    extensions = [MediaKeys()]

    layer_names: list(str) = []
    layer_modes: list(str) = []

    def __init__(self):
        self.encoder_handler = EncoderHandler()
        self.encoder_handler.pins = (self.enc_1_pins, self.enc_2_pins)
        self.extensions.append(self.encoder_handler)

    def setup(self, layers: list(Layer)):
        self.layer_names = [layer.name for layer in layers]
        self.layer_modes = [layer.mode for layer in layers]
        self.keymap = [layer.keymap for layer in layers]
        self.encoder_handler.map = self._setup_layers_switch(layers)

    def _setup_layers_switch(self, layers: list(Layer)):
        max = len(layers)
        enc = []
        for i, layer in enumerate(layers):
            enc.append(
                ((self._prev(i, max), self._next(i, max), self._ground()), layer.enc)
            )
        return enc

    def _prev(self, i: int, max: int):
        return KC.DF(i-1 if i > 0 else max-1)

    def _next(self, i: int, max: int):
        return KC.DF(i+1 if i < max-1 else 0)

    def _ground(self):
        return KC.DF(0)
