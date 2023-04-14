# Code For Mac
import os
if __name__ == '__main__':
    print('Welcome To Robo Speaker 1.2.')
    print("Write 'iai' to exit")
    while True:
        x = input('Enter Here What Do Want Me To Speak: ')
        if x == "iai":
            break
        command = f"say {x}"
        os.system(command)
