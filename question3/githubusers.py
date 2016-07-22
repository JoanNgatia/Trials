# initialize new user with repos, g.hub username, email
# connect all the model classess, create all separately but similar
# attributes where they cross into each other.


class User(object):
    """Initialize new user with their details."""

    def __init__(self, email, username, date_joined='1/1/2016'):
        self.email = email
        self.username = username
        self.date_joined = date_joined


class Repository(object):
    """Initialize repository class with attributes."""

    def __init__(self, name, owner):
        self.name = name
        # self.date_created = date_created
        self.owner = owner.username
        self.contributions = []

    def make_contribution(self, contribution_name, creator):
        self.contribution_name = contribution_name
        self.creator = creator
        new_contribution = Contribution(self.contribution_name, self.creator)
        self.contributions.append(new_contribution)


class Contribution(object):
    """Initialize contributions class with its attributes."""

    def __init__(self, name, creator):
        self.name = name
        self.creator = creator.username


class GithubUser(object):
    """Main Github user class."""

    def __init__(self, user):
        """Pass in instance of User class."""
        # self.repositories = repositories
        self.followers = []
        self.followings = []
        # self.contributions = contributions
        self.user = user
        self.email = user.email
        self.username = user.username


# test code to check accurate creation of Github user.
userq = User('joanwanjirungatia@gmail.com', 'andela-jngatia')
userv = User('mamaashley19@gmail.com', 'mmaashley')
# print userq.username
userw = GithubUser(userq)
# print userw.email

repo2 = Repository('trials', userq)
# print repo2.owner.username

# contribution1 = Contribution('just try', repo2, userq)
# print contribution1.creator
# print contribution1.repository
repo2.make_contribution('just try', userq)
repo2.make_contribution('Ash', userq)
repo2.make_contribution('Genevieve', userv)
for contribution in repo2.contributions:
    # import pdb; pdb.set_trace()
    print contribution.name, contribution.creator
