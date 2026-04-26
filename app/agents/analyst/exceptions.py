from typing import Any
from fastapi import HTTPException, status


class AnalystCustomHTTPException(HTTPException): 
    def __init__ (self, status_code: int, detail: str, headers: dict[str, Any]) -> None: 
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class InvalidToolException(AnalystCustomHTTPException): 
    def __init__(self, detail: str = "Invalid tool used in the prompt", headers: dict[str, Any] = None) -> None: 
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail, headers=headers)

class AnalysisNotFoundException(AnalystCustomHTTPException): 
    def __init__(self, detail: str = "Analysis not found", headers: dict[str, Any] = None) -> None: 
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail, headers=headers)

class AnalysisFailedException(AnalystCustomHTTPException): 
    def __init__(self, detail: str = "Analysis failed", headers: dict[str, Any] = None) -> None: 
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail, headers=headers)

class InvalidInputException(AnalystCustomHTTPException): 
    def __init__(self, detail: str = "Invalid input provided", headers: dict[str, Any] = None) -> None: 
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail, headers=headers)

