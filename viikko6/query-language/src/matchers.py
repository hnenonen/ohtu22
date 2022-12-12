class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

### 2 tehtävä
class All:
    @staticmethod
    def matches(*args):
        return True

class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def matches(self, player):
        return not self._matcher.matches(player)

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

### 3 Tehtävä
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True

        return False

## 4 Tehtävä

class QueryBuilder:
    def __init__(self, query=All()):
        self._query = query

    def build(self):
        return self._query

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._query))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self._query))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self._query))

    @staticmethod
    def oneOf(query1, query2):
        return QueryBuilder(Or(query1, query2))