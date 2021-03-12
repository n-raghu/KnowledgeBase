from typing import Any

from pydantic import BaseModel


class Analyse(BaseModel):
    instance_id: Any
