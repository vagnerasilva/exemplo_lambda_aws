import logging
import os
from http import HTTPStatus


logger = logging.getLogger()
logger.setLevel(logging.INFO)

# VALUE_GLOBAL = os.environ['VALUE_GLOBAL']
VALUE_GLOBAL = "VALOR_GLOBAL"


def lambda_handler(event, context):
    try:
        logger.info(f'Entrada do handler da lambda {VALUE_GLOBAL} ')
        value = ""
        logger.info('Retorno da chamada {}, retornado output ...'.format(len(value))) # noqa E501

    except Exception as e:  # Catch all for easier error tracing in logs
        logger.error(e, exc_info=True)
        raise Exception('Error durante execucao')  # notify aws of failure

    return {
        "statusCode": HTTPStatus.OK.value
    }


print(lambda_handler("", ""))
