from src.tasker.handler import BasicTaskerHandler


def main():
    handler = BasicTaskerHandler()
    while 1:
        stdin = input("Write a command: ")
        handler.route_command(stdin)


if __name__ == "__main__":
    main()
