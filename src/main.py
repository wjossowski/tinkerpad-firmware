from boards.rev1 import Macropad
from layers.base import BaseLayer
from layers.kicad import KicadSCHLayer, KicadPCBLayer
from devices.oled import StatusOLED
from layers.layer_composer import LayerComposer

kb = Macropad()

layers = LayerComposer([ BaseLayer(), KicadSCHLayer(), KicadPCBLayer() ])
layers.install_on(kb, kb.enc_pins)

oled = StatusOLED(layers.names, layers.modes)
oled.install_on(kb)

if __name__ == '__main__':
    kb.go()
