import re
from decimal import Decimal, InvalidOperation

from app.models.customer_lead import CustomerLead


class LeadValidationService:
    EMAIL_PATTERN = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")

    def validate(self, record: dict) -> tuple[CustomerLead | None, list[str]]:
        errors: list[str] = []

        name = self._clean_text(record.get("nome"))
        email = self._clean_text(record.get("email")).lower()
        phone = self._clean_text(record.get("telefone"))
        company = self._clean_text(record.get("empresa"))
        value = self._parse_decimal(record.get("valor"))

        if len(name) < 3:
            errors.append("nome deve ter pelo menos 3 caracteres")
        if not self.EMAIL_PATTERN.match(email):
            errors.append("email invalido")
        if len(re.sub(r"\D", "", phone)) < 10:
            errors.append("telefone deve ter pelo menos 10 digitos")
        if len(company) < 2:
            errors.append("empresa deve ter pelo menos 2 caracteres")
        if value is None or value <= 0:
            errors.append("valor deve ser maior que zero")

        if errors:
            return None, errors

        lead = CustomerLead(
            name=name,
            email=email,
            phone=phone,
            company=company,
            value=value,
        )
        return lead, []

    @staticmethod
    def _clean_text(value: object) -> str:
        return str(value).strip() if value is not None else ""

    @staticmethod
    def _parse_decimal(value: object) -> Decimal | None:
        if value is None or value == "":
            return None
        try:
            normalized = str(value).replace("R$", "").replace(".", "").replace(",", ".").strip()
            return Decimal(normalized)
        except (InvalidOperation, ValueError):
            return None
