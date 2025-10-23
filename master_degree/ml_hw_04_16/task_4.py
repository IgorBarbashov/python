class Creature:
    health_points: int


class EarthCreature(Creature):
    pass


class SeaCreature(Creature):
    pass


class AirCreature(Creature):
    pass


class Troll(EarthCreature):
    health_points = 100


class Elf(EarthCreature):
    health_points = 80


class Mermaid(SeaCreature):
    health_points = 60


class Siren(SeaCreature):
    health_points = 75


class Dragon(AirCreature):
    health_points = 120


class Pegasus(AirCreature):
    health_points = 85


if __name__ == "__main__":
    x = Elf()
    print(isinstance(x, EarthCreature))
    print(isinstance(x, Creature))
    print(x.health_points)
