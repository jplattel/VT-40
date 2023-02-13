print("Starting VT-40")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.debug_enabled = True
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP21,
    board.GP20,
    board.GP19,
    board.GP18,
)

keyboard.row_pins = (
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5
)

keyboard.diode_orientation = DiodeOrientation.COLUMNS

encoder_handler = EncoderHandler()
encoder_handler.pins = (
	(board.GP16, board.GP17, None,),
	(board.GP26, board.GP27, None,),
)
encoder_handler.map = [
    (
        (KC.VOLD,KC.VOLU,1),
        (KC.BRID,KC.BRIU,1),
    )
]
keyboard.modules.append(encoder_handler)

keyboard.keymap = [
	[
		KC.ESC,  KC.Q,    KC.W,  	KC.E,   KC.R,   KC.T,   KC.Y,    KC.U,     KC.I,     KC.O,    KC.P,    KC.BKDL, 	
		KC.TAB,  KC.A,    KC.S,  	KC.D,   KC.F,   KC.G,   KC.H,    KC.J,     KC.K,     KC.L,    KC.GRV,  KC.LSFT(KC.BSLS),
		KC.LSFT, KC.Z,    KC.X,  	KC.C,   KC.V,   KC.B,   KC.N,    KC.M,     KC.COMMA, KC.DOT,  KC.UP,   KC.ENT,
		KC.LCTL, KC.LALT, KC.LGUI,	KC.SPC, KC.SPC, KC.SPC, KC.RGUI, KC.RALT,  KC.NO,    KC.LEFT, KC.DOWN, KC.RIGHT,
	],
]

if __name__ == '__main__':
	keyboard.go()
