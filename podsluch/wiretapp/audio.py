from pygame import mixer


def play(path):
    # Starting the mixer
    mixer.init()
    # Loading the song
    mixer.music.load(path)
    # Setting the volume
    mixer.music.set_volume(0.7)
    # Start playing the song
    mixer.music.play()


def stop():
    mixer.music.pause()

def unpause():
    mixer.music.unpause()

def exit():
    mixer.music.stop()


if __name__ == "__main__":

    play("../podsluchDjango/podsluch/wiretapp/static/records/1.mp3")
    # infinite loop
    while True:

        print("Press 'p' to pause, 'r' to resume")
        print("Press 'e' to exit the program")
        query = input("  ")

        if query == 'p':
            # Pausing the music
            stop()
        elif query == 'r':
            unpause()
            # Resuming the music

        elif query == 'e':
            exit()
            # Stop the mixer
            break
