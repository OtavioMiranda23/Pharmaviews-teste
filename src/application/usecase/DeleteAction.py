class DeleteAction:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self, id):
        action = self.repository.delete_action_by_id(id)
        return action