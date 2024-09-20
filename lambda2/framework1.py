print("# 2 FRAMEWORK1 OPCAO A ")
from src.routes import route1


def post_http():
    http_message = {
        "HTTP_method": "POST",
        "HTTP_header": [
            ("token", "Bearer jioiaefi48904729kldan324"),
            ("origin", "http://something.other.org")
        ],
        "HTTP_body": [
            ("name", "Lhama"),
            ("message", "Hello Word")
        ]
    }

    """
    http_message = {
            "method": "POST",
            "header": {
                "token": "Bearer jioiaefi48904729kldan324",
                "origin": "http://something.other.org"
            },
            "body": {
                "name": "Lhama",
                "message": "Hello Word"
            }
        }
    """
    
    route1(http_message)
