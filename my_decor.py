from datetime import datetime, date, time
import os


def logger(file_name, file_path=None):
    if file_path is None:
        file_place = os.path.join(os.getcwd())
    else:
        file_place = os.path.join(os.path.abspath(file_path))

    file_path = os.path.join(file_place, file_name)

    def log_func(funcion):

        def result_func(*args, **kwargs):
            date_func = datetime.today()
            func_name = funcion.__name__
            input_d = f'вводные данные {args} {kwargs}'
            output = funcion(*args, **kwargs)
            result = f'вызвана функция {func_name} \n' \
                     f'дата и время вызова : {date_func} \n' \
                     f'{input_d} \n' \
                     f'результирующее значение функции {func_name}: {output}\n' \
                     f'-----------------------------------\n'

            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(result)

            return output

        return result_func

    return log_func
