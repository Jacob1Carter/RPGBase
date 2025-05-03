from shared import NPC


class worker(NPC):

    def __init__(self):
        super().__init__()
        self.name = "Worker"
        self.description = "A worker in the factory."