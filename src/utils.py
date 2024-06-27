
import json
from pathlib import Path


def get_operations() -> list:
    """возвращаем список операций клиента"""
    path = Path("../data/operations.json")
    content = path.read_text()
    data = json.loads(content)
    return data


def edit_operations(data: list) -> list:
    """Возвращает отредактированный список операций"""
    lst = [x for x in data if x.get("from")]
    for operation in lst:
        operation["come_from"] = operation.pop("from")
    return lst


def sort_operations(data: list) -> list:
    """возвращаем отсортированный по датам список"""
    lst = [x for x in data if x.get("date")]
    return sorted(lst, key=lambda x: x["date"], reverse=True)


def show_last_operation(data: list, number: int) -> list:
    """возвращаем список последних операций операций"""
    return [x for x in data[0: number + 1] if x["state"] == "EXECUTED"]