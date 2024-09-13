import logging
import os
from http import HTTPStatus
from app import processor

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# VALUE_GLOBAL = os.environ['VALUE_GLOBAL']
VALUE_GLOBAL = "VALOR_GLOBAL"


def lambda_handler(event, context):
    response = processor.lambda_processor(event, context)

    return response
