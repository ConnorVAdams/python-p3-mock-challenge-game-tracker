class Game:
    all = []
    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, 'title'):
            raise ValueError(
                'Title cannot be re-assigned.'
            )
        elif not isinstance(title, str) and len(title):
            raise TypeError(
                'Title must be a non-empty string.'
            )
        else:
            self._title = title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set(result.player for result in self.results()))

    def average_score(self, player):
        all_scores = [result.score for result in self.results() if result.player in self.players()]
        return sum(all_scores) / len(all_scores)

class Player:
    all = []
    def __init__(self, username):
        self.username = username
        type(self).all.append(self)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) > 1 and len(username) < 17:
            self._username = username
        else:
            raise TypeError(
                'Username must be a string between 2 and 16 characters.'
            )

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if hasattr(self, 'score'):
            raise ValueError(
                'Score cannot be re-assigned.'
            )
        elif isinstance(score, int) and score > 0 and score < 5001:
            self._score = score
        else:
            raise TypeError(
                'Score must be an integer between 1 and 5000.'
            )
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise TypeError(
                'Player must be of the Player class.'
            )
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise TypeError(
                'Game must be of the Game class.'
            )