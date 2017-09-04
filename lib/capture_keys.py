
import lib.constants as const

def log_keys(win32api):
    keys = []
    for key in const.keyList:
        if win32api.GetAsyncKeyState(ord(key)):
            print(key,end='-')
            keys.append(key)
    return keys
 

def get_keys(win32api):
    keys=log_keys(win32api)
    output =const.nk
    if 'A' in keys:
        output = const.a
    elif 'D' in keys:
        output = const.d
    elif 'W' in keys:
        output = const.w
    elif 'S' in keys:
        output = const.s
    return output

