from agent.model.AgentModel import AgentModel


class Asset(AgentModel):

    def __init__(self, _id, _price):
        self.id = _id
        self.price = _price
