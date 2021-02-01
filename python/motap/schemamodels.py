from typing import Any

from pydantic import BaseModel


class AddrSchema(BaseModel):
    address_matched: Any
    customerID: int
    dob: str
    income: int
    bureauScore: int
    applicationScore: int
    maxDelL12M: int
    allowedFoir: int
    existingEMI: int
    loanTenure: int
    currentAddress: str
    bureauAddress: str
    rejected: Any
    loanAmount: Any
