from typing import TypeVar, Union


StrangeType = TypeVar('StrangeType', str, int)


def mult_value(val: Union[str, bytes]) -> Union[str, bytes]:
    return val * 2


val = mult_value('A')
print(val + '!')