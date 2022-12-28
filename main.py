from pyjoystick.sdl2 import Key, Joystick, run_event_loop
import pyvjoy

FORBIDDEN_LIST = ["Up Left", "Up Right", "Down Left", "Down Right", "Centered"]
vJoyDeviceOutput = pyvjoy.VJoyDevice(2)

def DUMMY():
    print("")

# TMS
def TMS_UP():
    vJoyDeviceOutput.set_button(1, 1)

def TMS_DOWN():
    vJoyDeviceOutput.set_button(2, 1)

def TMS_RIGHT():
    vJoyDeviceOutput.set_button(3, 1)

def TMS_LEFT():
    vJoyDeviceOutput.set_button(4, 1)

# DMS
def DMS_UP():
    vJoyDeviceOutput.set_button(5, 1)

def DMS_DOWN():
    vJoyDeviceOutput.set_button(6, 1)

def DMS_RIGHT():
    vJoyDeviceOutput.set_button(7, 1)

def DMS_LEFT():
    vJoyDeviceOutput.set_button(8, 1)

# CHINA HAT
def CH_FORWARD():
    vJoyDeviceOutput.set_button(9, 1)

def CH_AFT():
    vJoyDeviceOutput.set_button(10, 1)

# BOAT SWITCH
def BS_FORWARD():
    vJoyDeviceOutput.set_button(11, 1)

def BS_AFT():
    vJoyDeviceOutput.set_button(12, 1)

def BS_CENTER():
    vJoyDeviceOutput.set_button(13, 1)

# HAT
def HAT_UP():
    vJoyDeviceOutput.set_button(14, 1)

def HAT_DOWN():
    vJoyDeviceOutput.set_button(15, 1)

def HAT_RIGHT():
    vJoyDeviceOutput.set_button(16, 1)

def HAT_LEFT():
    vJoyDeviceOutput.set_button(25, 1)

# SLEW
def SLEW_UP():
    vJoyDeviceOutput.set_button(26, 1)

def SLEW_DOWN():
    vJoyDeviceOutput.set_button(27, 1)

def SLEW_RIGHT():
    vJoyDeviceOutput.set_button(28, 1)

def SLEW_LEFT():
    vJoyDeviceOutput.set_button(29, 1)

# SOI
def SOI_UP():
    vJoyDeviceOutput.set_button(30, 1)

def SOI_RIGHT():
    vJoyDeviceOutput.set_button(31, 1)

def SOI_LEFT():
    vJoyDeviceOutput.set_button(32, 1)


mode = {"active": None}
guide = {
    16: { # TMS
        "Up": TMS_UP,
        "Down": TMS_DOWN,
        "Right": TMS_RIGHT,
        "Left": TMS_LEFT
    },
    17: { # DMS
        "Up": DMS_UP,
        "Down": DMS_DOWN,
        "Right": DMS_RIGHT,
        "Left": DMS_LEFT
    },
    1: { # CHINA HAT
        "Up": CH_FORWARD,
        "Down": CH_AFT,
        "Right": DUMMY,
        "Left": DUMMY
    },
    2: { # BOAT SWITCH 
        "Up": BS_FORWARD,
        "Down": BS_AFT,
        "Right": BS_CENTER,
        "Left": BS_CENTER
    },
    20: { # HAT
        "Up": HAT_UP,
        "Down": HAT_DOWN,
        "Right": HAT_RIGHT,
        "Left": HAT_LEFT
    },
    19: { # SLEW
        "Up": SLEW_UP,
        "Down": SLEW_DOWN,
        "Right": SLEW_RIGHT,
        "Left": SLEW_LEFT
    },
    18: { # SOI
        "Up": SOI_UP,
        "Down": DUMMY,
        "Right": SOI_RIGHT,
        "Left": SOI_LEFT
    }
}

devices = Joystick.get_joysticks()
print("Devices:", devices)
def print_add(joy):
    print('Added', joy)

def print_remove(joy):
    print('Removed', joy)


def key_received(key):

    #if key.number == 0:
        #print("yw")

    if key.keytype != Key.AXIS:
        print(f"-------\nValue: {key.value}\nNumber: {key.number}\nType: {key.keytype}")
        if key.number >= 16 and key.number <= 20 or key.number == 2 or key.number == 1 and key.keytype == Key.BUTTON:
            #print("switching")
            mode["active"] = key.number
    if key.keytype == Key.HAT:
        hat_type = key.get_hat_name()
        if mode["active"] != None and hat_type not in FORBIDDEN_LIST:
            for i in range(32):
                vJoyDeviceOutput.set_button(i+1, 0)
            guide[mode["active"]][hat_type]()
        if hat_type == "Centered":
            for i in range(32):
                vJoyDeviceOutput.set_button(i+1, 0)

    #print(mode)

run_event_loop(print_add, print_remove, key_received)
