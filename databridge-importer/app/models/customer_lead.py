from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class CustomerLead:
    name: str
    email: str
    phone: str
    company: str
    value: Decimal
