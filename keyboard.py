import json
from decimal import Decimal

#Global Static
UNIT = 19.05
BOARD_X = (16 * UNIT) + (30.48 * 2) + 4
BOARD_Y = (UNIT * 6)
OFFSET_X = (BOARD_X / 2) - (16 * UNIT) / 2
OFFSET_Y = (UNIT * 6) - (UNIT / 2) 

f1 = open("1-schematic_page1.scr", "w")
f2 = open("2-schematic_page2.scr", "w")
f3 = open("3-schematic_page3.scr", "w")
f4 = open("4-board.scr", "w")



data = json.loads (
    '''
    [
        [{"n":"ESC"},{"n":"F1"},{"n":"F2"},{"n":"F3"},{"n":"F4"},{"n":"F5"},{"n":"F6"},{"n":"F7"},{"n":"F8"},{"n":"F9"},{"n":"F10"},{"n":"F11"},{"n":"F12"},{"n":"PrtScr"},{"n":"Pause"},{"n":"Del"}],
        [{"n":"Tilde"},{"n":"1"},{"n":"2"},{"n":"3"},{"n":"4"},{"n":"5"},{"n":"6"},{"n":"7"},{"n":"8"},{"n":"9"},{"n":"0"},{"n":"Minus"},{"n":"Plus"},{"n":"Backspace","s":2},{"n":"Home"}],
        [{"n":"Tab","s":1.5},{"n":"Q"},{"n":"W"},{"n":"E"},{"n":"R"},{"n":"T"},{"n":"Y"},{"n":"U"},{"n":"I"},{"n":"O"},{"n":"P"},{"n":"LBracket"},{"n":"RBracket"},{"n":"Pipe","s":1.5},{"n":"PgUP"}],
        [{"n":"Caps","s":1.75},{"n":"A"},{"n":"S"},{"n":"D"},{"n":"F"},{"n":"G"},{"n":"H"},{"n":"J"},{"n":"K"},{"n":"L"},{"n":"Semicolon"},{"n":"Quote"},{"n":"Enter","s":2.25},{"n":"PgDown"}],
        [{"n":"LShift","s":2.25},{"n":"Z"},{"n":"X"},{"n":"C"},{"n":"V"},{"n":"B"},{"n":"N"},{"n":"M"},{"n":"Comma"},{"n":"Period"},{"n":"Slash"},{"n":"RShift","s":1.75},{"n":"Up"},{"n":"End"}],
        [{"n":"LCtl","s":1.25},{"n":"LWin","s":1.25},{"n":"LAlt","s":1.25},{"n":"Space","s":6.25},{"n":"Ralt"},{"n":"Fn"},{"n":"Ctl"},{"n":"Left"},{"n":"Down"},{"n":"Right"}]
    ]
    '''
)



# Download and import the following into Eagle (I'm using eagle 9.2)
#  https://github.com/VinnyCordeiro/NPKC-17-switch-tester-alt-PCB/blob/master/Cherry_MX_v7.0.lbr
#  https://github.com/adafruit/Adafruit-Eagle-Library/blob/master/adafruit.lbr
#  https://github.com/chiengineer/Eagle-Libraries/blob/master/Knobs-Buttons-Switches/switch-alps.lbr
#  https://www.diymodules.org/eagle-show-library?type=usr&id=2500

# Arduino nRF52 Feather Bluefruit Headers
f1.write("""
ADD PINHD-1X16@pinhead (0 3);
NET RESET (-.1 3.7) (-.4 3.7);
NET +3V3 (-.1 3.6) (-.4 3.6);
NET +3V3_2 (-.1 3.5) (-.4 3.5);
NET PE (-.1 3.4) (-.4 3.4);
NET A0 (-.1 3.3) (-.4 3.3);
NET A1 (-.1 3.2) (-.4 3.2);
NET A2 (-.1 3.1) (-.4 3.1);
NET A3 (-.1 3.0) (-.4 3.0);
NET A4 (-.1 2.9) (-.4 2.9);
NET A5 (-.1 2.8) (-.4 2.8);
NET SCK (-.1 2.7) (-.4 2.7);
NET MOSI (-.1 2.6) (-.4 2.6);
NET MISO (-.1 2.5) (-.4 2.5);
NET TXD (-.1 2.4) (-.4 2.4);
NET RXD (-.1 2.3) (-.4 2.3);
NET DFU (-.1 2.2) (-.4 2.2);

ADD PINHD-1X12@pinhead (2 3);
NET BAT (1.9 3.5) (1.6 3.5);
NET EN (1.9 3.4) (1.6 3.4);
NET USB (1.9 3.3) (1.6 3.3);
NET 16 (1.9 3.2) (1.6 3.2);
NET 15 (1.9 3.1) (1.6 3.1);
NET 7 (1.9 3.0) (1.6 3.0);
NET 11 (1.9 2.9) (1.6 2.9);
NET 13 (1.9 2.8) (1.6 2.8);
NET 30 (1.9 2.7) (1.6 2.7);
NET 27 (1.9 2.6) (1.6 2.6);
NET SCL (1.9 2.5) (1.3 2.5);
NET SDA (1.9 2.4) (1.3 2.4);

ADD +3V3@supply1 (1.0 2.8);
ADD +3V3@supply1 (1.0 2.3);
NET SCL (1.4 2.5)(1.4 2.7);
NET SDA (1.4 2.4)(1.4 2.2);
ADD R-US_0204/5@adafruit (1.2 2.7);
ADD R-US_0204/5@adafruit (1.2 2.2);

LABEL (-.4 3.7) (-.6 3.7);
LABEL (-.4 3.6) (-.6 3.6);
LABEL (-.4 3.5) (-.6 3.5);
LABEL (-.4 3.4) (-.6 3.4);
LABEL (-.4 3.3) (-.6 3.3);
LABEL (-.4 3.2) (-.6 3.2);
LABEL (-.4 3.1) (-.6 3.1);
LABEL (-.4 3.0) (-.6 3.0);
LABEL (-.4 2.9) (-.6 2.9);
LABEL (-.4 2.8) (-.6 2.8);
LABEL (-.4 2.7) (-.6 2.7);
LABEL (-.4 2.6) (-.6 2.6);
LABEL (-.4 2.5) (-.6 2.5);
LABEL (-.4 2.4) (-.6 2.4);
LABEL (-.4 2.3) (-.6 2.3);
LABEL (-.4 2.2) (-.6 2.2);

LABEL (1.9 3.5) (1.5 3.5);
LABEL (1.9 3.4) (1.5 3.4);
LABEL (1.9 3.3) (1.5 3.3);
LABEL (1.9 3.2) (1.5 3.2);
LABEL (1.9 3.1) (1.5 3.1);
LABEL (1.9 3.0) (1.5 3.0);
LABEL (1.9 2.9) (1.5 2.9);
LABEL (1.9 2.8) (1.5 2.8);
LABEL (1.9 2.7) (1.5 2.7);
LABEL (1.9 2.6) (1.5 2.6);
LABEL (1.3 2.5) (1.1 2.5);
LABEL (1.3 2.4) (1.1 2.4);

ADD EC12E_SW LEFT_WHEEL (0 4.5);
ADD PE@supply1  (-0.4 4.2);
NET 16 (-0.3 4.7) (-0.3 4.8);
NET 15 (-0.5 4.7) (-0.5 4.8);
NET SW-83 (0.6 4.7) (0.7 4.7);
NET PE (2.2 4.7) (2.1 4.7);
ADD PE@supply1 (2.1 4.6);
LABEL (0.7 4.7) (0.7 4.7);
LABEL (-0.3 4.8) (-0.3 4.8);
LABEL (-0.5 4.8) (-0.5 4.8);


ADD EC12E_SW RIGHT_WHEEL (2 4.5);
ADD PE@supply1  (1.6 4.2);
NET 7 (1.5 4.7) (1.5 4.8);
NET 11 (1.7 4.7) (1.7 4.8);
NET SW-84 (2.6 4.7) (2.7 4.7);
NET PE (0.2 4.7) (0.1 4.7);
ADD PE@supply1 (0.1 4.6);
LABEL (1.5 4.8) (1.5 4.8);
LABEL (1.7 4.8) (1.7 4.8);
LABEL (2.7 4.7) (2.7 4.7);

ADD JOYSTICKPTH@adafruit RIGHT_JOYSTICK (4 3);
NET +3V3 (3.6 3.4) (3.5 3.4);
NET A0 (3.6 3.3) (3.5 3.3);
NET PE (3.6 3.2) (3.5 3.2);
NET +3V3 (3.6 3.0) (3.5 3.0);
NET A1 (3.6 2.9) (3.5 2.9);
NET PE (3.6 2.8) (3.5 2.8);
NET SW-85 (3.6 2.6) (3.5 2.6);
NET PE (3.6 2.5) (3.5 2.5);
LABEL (3.5 3.4) (3.2 3.4);
LABEL (3.5 3.3) (3.2 3.3);
LABEL (3.5 3.2) (3.2 3.2);
LABEL (3.5 3.0) (3.2 3.0);
LABEL (3.5 2.9) (3.2 2.9);
LABEL (3.5 2.8) (3.2 2.8);
LABEL (3.5 2.6) (3.2 2.6);
LABEL (3.5 2.5) (3.2 2.5);



ADD JOYSTICKPTH@adafruit LEFT_JOYSTICK (6 3);
NET +3V3 (5.6 3.4) (5.5 3.4);
NET A2 (5.6 3.3) (5.5 3.3);
NET PE (5.6 3.2) (5.5 3.2);
NET +3V3 (5.6 3.0) (5.5 3.0);
NET A3 (5.6 2.9) (5.5 2.9);
NET PE (5.6 2.8) (5.5 2.8);
NET SW-86 (5.6 2.6) (5.5 2.6);
NET PE (5.6 2.5) (5.5 2.5);
LABEL (5.5 3.4) (5.2 3.4);
LABEL (5.5 3.3) (5.2 3.3);
LABEL (5.5 3.2) (5.2 3.2);
LABEL (5.5 3.0) (5.2 3.0);
LABEL (5.5 2.9) (5.2 2.9);
LABEL (5.5 2.8) (5.2 2.8);
LABEL (5.5 2.6) (5.2 2.6);
LABEL (5.5 2.5) (5.2 2.5);


ADD PINHD-2X5@pinhead (0 1.7);
NET SW-87 (-.1 1.9) (-.3 1.9);
NET SW-88 (-.1 1.8) (-.3 1.8);
NET SW-89 (-.1 1.7) (-.3 1.7);
NET SW-90 (-.1 1.6) (-.3 1.6);
NET SW-91 (-.1 1.5) (-.3 1.5);
NET PE (.2 1.9) (.4 1.9);
NET PE (.2 1.8) (.4 1.8);
NET PE (.2 1.7) (.4 1.7);
NET PE (.2 1.6) (.4 1.6);
NET PE (.2 1.5) (.4 1.5);

LABEL (-.3 1.9)(-.6 1.9);
LABEL (-.3 1.8)(-.6 1.8);
LABEL (-.3 1.7)(-.6 1.7);
LABEL (-.3 1.6)(-.6 1.6);
LABEL (-.3 1.5)(-.6 1.5);
LABEL (.4 1.9)(.4 1.9);
LABEL (.4 1.8)(.4 1.8);
LABEL (.4 1.7)(.4 1.7);
LABEL (.4 1.6)(.4 1.6);
LABEL (.4 1.5)(.4 1.5);


ADD PINHD-2X5@pinhead (0 0.7);
NET SW-92 (-.1 0.9) (-.3 0.9);
NET SW-93 (-.1 0.8) (-.3 0.8);
NET SW-94 (-.1 0.7) (-.3 0.7);
NET SW-95 (-.1 0.6) (-.3 0.6);
NET SW-96 (-.1 0.5) (-.3 0.5);
NET PE (.2 0.9) (.4 0.9);
NET PE (.2 0.8) (.4 0.8);
NET PE (.2 0.7) (.4 0.7);
NET PE (.2 0.6) (.4 0.6);
NET PE (.2 0.5) (.4 0.5);

LABEL (-.3 0.9)(-.6 0.9);
LABEL (-.3 0.8)(-.6 0.8);
LABEL (-.3 0.7)(-.6 0.7);
LABEL (-.3 0.6)(-.6 0.6);
LABEL (-.3 0.5)(-.6 0.5);
LABEL (.4 0.9)(.4 0.9);
LABEL (.4 0.8)(.4 0.8);
LABEL (.4 0.7)(.4 0.7);
LABEL (.4 0.6)(.4 0.6);
LABEL (.4 0.5)(.4 0.5);

ADD PINHD-1x25@pinhead (-1 -0.8);
NET A4 (-1.1 -2.0) (-1.3 -2.0);
NET PE (-1.1 -1.9) (-1.3 -1.9);
NET A5 (-1.1 -1.8) (-1.3 -1.8);
NET PE (-1.1 -1.7) (-1.3 -1.7);
NET 13 (-1.1 -1.6) (-1.3 -1.6);
NET PE (-1.1 -1.5) (-1.3 -1.5);
NET 30 (-1.1 -1.4) (-1.3 -1.4);
NET PE (-1.1 -1.3) (-1.3 -1.3);
NET 27 (-1.1 -1.2) (-1.3 -1.2);
NET PE (-1.1 -1.1) (-1.3 -1.1);
NET SCL (-1.1 -1.0) (-1.3 -1.0);
NET PE (-1.1 -0.9) (-1.3 -0.9);
NET MOSI (-1.1 -0.8) (-1.3 -0.8);
NET MISO (-1.1 -0.7) (-1.3 -0.7);
NET RESET (-1.1 -0.6) (-1.3 -0.6);
NET EN (-1.1 -0.5) (-1.3 -0.5);
NET +3V3_2 (-1.1 -0.4) (-1.3 -0.4);
NET PE (-1.1 -0.3) (-1.3 -0.3);
NET PE (-1.1 -0.2) (-1.3 -0.2);
NET TXD (-1.1 -0.1) (-1.3 -0.1);
NET RXD (-1.1 0.0) (-1.3 0.0);
NET DFU (-1.1 0.1) (-1.3 0.1);
NET BAT (-1.1 0.2) (-1.3 0.2);
NET USB (-1.1 0.3) (-1.3 0.3);
NET +3V3 (-1.1 0.4) (-1.3 0.4);

LABEL (-1.1 -2.0) (-1.5 -2.0);
LABEL (-1.1 -1.9) (-1.5 -1.9);
LABEL (-1.1 -1.8) (-1.5 -1.8);
LABEL (-1.1 -1.7)(-1.5 -1.7);
LABEL (-1.1 -1.6)(-1.5 -1.6);
LABEL (-1.1 -1.5)(-1.5 -1.5);
LABEL (-1.1 -1.4)(-1.5 -1.4);
LABEL (-1.1 -1.3)(-1.5 -1.3);
LABEL (-1.1 -1.2)(-1.5 -1.2);
LABEL (-1.1 -1.1)(-1.5 -1.1);
LABEL (-1.1 -1.0)(-1.5 -1.0);
LABEL (-1.1 -0.9)(-1.5 -0.9);
LABEL (-1.1 -0.8)(-1.5 -0.8);
LABEL (-1.1 -0.7)(-1.5 -0.7);
LABEL (-1.1 -0.6)(-1.5 -0.6);
LABEL (-1.1 -0.5)(-1.5 -0.5);
LABEL (-1.1 -0.4)(-1.5 -0.4);
LABEL (-1.1 -0.3)(-1.5 -0.3);
LABEL (-1.1 -0.2)(-1.5 -0.2);
LABEL (-1.1 -0.1)(-1.5 -0.1);
LABEL (-1.1 0.0)(-1.5 0.0);
LABEL (-1.1 0.1)(-1.5 0.1);
LABEL (-1.1 0.2)(-1.5 0.2);
LABEL (-1.1 0.3)(-1.5 0.3);
LABEL (-1.1 0.4)(-1.5 0.4);


ADD PINHD-1X2@pinhead (2 1);
NET MCP_INT (1.9 1.1) (1.6 1.1);
NET 27 (1.9 1.0) (1.6 1.0);

LABEL (1.6 1.1) (1.2 1.1);
LABEL (1.6 1.0) (1.4 1.0);

ADD FH12-12S-0.5SH (3.7 1.3);
NET +3V3 (3.6 1.8) (3.5 1.8);
NET MISO (3.6 1.7) (3.5 1.7);
NET MOSI (3.6 1.6) (3.5 1.6);
NET PE (3.6 0.7) (3.5 0.7);

LABEL (3.5 1.8)(3.2 1.8);
LABEL (3.5 1.7)(3.2 1.7);
LABEL (3.5 1.6)(3.2 1.6);
LABEL (3.5 0.7)(3.2 0.7);

""")

# MCP IO Expanders
cursor_x = 0
cursor_y = 0
for h in range(6):
    name = ("MCP-%s" % (h))
    f2.write("ADD MCP23017SS@adafruit %s (%s %s);\n" % (name, round (cursor_x, 11), round (cursor_y, 11)))

    # Ground (VSS / PE)
    f2.write("NET PE (%s %s) (%s %s);\n" % (round (cursor_x - .5, 11), 
                                            round (cursor_y - .8, 11), 
                                            round (cursor_x - .9, 11), 
                                            round (cursor_y - .8, 11)))

    f2.write("ADD PE@supply1 (%s %s);\n" % (round(cursor_x - .9, 11), 
                                            round(cursor_y - .9, 11)))

    # Power (VDD / +3V3)
    f2.write("NET +3V3 (%s %s) (%s %s);\n" % (round (cursor_x - .5, 11), 
                                            round (cursor_y + .8, 11), 
                                            round (cursor_x - 1.0, 11), 
                                            round (cursor_y + .8, 11)))

    f2.write("ADD +3V3@supply1 (%s %s);\n" % (round(cursor_x - 1.0, 11), 
                                            round(cursor_y + .9, 11)))

    # Address Pins
    for i in range(3):
        # Value of current bit
        value = h >> i & 1

        if value:
            f2.write("NET +3V3 (%s %s) (%s %s);\n" % (round (cursor_x - .5, 11), 
                                                    round (cursor_y - (i * .1) - .4, 11), 
                                                    round (cursor_x - 1.0, 11), 
                                                    round (cursor_y - (i * .1) - .4, 11)))
            f2.write("NET +3V3 (%s %s) (%s %s);\n" % (round (cursor_x - 1.0, 11), 
                                                    round (cursor_y + .8, 11), 
                                                    round (cursor_x - 1.0, 11), 
                                                    round (cursor_y - (i * .1) - .4, 11)))

        else:
            f2.write("NET PE (%s %s) (%s %s);\n" % (round (cursor_x - .5, 11), 
                                                    round (cursor_y - (i * .1) - .4, 11), 
                                                    round (cursor_x - .9, 11), 
                                                    round (cursor_y - (i * .1) - .4, 11)))
            f2.write("NET PE (%s %s) (%s %s);\n" % (round (cursor_x - .9, 11), 
                                                    round (cursor_y - .8, 11), 
                                                    round (cursor_x - .9, 11), 
                                                    round (cursor_y - (i * .1) - .4, 11)))
    # Reset NET
    f2.write("NET MCP_INT (%s %s) (%s %s);\n" % (round (cursor_x - .5, 11), 
                                            round (cursor_y + .4, 11), 
                                            round (cursor_x - .6, 11), 
                                            round (cursor_y + .4, 11)))

    f2.write("LABEL (%s %s) (%s %s);\n" % (round (cursor_x - .6, 11), 
                                            round (cursor_y + .4, 11), 
                                            round (cursor_x - 1.0, 11), 
                                            round (cursor_y + .4, 11))) 

    # Interrupt NET
    f2.write("NET MCP_INT (%s %s) (%s %s);\n" % (round (cursor_x - .5, 11), 
                                            round (cursor_y + .4, 11), 
                                            round (cursor_x - .6, 11), 
                                            round (cursor_y + .4, 11)))

    f2.write("LABEL (%s %s) (%s %s);\n" % (round (cursor_x - .6, 11), 
                                            round (cursor_y + .4, 11), 
                                            round (cursor_x - 1.0, 11), 
                                            round (cursor_y + .4, 11))) 

    # I2C Pins
    f2.write("NET SCL (%s %s) (%s %s);\n" % (round (cursor_x - .5, 11), 
                                            round (cursor_y - .1, 11), 
                                            round (cursor_x - .6, 11), 
                                            round (cursor_y - .1, 11)))

    f2.write("LABEL (%s %s) (%s %s);\n" % (round (cursor_x - .6, 11), 
                                            round (cursor_y - .1, 11), 
                                            round (cursor_x - .8, 11), 
                                            round (cursor_y - .1, 11)))


    f2.write("NET SDA (%s %s) (%s %s);\n" % (round (cursor_x - .5, 11), 
                                            round (cursor_y - .2, 11), 
                                            round (cursor_x - .6, 11), 
                                            round (cursor_y - .2, 11)))

    f2.write("LABEL (%s %s) (%s %s);\n" % (round (cursor_x - .6, 11), 
                                            round (cursor_y - .2, 11), 
                                            round (cursor_x - .8, 11), 
                                            round (cursor_y - .2, 11)))



    # Connect each pin to the proper switch network
    for i in range (8):
        f2.write("NET SW-%s (%s %s) (%s %s);\n" % (i + (h * 16), 
                                                round (cursor_x + .5, 11), 
                                                round (cursor_y - (i * .1) + .8, 11), 
                                                round (cursor_x + .6, 11), 
                                                round (cursor_y - (i * .1) + .8, 11)))
        f2.write("LABEL (%s %s) (%s %s);\n" % (round (cursor_x + .6, 11), 
                                                round (cursor_y - (i * .1) + .8, 11), 
                                                round (cursor_x + .6, 11), 
                                                round (cursor_y - (i * .1) + .8, 11)))

    for i in range (8):
        f2.write("NET SW-%s (%s %s) (%s %s);\n" % (i + (h * 16) + 8, 
                                                round (cursor_x + .5, 11), 
                                                round (cursor_y - (i * .1) - .1 , 11), 
                                                round (cursor_x + .6, 11), 
                                                round (cursor_y - (i * .1) - .1, 11)))
        f2.write("LABEL (%s %s) (%s %s);\n" % (round (cursor_x + .6, 11), 
                                                round (cursor_y - (i * .1) - .1, 11), 
                                                round (cursor_x + .6, 11), 
                                                round (cursor_y - (i * .1) - .1, 11)))

    cursor_x = cursor_x + 2.2

cursor_x = 0
cursor_y = 0
num = 0
for h in data:
    for i in h:

        name = "SW-" + i.get("n")
        units = (i.get("s") or 1.0) 
        part = "CHERRY_MX_WITH_FIXING_PINS" if units < 2 else "CHERRY_MX_WITH_FIXING_PINS_&_STABILIZER_%sX" % (2 if units <= 2.25 else units)

        cursor_x = round(cursor_x + (0.4 * units), 11)

        f3.write("ADD %s %s (%s %s);\n" % (part, name, cursor_x, cursor_y))
        f3.write("NET SW-%s (%s %s)(%s %s);\n" % (num,
                                        round(cursor_x - .2, 11), 
                                        round(cursor_y + .2, 11), 
                                        round(cursor_x - .3, 11), 
                                        round(cursor_y + .2, 11)))

        f3.write("LABEL (%s %s)(%s %s);\n" % (round(cursor_x - .3, 11), 
                                        round(cursor_y + .2, 11),
                                        round(cursor_x - .55, 11), 
                                        round(cursor_y + .2, 11)))

        f3.write("NET PE (%s %s)(%s %s);\n" % (round(cursor_x + .2, 11), 
                                        round(cursor_y - .2, 11),
                                        round(cursor_x + .3, 11), 
                                        round(cursor_y - .2, 11)))

        f3.write("ADD PE@supply1 (%s %s);\n" % (round(cursor_x + .3, 12), 
                                                round(cursor_y - .3, 11)))

        # If you want to set the value, you can do this:
        #f3.write("VALUE %s %s;\n" % (name, i.get("n")))

        cursor_x = round(cursor_x + (0.4 * units), 13)
        num = num + 1
    cursor_x = 0
    cursor_y = cursor_y - 1


f4.write("MOVE (%smm %smm) (%smm %smm);\n" % (160, 50, BOARD_X, 50))
f4.write("MOVE (%smm %smm) (%smm %smm);\n" % (round(BOARD_X / 2, 10), 100, round(BOARD_X / 2, 10), round(BOARD_Y, 11)))


f4.write("MOVE LEFT_WHEEL (%smm %smm);\n" % (round(25.4 / 2, 11) + 1, 
                                                round(BOARD_Y, 11) - round(25.4 / 2, 11) - 1))
f4.write("MOVE RIGHT_WHEEL (%smm %smm);\n" % (round(BOARD_X ,11) - round(25.4 / 2, 11) - 1, 
                                                round(BOARD_Y, 11) - round(25.4 / 2, 11) - 1))

# Joystick X is centered on the side buffer size with 1mm of offset from side.  
# Joystick Y (from top) is joystick width + buffer + scroll wheel height + another offset
f4.write("MOVE LEFT_JOYSTICK (%smm %smm);\n" % (round((30.48 / 2) + 1, 11), 
                                                round(BOARD_Y, 11) - round(30.48 / 2, 11) - 2 - 25.4 - 20))
f4.write("MOVE RIGHT_JOYSTICK (%smm %smm);\n" % (round(BOARD_X ,11) - round(30.48 / 2, 11) - 1, 
                                                round(BOARD_Y, 11) - round(30.48 / 2, 11) - 2 - 25.4 - 20))

f4.write("MIRROR JP1;\n")
f4.write("MIRROR JP2;\n")
f4.write("MOVE JP1 (-33.02mm 314.96mm);\n")
f4.write("MOVE JP2 (-27.94mm 292.10mm);\n")
f4.write("ROTATE JP1; ROTATE JP1;\n")
f4.write("ROTATE JP2; ROTATE JP2;\n")

cursor_x = OFFSET_X
cursor_y = OFFSET_Y
for h in data:
    for i in h:
        # Read key params from JSON
        name = "SW-" + i.get("n")
        width = (i.get("s") or 1.0) * UNIT
        
        # Add half width (position is from center)
        cursor_x = round(cursor_x + (width / 2.0), 11)

        # Generate move command
        f4.write("MOVE %s (%smm %smm);\n" % (name, round(cursor_x, 11), round(cursor_y, 11)))
        f4.write("ROTATE %s;\n" % (name))
        f4.write("ROTATE %s;\n" % (name))

        # Move the cursor to the blank space
        cursor_x = round(cursor_x + (width / 2.0), 11)
    cursor_x = OFFSET_X
    cursor_y = round(cursor_y - UNIT, 11)

    f4.write("GRID MM 2.54 lines on alt MM 2.54 MM;\n")


    f4.write("HOLE 2mm (%smm %smm);\n" % (2, -40 - 21))
    f4.write("HOLE 2mm (%smm %smm);\n" % (2, -40 - 45))
    f4.write("HOLE 2mm (%smm %smm);\n" % (95, -40 - 21))
    f4.write("HOLE 2mm (%smm %smm);\n" % (95, -40 - 45))
    f4.write("RECT (%smm %smm) (%smm %smm);\n" % (0, -40, 98, -40 - 70))