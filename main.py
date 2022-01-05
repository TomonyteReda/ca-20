import math
from typing import Union, Optional
import logging

logging.basicConfig(filename="log_file.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


def sum_arguments(*args: Union[int, float]) -> Union[int, float]:
    result = sum(args)
    logging.info(f"Sum {args} = {result}")
    return result


def get_sqrt_root(num: Union[int, float]) -> Optional:
    try:
        result = math.sqrt(num)
        logging.info(f"Square root of {num} = {result}")
    except TypeError as e:
        logging.error(f"expected int got {type(num)}")
    else:
        return result


def get_number_of_chars(s: str) -> int:
    result = len(s)
    logging.info(f"Number of symbols in {s}: {result}")
    return result


def get_division(x: Union[int, float], y: Union[int, float]) -> Optional:
    try:
        result = x / y
        logging.info(f"{x} / {y} = {result}")
    except ZeroDivisionError as e:
        logging.error("Division by 0")
    else:
        return result


if __name__ == "__main__":
    print(sum_arguments(1, 2.7, 3, 5))
    print(get_sqrt_root("labas"))
    print(get_number_of_chars("Labas vakaras!"))
    print(get_division(200, 0))
