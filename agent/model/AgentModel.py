import json

class AgentModel:

    def __init__(self):
        pass

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

