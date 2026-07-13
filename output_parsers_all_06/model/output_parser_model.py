from typing import Literal

from pydantic import BaseModel, Field

class ParserModel(BaseModel):
    topic: str


class Disaster(BaseModel):
    disasterName:  str = Field(description="Type of Disaster , eg: hurricane, forest fire , earthquake etc")
    rootCause: str = Field(description="Root Cause of the disaster ")
    effects: list[str] = Field(description="list of effects on people")
    precautions: list[str] = Field(description="list of 2 main precautions that people have to take at thge time of the disaster")

class Sentiment(BaseModel):
    sentiment: Literal["POSITIVE", "NEGATIVE"] = Field(description="Provide the sentiment of the statement as NEGATIVE or POSITIVE")