#Below code shows automatically what type of data ar variable use 

from typing import List, Tuple, Union

#list of integer
number: List[int] = [1, 2, 3, 4, 5]

#Tuple of string and integer
person: Tuple[str, int] = ("Naimul", 8)

#Dictionary with string keys and integer valus 
scores: dict[str, int] = {"Naimul": 98, "Rup": 99}

#Union type variable that can holes multiple types 
identifier: Union[str, int] = "PI008"
identifier = 665232 #also valid

n : int = 5

name : str = "Naimul"

#using in function
def sum(a: int, b: int) -> int:
    return a+b