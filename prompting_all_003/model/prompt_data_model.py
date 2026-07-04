from pydantic import BaseModel

class PromptDataModel(BaseModel):
    character_input: str
    mythology_input: str
    no_of_lines_input: int

class PromptSelectablesModel:
    def __init__(self, character_options, mythology_options, no_of_lines_options):
        self.character_options = character_options
        self.mythology_options = mythology_options
        self.no_of_lines_options = no_of_lines_options
