class GetActionById:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self, id):
        action = self.repository.get_action_by_id(id)
        return action