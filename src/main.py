from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_Display import Oled, OledDisplayMode, OledReactionType, OledData

from boards.rev1 import Macropad
from layers.base import BaseLayer
from layers.kicad import KicadSCHLayer, KicadPCBLayer

keyboard = Macropad()
keyboard.setup([
    BaseLayer(), KicadSCHLayer(), KicadPCBLayer()
])

oled_ext = Oled(
    OledData(
        corner_one={0: OledReactionType.STATIC, 1: ["Layer: "]},
        corner_two={0: OledReactionType.STATIC, 1: [""]},
        corner_three={0: OledReactionType.LAYER, 1: keyboard.layer_names},
        corner_four={0: OledReactionType.LAYER, 1: keyboard.layer_modes}
    ),
    toDisplay=OledDisplayMode.TXT, flip=True)
keyboard.extensions.append(oled_ext)

if __name__ == '__main__':
    keyboard.go()
