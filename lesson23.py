from typing import Optional
from typing import Any
from typing import Union
from typing import List

def process_anything(value: Any) -> str:
    return f"Processed {value}"
print(process_anything)

def proscess_value(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Number:{value}"
    return f"String: {value}"
print(proscess_value("Digital School"))

def  sum_list(numbers: List[int]) -> int:
    return sum(numbers)

numbers: List[int] = [1,2,3,4]
result: List = sum_list(numbers)
print(result)