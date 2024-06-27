
from src.operation import Operation
from src import utils as u


def main():
    #данные из файла джейсон
    list_operations = u.get_operations()
    #редактор файла для создания классов
    operations_edited = u.edit_operations(list_operations)
    #Сортировать операций по дате
    sorted_operations = u.sort_operations(operations_edited)
    #извлечение количества операций
    last_operations = u.show_last_operation(sorted_operations, 5)
    #создать классы из списка
    operations = Operation.from_dict(last_operations)
    return [x for x in operations]


if __name__ == "__main__":
    transactions = main()
    for operation in transactions:
        print(
            f"{operation.edit_date()} {operation.description} \n"
            f"{operation.hide_card_numbers(operation.come_from)} -> {operation.hide_account_numbers(operation.to)}\n"
            f"{operation.operationAmount['amount']} {operation.operationAmount['currency']['name']}\n"
        )