from typing import Any
from dataclasses import asdict
from strawberry.arguments import is_unset


def data_to_dict(data: Any) -> dict:
    valid_items = {}

    for key, value in asdict(data).items():
        if is_unset(value):
            continue
        valid_items[key] = value

    return valid_items