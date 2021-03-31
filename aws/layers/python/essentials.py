import os


def osinfo():
    return {
        'name': os.name,
        'pid': os.getpid(),
    }


if __name__ == '__main__':
    print(osinfo())
