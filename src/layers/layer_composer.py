from kmk.kmk_keyboard import KMKKeyboard

from devices.encoder_layer_handler import EncoderLayerHandler
from layers.layer import Layer

class LayerComposer:
    layers: list[Layer]
    names: list[str] = []
    modes: list[str] = []

    def __init__(self, layers: list[Layer]):
        self.layers = layers
        self.names = [layer.name for layer in layers]
        self.modes = [layer.mode for layer in layers]

    def install_on(self, keyboard: KMKKeyboard, encoder_pins):
        encoder = EncoderLayerHandler(encoder_pins).compose(self.layers)
        keyboard.extensions.append(encoder)
        keyboard.keymap = [layer.keymap for layer in self.layers]

