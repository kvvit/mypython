#!/usr/bin/env python3
"""
Консольное приложение для тестового задания по разделу QA учебного курса REBRAINME (http://rebrainme.com/)
"""
import sys
import logging
import re


# Глобальные константы
OPERATORS = {
    '+': lambda a, b : a + b,
    '-': lambda a, b : a - b,
    '*': lambda a, b : a * b,
    '**': lambda a, b : a ** b,
    '/': lambda a, b : a / b
}

# Функция обработчики
def usage():
    logging.info("""
    Сомнительный калькулятор®
    Использование:
    {} NUM1,OPERATOR,NUM2
    Поддерживаемые операторы:
    {}

    Пример использования:
    {} 1,+,2
    """.format(sys.argv[0], ','.join(OPERATORS.keys()), sys.argv[0]))

def calculate(command):
    command_splitted = command.split(',')
    logging.info("Разделенная на аргументы команда: {}".format(command_splitted))

    arg1 = command_splitted[0]
    operator = command_splitted[1]
    arg2 = command_splitted[2]

    # Проверяем оператор, в зависимости от результата проверки - возвращаем разный error_code
    if operator in OPERATORS:
        return OPERATORS[operator](int(arg1), int(arg2)), 0
    else:
        return -1, 1

# Основаная часть
if __name__ == '__main__':
     # Настраиваем логгирование
    LOGGER = logging.getLogger()
    LOGGER.level = logging.DEBUG
    # -> Обработчик сообщений уровня INFO
    STDOUT_HANDLER = logging.StreamHandler(sys.stdout)
    STDOUT_HANDLER.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
        )
    STDOUT_HANDLER.setLevel(logging.DEBUG)
    STDOUT_HANDLER.addFilter(lambda record: record.levelno <= logging.INFO)
    # -> Обработчик сообщений уровня ERROR
    STDERR_HANDLER = logging.StreamHandler(sys.stderr)
    STDERR_HANDLER.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
        )
    STDERR_HANDLER.setLevel(logging.WARNING)
    # -> Добавляем обработчики в Logger
    LOGGER.addHandler(STDOUT_HANDLER)
    LOGGER.addHandler(STDERR_HANDLER)

    # Проверяем ввод
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    # Теперь проверка операторов вынесена в отдельный блок, так что делаем wildcard
    if not re.match(r'^-?[0-9]\d*(\.\d+)?,.+,-?[0-9]\d*(\.\d+)?$', sys.argv[1]):
        logging.error("Некорректный ввод")
        usage()
        sys.exit(1)

    # Вызываем функцию подсчета
    result, error_code = calculate(sys.argv[1])
    if error_code == 0:
        logging.info(result)
    elif error_code == 1:
        logging.error("Некорректный оператор")
        usage()
        sys.exit(1)
