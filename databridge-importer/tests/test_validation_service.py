from decimal import Decimal

from app.services.validation_service import LeadValidationService


def test_valid_lead_record():
    validator = LeadValidationService()
    lead, errors = validator.validate(
        {
            "nome": "Ana Costa",
            "email": "ana@empresa.com",
            "telefone": "11987654321",
            "empresa": "Empresa Teste",
            "valor": "1500,50",
        }
    )

    assert errors == []
    assert lead is not None
    assert lead.value == Decimal("1500.50")


def test_invalid_lead_record():
    validator = LeadValidationService()
    lead, errors = validator.validate(
        {"nome": "A", "email": "email", "telefone": "123", "empresa": "", "valor": "0"}
    )

    assert lead is None
    assert len(errors) == 5
