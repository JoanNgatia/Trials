# initialize new user with repos, g.hub username, email
# connect all the model classess, create all separately but similar
# attributes where they cross into each other.


class User(object):
    """Initialize new user with their details."""

    def __init__(self, email, username, date_joined='1/1/2016'):
        self.email = email
        self.username = username
        self.date_joined = date_joined
        self.repositories = []
        self.followings = []

    def create_repository(self, repo_name):
        self.repo_name = repo_name
        new_repository = Repository(
            self.repo_name, self.username)
        self.repositories.append(new_repository)
        return self.repositories

    def follow_person(self, user):
        self.user = user
        following = User(self.user.username, self.user.email)
        self.followings.append(following)
        return self.followings


class Repository(object):
    """Initialize repository class with attributes."""

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
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
        self.user = user
        self.followings = user.followings
        self.repositories = user.repositories
        self.followers = []

# test code to check accurate creation of Github user.
userq = User('joanwanjirungatia@gmail.com', 'andela-jngatia')
userv = User('mamaashley19@gmail.com', 'mmaashley')
repo2 = Repository('trials', userq)
repo2.make_contribution('just try', userq)
repo2.make_contribution('Ash', userq)
repo2.make_contribution('Genevieve', userv)
userq.create_repository('Bucketlists')
userq.follow_person(userv)
# .make_contribution('trials2', userv)
# userq.create_repository(repo2)
userw = GithubUser(userq)
# for repository in userw.repositories:
    # print repository.name, repository.contributions

for following in userw.followings:
    print following.username, following.email
# print userw.repositories
# print userw.contributions

# for contribution in repo2.contributions:
#     # import pdb; pdb.set_trace()
#     print contribution.name, contribution.creator
