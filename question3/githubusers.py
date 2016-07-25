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
        self.owner = owner


class Contribution(object):
    """Initialize contributions class with its attributes."""

    def __init__(self, name, creator, repo):
        self.name = name
        self.creator = creator
        self.repo = repo


class GithubUser(User):
    """Main Github user class."""

    def __init__(self, email, username, date_joined, **kwargs):
        """Pass in instance of User class."""
        super(GithubUser, self).__init__(email, username, date_joined)
        self.followers = kwargs.get('followers', [])
        self.followings = kwargs.get('followings', [])
        self.repositories = kwargs.get('repositories', [])
        self.contributions = kwargs.get('contributions', [])

    def create_repository(self, repo_name):
        self.repo_name = repo_name
        new_repository = Repository(
            self.repo_name, self.username)
        self.repositories.append(new_repository)
        return self.repositories

    def follow_person(self, user):
        self.user = user
        following = GithubUser(
            self.user.username, self.user.email, self.user.date_joined)
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


# test code to check accurate creation of Github user.
userw = GithubUser('joanwanjirungatia@gmail.com',
                   'andela-jngatia', '1/2/2016')
userv = GithubUser('mamaashley19@gmail.com', 'mmaashley', '1/2/2016')
repo2 = Repository('bucketlists', userw)
contribution1 = Contribution('buckets', userw, repo2)
userw.follow_person(userv)
userw.make_contribution(repo2, 'bucketlists')
for person in userw.followings:
    print person.username

for contribution in userw.contributions:
    print contribution.name
