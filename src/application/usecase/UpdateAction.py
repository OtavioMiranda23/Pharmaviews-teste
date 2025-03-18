from src.entities.Action import Action

class UpdateAction:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self, id: str, action_data: dict):
        existing_action = self.repository.get_action_by_id(id)
        action_name = existing_action.action_name  
        if not existing_action:
            raise ValueError("Action não encontrada")
        if action_data.get("id_action_type") != existing_action.id_action_type:
            action_name = self.repository.get_action_name_by_id(action_data.get("id_action_type"))
        updated_action = Action(
            existing_action.id,
            action_data.get("id_action_type", existing_action.id_action_type),
            action_name,
            action_data.get("expect_date", existing_action.date),
            action_data.get("investment", existing_action.investment)
        )
        self.repository.update_action(id, updated_action)
        return updated_action   