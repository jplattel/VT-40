# My Personal VT-40 (original by [vladantrhlik](https://github.com/vladantrhlik/VT-40/))

40% ortholinear mechanical keyboard, modified to my own taste with a cover for the microcontroller & a custom base-plate.

## Materials

- Raspberry Pi Pico
- Diodes (1N4148)
- PCB (ordered on JLC with `pcb/gerber.zip`)
- Encoders (EC11)
- screws (which type did I use?)
    - m2.5 10mm (2x)    mounting the cover to the Pico
    - m4 15mm? (1x)     mounting the cover to the PCB
    - m2 (6x)           bottom plate to PCB 
- Switches (running Kailh Low Profile Choc Red's)
- Keycaps (got a set of [Work Louder Blind](https://worklouder.cc/shop/wrk-blind/))

## Building it

Solder the diodes, put in the headers for the Pico, solder the Pico to the pcb and finally the encoders & switches

I lasered the microcontroller cover out of black HDPE, 3mm thick. Use the file in the `dxf` folder. Carefully mount the cover on the microcontroller. Then use the bigger screw to attach the cover to the PCB. (the screw will self-fasten in the PCB).

Print the two bottom plates, the first one (`bottom-1.stl`) in the color you like, the other one (`bottom-2.stl`) in TPU. Mount `bottom-1` plate to the PCB and attach the `bottom-2` plate with double sided tape.

## Code

See the `src` folder. Updated for the new KMK version which supports the encoders differently. I didn't solder the LEDs, so that's not in there!. Flash KMK to the Pico and copy the `main.py` over when plugging the keyboard in. That's it, ready now!