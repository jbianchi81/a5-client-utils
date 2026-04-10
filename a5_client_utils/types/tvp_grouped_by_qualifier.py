from typing import TypedDict, List
from .tvp import TVP


class TVPGroupedByQualifier(TypedDict):
    qualifier : str
    pronosticos : List[TVP]