
import lib.constants as const

def log_keys(win32api):
    keys = []
    for key in const.keyList:
        if win32api.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys
 

def get_keys(win32api):
    keys=log_keys(win32api)
    output =const.nk
    if  'W' in keys and 'A' in keys:
        output = const.wa
    elif 'W' in keys and 'D' in keys:
        output = const.wd
    elif 'S' in keys and 'A' in keys:
        output = const.sa
    elif 'S' in keys and 'D' in keys:
        output = const.sd
    elif 'W' in keys:
        output = const.w
    elif 'S' in keys:
        output = const.s
    elif 'A' in keys:
        output = const.a
    elif 'D' in keys:
        output = const.d
    return output
