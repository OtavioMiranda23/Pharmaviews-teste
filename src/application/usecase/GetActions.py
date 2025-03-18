class GetActions:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self):
        actions = self.repository.get_all_actions()
        return actions