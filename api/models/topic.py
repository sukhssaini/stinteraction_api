from api.models.base import Base


class Topic(Base):
    def __init__(self):
        Base.__init__(self)
        self.topic_name = None
        self.description = None
        self.topic_id = None
        self.user_id = None
