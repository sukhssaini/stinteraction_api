from api.models.base import Base


class User(Base):
    def __init__(self):
        Base.__init__(self)
        self.user_id = None
        self.user_name = None
        self.email_id = None
        self.type = None
        self.phone_number = None
