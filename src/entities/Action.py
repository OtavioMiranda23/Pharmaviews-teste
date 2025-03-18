import datetime
import decimal
import uuid

class Action:
    def __init__(self, id: uuid.UUID, id_action_type: int, action_name: str, date: datetime.date, investment: decimal.Decimal):
        self.id = id
        self.set_id_action_type(id_action_type)
        self.set_action_name(action_name)
        self.set_date(date)
        self.set_investment(investment)

    @staticmethod
    def create(id_action_type: int, action_name: str, date: datetime.date, investment: decimal.Decimal):
        id = uuid.uuid4()
        return Action(id, id_action_type, action_name, date, investment)

    def set_id_action_type(self, id_action_type: int):
        if not isinstance(id_action_type, int) or id_action_type <= 0:
            raise ValueError("O id_action_type deve ser um número inteiro positivo.")
        self.id_action_type = id_action_type

    def set_action_name(self, action_name: str):
        if not isinstance(action_name, str) or not action_name.strip():
            raise ValueError("O action_name deve ser uma string não vazia.")
        if len(action_name) > 100:
            raise ValueError("O action_name deve ter no máximo 100 caracteres.")
        self.action_name = action_name.strip()

    def set_date(self, date: datetime.date):
        if not isinstance(date, datetime.date):
            raise ValueError("O date deve ser uma instância válida de datetime.date.")

        self.date = date

    def set_investment(self, investment: decimal.Decimal):
        if not isinstance(investment, decimal.Decimal):
            raise ValueError("O investment deve ser um número decimal.")
        if investment < decimal.Decimal("0.01"):
            raise ValueError("O investimento deve ser um valor positivo.")
        self.investment = investment
    def to_dict(self):
        return {
            "id": str(self.id),  
            "id_action_type": self.id_action_type,
            "action_name": self.action_name,
            "date": self.date.isoformat(),
            "investment": float(self.investment)  
        }