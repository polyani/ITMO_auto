def task_1() -> str:
    v_str: str = 'Мур'
    v_int: int = 8
    v_float: float = 3.8
    v_list: list = [10,20,30]
    v_bool: bool = False

    print(v_str, " относится к типу ", type(v_str),'\n')
    print(v_int, " относится к типу ",type(v_int),'\n')
    print(v_float, " относится к типу ",type(v_float),'\n')
    print(v_list, " относится к типу ",type(v_list),'\n')
    print(v_bool, " относится к типу ",type(v_bool),'\n')

def task_2() -> int:
    a = [1, 2, 3, 5, 8, 13, 21]
    print (a[0:3])

def task_3(a: int)-> int:
    return (a ** 2)

task_1()
task_2()
print ('\n Квадрат числа равен ',task_3(2))