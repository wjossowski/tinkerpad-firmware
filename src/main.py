from boards.rev1 import Macropad
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_Display import Oled, OledDisplayMode, OledReactionType, OledData

keyboard = Macropad()
keyboard.modules.append(Layers())

# ========= ENCODER ==================
keyboard.extensions.append(MediaKeys())
encoder_handler = EncoderHandler()
encoder_handler.pins = (keyboard.enc_1_pins, keyboard.enc_2_pins)
encoder_handler.map = [(
    (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.AUDIO_MUTE),
    (KC.MEDIA_PREV_TRACK, KC.MEDIA_NEXT_TRACK, KC.MEDIA_PLAY_PAUSE),
    )]
keyboard.extensions.append(encoder_handler)

# ========= KEYMAP ===================
keyboard.keymap = [[
            KC.AUDIO_MUTE, KC.MEDIA_PLAY_PAUSE, KC.X, KC.X,
            KC.A, KC.B, KC.C, KC.D,
            KC.E, KC.F, KC.G, KC.H,
            KC.I, KC.J, KC.K, KC.L,
            KC.M, KC.N, KC.O, KC.P,
            ]]

# ========= OLED ===================
oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["SZANOWNE"]},
        # corner_two={0:OledReactionType.STATIC,1:layers.names},
        corner_two={0:OledReactionType.STATIC,1:["PANSTWO"]},
        corner_three={0:OledReactionType.STATIC,1:["KOCHANI"]},
        corner_four={0:OledReactionType.STATIC,1:["MOI"]}
        ),
        toDisplay=OledDisplayMode.TXT,flip=True)

# ========= EXTENSIONS =============
keyboard.extensions.append(oled_ext)

if __name__ == '__main__':
    keyboard.go()

