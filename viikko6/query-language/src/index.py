from player_statistics import Statistics
from player_reader import PlayerReader
#from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or
from matchers import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi//nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    #matcher = And(
    #    HasAtLeast(5, "goals"),
    #    HasAtLeast(5, "assists"),
    #    PlaysIn("PHI")
    #)

    #matcher = And(
    #Not(HasAtLeast(1, "goals")),
    #PlaysIn("NYR")
    #)

    #matcher = And(
    #HasFewerThan(1, "goals"),
    #PlaysIn("NYR")
    #)

    #matcher = Or(
    #HasAtLeast(45, "goals"),
    #HasAtLeast(70, "assists")
    #)
    
    #matcher = And(
    #HasAtLeast(70, "points"),
    #Or(
    #    PlaysIn("NYR"),
    #    PlaysIn("FLA"),
    #    PlaysIn("BOS")
    #)
    #)

    #matcher = query.playsIn("NYR").build()
    
    #matcher = (
    #  query
    #  .playsIn("NYR")
    #  .hasAtLeast(10, "goals")
    #  .hasFewerThan(20, "goals")
    #  .build()
    #)

    m1 = (
        query
            .playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build()
        )

    m2 = (
        query
            .playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
        )

    matcher = query.oneOf(m1, m2).build()

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
