from typing import Annotated, Literal, Optional, TypedDict

from pydantic import BaseModel, Field

class UserComment(BaseModel):
    user_comment_str:str


class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["POSITIVE", "NEGATIVE", "NEUTRAL"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    reviewer: Annotated[Optional[str], "Write the name of the reviewer"]


class ReviewPydanticModel(BaseModel):
    key_themes: list[str] = Field (description="Write down all the key themes discussed in the review in a list") 
    summary: str = Field (description="A brief summary of the review")
    sentiment: Literal["POSITIVE", "NEGATIVE", "NEUTRAL"] = Field (description="Return sentiment of the review either negative, positive or neutral")
    pros: Optional[list[str]] = Field (default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field (default=None, description="Write down all the cons inside a list")
    reviewer: Optional[str] = Field (default=None, description="Write the name of the reviewer")


# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}