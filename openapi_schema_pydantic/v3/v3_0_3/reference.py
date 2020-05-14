from pydantic import BaseModel, Field


class Reference(BaseModel):
    """
    A simple object to allow referencing other components in the specification, internally and externally.

    The Reference Object is defined by [JSON Reference](https://tools.ietf.org/html/draft-pbryan-zyp-json-ref-03)
    and follows the same structure, behavior and rules.

    For this specification, reference resolution is accomplished as defined by the JSON Reference specification
    and not by the JSON Schema specification.
    """

    ref: str = Field(alias="$ref")
    """**REQUIRED**. The reference string."""

    class Config:
        schema_extra = {
            'examples': [
                {
                    "$ref": "#/components/schemas/Pet"
                }
            ]
        }