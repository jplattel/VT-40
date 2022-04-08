print("Starting VT-40")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.keys import KC
from kmk.rotary_encoder import Encoder

# Setup keyboard
keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COLUMNS

# Encoder handlers
def onRotateLeftEncode(direction):
    if(direction > 0):
        print("turning left knob way (right?)")
    elif(direction < 0):
        print("turning left knob way (left?)")

def onRotateRightEncode(direction):
    if(direction > 0):
        print("turning right knob way (right?)")
    elif(direction < 0):
        print("turning right knob way (left?)")

# Pins
keyboard.col_pins = (board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP21,board.GP20,board.GP19,board.GP18,board.GP22)
keyboard.row_pins = (board.GP2,board.GP3,board.GP4,board.GP5)

# Encoders
keyboard.encoders = [Encoder(board.GP26, board.GP16, onRotateLeftEncode), Encoder(board.GP27, board.GP17, onRotateRightEncode)]

# Keymap
keyboard.keymap = [
	[
		KC.ESC,  KC.Q,    KC.W,     KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,    KC.I,     KC.O,    KC.P,    KC.BSPC,           KC.MPLY,
		KC.TAB,  KC.A,    KC.S,     KC.D,   KC.F,   KC.G,   KC.H,   KC.J,    KC.K,     KC.L,    KC.GRV,  KC.LSFT(KC.BSLS),  KC.MUTE,
		KC.LSFT, KC.Z,    KC.X,     KC.C,   KC.V,   KC.B,   KC.N,   KC.M,    KC.COMMA, KC.DOT,  KC.UP,   KC.ENT,            KC.NO,
		KC.LCTL, KC.LALT, KC.LCMD,  KC.SPC, KC.SPC, KC.SPC, KC.SPC, KC.RALT, KC.NO,    KC.LEFT, KC.DOWN, KC.RIGHT,          KC.NO,
	],
]

# Start wandering...
if __name__ == '__main__':
    keyboard.go()