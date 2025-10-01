# Updating structured output schema for parsing multiple items

from pydantic import BaseModel

class BatchDocumentClassification(BaseModel):
    class Category(BaseModel):
        document_id: str
        category: list[str]

    categories: list[Category] # Update the Pydantic model to include a list of Category models.