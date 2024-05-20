from typing import List, Dict, Any
from langchain.output_parsers import PydanticOutputParser
from pydantic.v1 import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(..., description="A short summary of the person")
    facts: List[str] = Field(
        ..., description="Interesting facts about the person"
    )


summary_parser = PydanticOutputParser(pydantic_object=Summary)
