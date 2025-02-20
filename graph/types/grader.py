from pydantic import BaseModel, Field

class GradeSummary(BaseModel):
    """Checklist scores for summary criteria assessment."""

    updates_specific_portions: bool = Field(
        description="Summary only updates specific portions necessary to reflect new information or changes"
    )
    explicit_information: bool = Field(
        description="Summary only includes explicitly discussed information from the session"
    )
    factually_accurate: bool = Field(
        description="Summary is factually accurate and reflects discussion nuances"
    )
    concise_and_clear: bool = Field(
        description="Summary is detailed while being concise and clear"
    )
