def create_success_response(data: dict) -> dict:
    return {
        "status": "ok",
        **data,
    }


def create_error_response(code: int, message: str) -> dict:
    return {
        "status": "error",
        "error": {
            "code": code,
            "message": message,
        },
    }
