import os, sys, json, json5
from typing import NamedTuple, List, Any, final
from dataclasses import dataclass, field, asdict, astuple

@dataclass
class DCOne:
    a: str
    b: int

dc = DCOne("s", 3)
print(dc)