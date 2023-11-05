import functools
from typing import List

from pydantic import RootModel

from k_tool_box.api import BaseAPI, APIRet
from k_tool_box.api.model import Creator

__all__ = ["GetCreators", "get_creators"]


class GetCreators(BaseAPI):
    path = "/creators.txt"
    method = "get"

    class Response(RootModel[List[Creator]]):
        root: List[Creator]

    @classmethod
    async def __call__(cls) -> APIRet[List[Creator]]:
        return await cls.request()


get_creators = GetCreators.__call__
"""List all creators with details. I blame DDG for .txt."""
