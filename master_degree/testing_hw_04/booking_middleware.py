import logging
from functools import wraps

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def booking_middleware(func):
    """
    Декоратор, который логирует:
    - факт вызова функции и ее аргументы (event_id, user_id, booking_id)
    - успешный результат
    - ошибки ValueError/KeyError с повторным пробросом
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__

        event_id = kwargs.get("event_id")
        user_id = kwargs.get("user_id")
        booking_id = kwargs.get("booking_id")

        if func_name == "create_booking":
            if event_id is None and len(args) >= 1:
                event_id = args[0]
            if user_id is None and len(args) >= 2:
                user_id = args[1]
        elif func_name == "get_booking":
            if booking_id is None and len(args) >= 1:
                booking_id = args[0]

        logger.info(
            "Calling %s with event_id=%s, user_id=%s, booking_id=%s",
            func_name,
            event_id,
            user_id,
            booking_id,
        )

        try:
            result = func(*args, **kwargs)
            logger.info(
                "Function %s finished successfully",
                func_name,
            )
            return result
        except (ValueError, KeyError) as exc:
            logger.error(
                "Error in %s: %s (type=%s)", func_name, exc, type(exc).__name__
            )
            raise

    return wrapper
