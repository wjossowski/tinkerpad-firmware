from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence

from layers.layer import Layer

ruler = KC.LGUI(KC.LSFT(KC.M))
undo = KC.LGUI(KC.Z)
redo = KC.LSFT(KC.LGUI(KC.Z))
render = KC.LALT(KC.N3)
close = KC.LGUI(KC.W)
save = KC.LGUI(KC.S)

duplicate = simple_key_sequence([
    KC.LGUI(KC.C),
    KC.LGUI(KC.V),
])


class KicadSCHLayer(Layer):
    name = "KiCad"
    mode = "Schematic"
    keymap = [
        close,  KC.DF(0),   KC.X,   KC.X,
        # -----------------------------------------------
        close,  KC.E,       ruler,  KC.BSPC,
        save,   duplicate,  KC.M,   KC.ENT,
        KC.A,   KC.F,       KC.R,   redo,
        KC.ESC, KC.W,       KC.Q,   undo,
    ]
    enc = (KC.LSFT(KC.N), KC.N, close)


class KicadPCBLayer(Layer):
    name = "KiCad"
    mode = "PCB Design"
    keymap = [
        close,  KC.DF(0),   KC.X,       KC.X,
        # -----------------------------------------------
        close,  KC.E,       ruler,  KC.BSPC,
        save,   KC.H,       KC.M,   KC.ENT,
        render, KC.F,       KC.R,   redo,
        KC.ESC, KC.X,       KC.V,   undo,
    ]
    enc = (KC.LSFT(KC.N), KC.N, close)
