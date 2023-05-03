from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

from layers.layer import Layer

class EncoderLayerHandler:
    encoder = EncoderHandler()

    def __init__(self, pins):
        self.encoder.pins = pins

    def compose(self, layers: list[Layer]):
        self.encoder.map = self._build_layer_jump(layers)
        return self.encoder

    def _build_layer_jump(self, layers: list[Layer]):
        enc = []
        count = len(layers)
        for i, layer in enumerate(layers):
            prev = self._prev(i, count)
            next = self._next(i, count)
            enc.append(((prev, next, KC.DF(0)), layer.enc))
        return enc

    def _prev(self, i: int, count: int):
        return KC.DF(i-1 if i > 0 else count-1)

    def _next(self, i: int, count: int):
        return KC.DF(i+1 if i < count-1 else 0)

