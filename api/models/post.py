from models import Base


class Post(Base):
    def __init__(self):
        Base.__init__()
        self.post_id = None
        self.post_name = None
        self.post_description = None
        self.topic_id = None
        self.file_location = None
