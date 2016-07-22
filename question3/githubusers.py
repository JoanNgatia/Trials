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
        self.followers = []
        self.contributions = []

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
        following.followers.append(self)
        return self.followings

    def make_contribution(self, repo, contribution_name):
        self.repo = repo
        self.contribution_name = contribution_name
        new_contribution = Contribution(
            self.contribution_name, self.username, self.repo.name)
        self.contributions.append(new_contribution)
        return self.contributions


class Repository(object):
    """Initialize repository class with attributes."""

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner


class Contribution(object):
    """Initialize contributions class with its attributes."""

    def __init__(self, name, creator, repo):
        self.name = name
        self.creator = creator
        self.repo = repo


class GithubUser(object):
    """Main Github user class."""

    def __init__(self, user):
        """Pass in instance of User class."""
        self.user = user
        self.followings = user.followings
        self.repositories = user.repositories
        self.contributions = user.contributions
        self.followers = user.followers

# test code to check accurate creation of Github user.
userq = User('joanwanjirungatia@gmail.com', 'andela-jngatia')
userv = User('mamaashley19@gmail.com', 'mmaashley')
repo2 = Repository('trials', userq)
userq.create_repository('Bucketlists')
userq.follow_person(userv)
userq.make_contribution(repo2, 'fewere contribution')
userw = GithubUser(userq)

for contribution in userw.contributions:
    print "{} by {}".format(contribution.name, contribution.creator)

for repository in userw.repositories:
    print repository.name

for following in userw.followings:
    print following.username, following.email
