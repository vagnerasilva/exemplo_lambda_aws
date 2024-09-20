print("# 3 ROUTES ")

from .controller import write_in_database
from .helper.adapter import Adapter


def route1(message):
    print("         ## CHAMANDO ADAPTER ##")
    processo = Adapter(Code())
    processo.handle(message)
    return True


class Code():

    def handle(self, message):
        token = message['header']['token']

        if token:
            print('Autentificando com o Token')
            write_in_database(
                message['body']['name'],
                message['body']['message']
            )
