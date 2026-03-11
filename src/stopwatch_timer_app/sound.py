import platform
import os


def play_alarm():

    if platform.system() == "Windows":

        import winsound
        winsound.Beep(1000, 500)

    else:

        os.system("printf '\\a'")
