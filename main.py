import modules.Controller as ctr
from time import sleep


def main():
    input = ctr.get_input()
    print(input)
    sleep(0.1)

if __name__ == '__main__':
    while True:
        main()
