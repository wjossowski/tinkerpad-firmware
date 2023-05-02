from kmk.keys import KC
from layers.layer import Layer


class BaseLayer(Layer):
    name = "Base"
    mode = "Numeric"
    keymap = [
        KC.DF(0),  KC.AUDIO_MUTE,   KC.X,       KC.X,
        # -----------------------------------------------
        KC.ESC,         KC.NA,      KC.NA,      KC.ENT,
        KC.N7,          KC.N8,      KC.N9,      KC.DOT,
        KC.N4,          KC.N5,      KC.N6,      KC.COMM,
        KC.N1,          KC.N2,      KC.N3,      KC.N0,
    ]
    enc = (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.AUDIO_MUTE)
