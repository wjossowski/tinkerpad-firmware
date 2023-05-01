from kmk.keys import KC
from layers.layer import Layer

class EmptyLayer(Layer):
    name = "Empty"
    keymap = [
            KC.NA, KC.NA, KC.NA, KC.NA,
            KC.NA, KC.NA, KC.NA, KC.NA,
            KC.NA, KC.NA, KC.NA, KC.NA,
            KC.NA, KC.NA, KC.NA, KC.NA,
            ],

Empty = EmptyLayer()
