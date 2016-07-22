# initialize new user with repos, g.hub username, email
# connect all the model classess, create all separately but similar
# attributes where they cross into each other.


class User(object):
    """Initialize new user with their details."""

    def __init__(self, email, username, date_joined):
        self.email = email
        self.username = username
        self.date_joined = date_joined


class Repository(object):
    """Initialize repository class with attributes."""

    def __init__(self, name, date_created, owner):
        self.name = name
        self.date_created = date_created
        self.owner = owner


class Contribution(object):
    """Initialize contributions class with its attributes."""

    def __init__(self, name, repository, creator):
        self.name = name
        self.repository = repository
        self.creator = creator
