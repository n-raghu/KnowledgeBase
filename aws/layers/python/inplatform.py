import platform


def pinfo():
    return {
        'machine': platform.machine(),
        'uname': platform.uname()
    }


if __name__ == '__main__':
    print(pinfo())
