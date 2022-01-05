import math
from typing import Union, Optional
import logging


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("log_file.log")
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# logging in terminal
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def sum_arguments(*args: Union[int, float]) -> Union[int, float]:
    result = sum(args)
    logger.info(f"Sum {args} = {result}")
    return result


def get_sqrt_root(num: Union[int, float]) -> float:
    try:
        result = math.sqrt(num)
        logger.info(f"Square root of {num} = {result}")
    except TypeError as e:
        logger.error(f"expected int got {type(num)}")
    else:
        return float(result)


def get_number_of_chars(s: str) -> int:
    result = len(s)
    logger.info(f"Number of symbols in {s}: {result}")
    return result


def get_division(x: Union[int, float], y: Union[int, float]) -> float:
    try:
        result = x / y
        logger.info(f"{x} / {y} = {result}")
    except ZeroDivisionError as e:
        logger.error("Division by 0")
    else:
        return float(result)


print(sum_arguments(1, 2.7, 3, 5))
print(get_sqrt_root("labas"))
print(get_number_of_chars("Labas vakaras!"))
print(get_division(200, 0))
