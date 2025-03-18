import datetime
import decimal
from src.entities.Action import Action

class CreateAction:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self, action_type: int, date: datetime.datetime, investment: decimal.Decimal):
        action_name = self.repository.get_action_name_by_id(action_type)
        action_entity = Action.create(action_type, action_name, date, investment)
        self.repository.save(action_entity)  
        return action_entity