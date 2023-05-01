from kmk.keys import KC
from layers.layer import Layer

class BaseLayer(Layer):
    name = "Base"
    keymap = [
            KC.A, KC.B, KC.C, KC.D,
            KC.E, KC.F, KC.G, KC.H,
            KC.I, KC.J, KC.K, KC.L,
            KC.M, KC.N, KC.O, KC.P,
            ],

Base = BaseLayer()
