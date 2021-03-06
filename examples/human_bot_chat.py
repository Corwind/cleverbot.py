"""Chat with Cleverbot in Python."""
import traceback

import cleverbot3


def main():
    # instantiate a Cleverbot object
    cleverbot_client = cleverbot3.Cleverbot()

    while True:
        question = input('>> You: ')
        answer = cleverbot_client.ask(question)
        print('>> Cleverbot: {}'.format(answer))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('>> Exiting...')
    except Exception as err:
        print(traceback.format_exc(err))
