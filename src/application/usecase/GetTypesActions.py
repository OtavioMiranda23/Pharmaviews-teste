class GetTypesActions:
    def __init__(self, repository):
        self.repository = repository
    
    def execute(self):
        types = self.repository.get_all_types_actions()
        return types