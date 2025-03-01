
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Operation:
    """"""
    id: int
    state: str
    date: str
    operationAmount: dict
    description: str
    to: str
    come_from: str = None

    @classmethod
    def from_dict(cls, array: list) -> list:
        """список экземпляров класса"""
        return [Operation(**x) for x in array]

    def edit_date(self) -> str:
        """формат времени"""
        date = datetime.fromisoformat(self.date)
        format = "%d.%m.%Y"
        return date.strftime(format)

    def hide_card_numbers(self, come_from: str) -> str:
        """строка со скрытыми номерами карт"""
        if come_from:
            account_info = "".join(x for x in self.come_from if not x.isnumeric())
            card_nums = "".join(x for x in self.come_from if x.isnumeric())
            return f"{account_info}{card_nums[:4]} {card_nums[4:6]}** **** {card_nums[-4:]}"

    def hide_account_numbers(self, to: str) -> str:
        """строка со скрытыми номерами счетов"""
        account_info = "".join(x for x in self.to if x.isalpha())
        return f"{account_info} **{self.to[-4:]}"