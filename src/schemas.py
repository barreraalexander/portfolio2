from pydantic import BaseModel
from pydantic.validators import str_validator
from typing import Union

class ipKey(str):
    @classmethod
    def __get_validators__(cls):
        yield str_validator
        yield cls.empty_to_none

    @classmethod
    def empty_to_none(
        cls,
        val: str
        ) -> Union[None, str]:
        if val=="":
            return None
        return cls(val)
        # pass


class cacheKey(BaseModel):
    ipAddr: ipKey

class cacheKey2(BaseModel):
    pass

# class generateKey():
#     pass