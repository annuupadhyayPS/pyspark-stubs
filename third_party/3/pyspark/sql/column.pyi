# Stubs for pyspark.sql.column (Python 3.5)
#

from typing import Any, Union
from pyspark.sql.types import *
from pyspark.sql.window import Window

class Column:
    def __init__(self, jc) -> None: ...
    def __neg__(self) -> 'Column': ...
    def __add__(self, other: Any) -> 'Column': ...
    def __sub__(self, other: Any) -> 'Column': ...
    def __mul__(self, other: Any) -> 'Column': ...
    def __div__(self, other: Any) -> 'Column': ...
    def __truediv__(self, other: Any) -> 'Column': ...
    def __mod__(self, other: Any) -> 'Column': ...
    def __radd__(self, other: Any) -> 'Column': ...
    def __rsub__(self, other: Any) -> 'Column': ...
    def __rmul__(self, other: Any) -> 'Column': ...
    def __rdiv__(self, other: Any) -> 'Column': ...
    def __rtruediv__(self, other: Any) -> 'Column': ...
    def __rmod__(self, other: Any) -> 'Column': ...
    def __pow__(self, other: Any) -> 'Column': ...
    def __rpow__(self, other: Any) -> 'Column': ...
    def __eq__(self, other: Any) -> 'Column': ...  # type: ignore  
    def __ne__(self, other: Any) -> 'Column': ...  # type: ignore 
    def __lt__(self, other: Any) -> 'Column': ...
    def __le__(self, other: Any) -> 'Column': ...
    def __ge__(self, other: Any) -> 'Column': ...
    def __gt__(self, other: Any) -> 'Column': ...
    def __and__(self, other: Any) -> 'Column': ...
    def __or__(self, other: Any) -> 'Column': ...
    def __invert__(self) -> 'Column': ...
    def __rand__(self, other: Any) -> 'Column': ...
    def __ror__(self, other: Any) -> 'Column': ...
    def __contains__(self, other: Any) -> 'Column': ...
    def __getitem__(self, other: Any) -> 'Column': ...
    def bitwiseOR(self, other: Any) -> 'Column': ...
    def bitwiseAND(self, other: Any) -> 'Column': ...
    def bitwiseXOR(self, other: Any) -> 'Column': ...
    def getItem(self, key: Any) -> 'Column': ...
    def getField(self, name: Any) -> 'Column': ...
    def __getattr__(self, item: Any) -> 'Column': ...
    def __iter__(self) -> None: ...
    def rlike(self, item: Any) -> 'Column': ...
    def like(self, item: Any) -> 'Column': ...
    def startswith(self, item: Any) -> 'Column': ...
    def endswith(self, item: Any) -> 'Column': ...
    def substr(self, startPos, length) -> 'Column': ...
    def __getslice__(self, startPos, length) -> 'Column': ...
    def isin(self, *cols: Any) -> 'Column': ...
    def asc(self) -> 'Column': ...
    def desc(self) -> 'Column': ...
    def isNull(self) -> 'Column': ...
    def isNotNull(self) -> 'Column': ...
    def alias(self, *alias: str) -> 'Column': ...
    def name(self, *alias: str) -> 'Column': ...
    def cast(self, dataType: Union[DataType, str]) -> 'Column': ...
    def astype(self, dataType: Union[DataType, str]) -> 'Column': ...
    def between(self, lowerBound, upperBound) -> 'Column': ...
    def when(self, condition: 'Column', value: Any) -> 'Column': ...
    def otherwise(self, value: Any) -> 'Column': ...
    def over(self, window: Window): ...
    def __nonzero__(self) -> None: ...
    def __bool__(self) -> None: ...
