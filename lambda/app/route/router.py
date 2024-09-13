from ..controllers.controller import write_in_database
from ..helper.adapter import Adapter


def route1(message):
    processo = Adapter(Code())
    processo.handle(message)


class Code():

    def handle(self, message):
        token = message['header']['token']

        if token:
            print('Autentificando o Token')
            write_in_database(
                message['body']['name'],
                message['body']['message']
            )
