from app.route import router


def post_http():
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

    router.route1(http_message)
