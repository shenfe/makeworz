import platform

def os_type():
    t = platform.system()
    print("platform is ", t)
    if t == 'Windows':
        return 0
    return 1
