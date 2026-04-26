from typing import Any
from fastapi import HTTPException, status


class AnalystCustomHTTPException(HTTPException): 
    def __init__ (self, status_code: int, detail: str, headers: dict[str, Any]) -> None: 
        super().__init__(status_code=status_code, detail=detail, headers=headers)

c