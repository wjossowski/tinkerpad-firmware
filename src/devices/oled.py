from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.peg_oled_Display import Oled, OledDisplayMode, OledReactionType, OledData

class StatusOLED:
    oled: Oled

    def __init__(self, layer_names: list[str], layer_modes: list[str]):
        self.oled = Oled( OledData(
            corner_one={0: OledReactionType.STATIC, 1: ["Layer:"]},
            corner_two={0: OledReactionType.STATIC, 1: ["Mode:"]},
            corner_three={0: OledReactionType.LAYER, 1: layer_names},
            corner_four={0: OledReactionType.LAYER, 1: layer_modes}
            ), toDisplay=OledDisplayMode.TXT, flip=True)

    def install_on(self, keyboard: KMKKeyboard):
        keyboard.extensions.append(self.oled)
