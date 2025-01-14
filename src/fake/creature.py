from models.creature import Creature

_creatures = [
  Creature(name="yetti",
           aka="Abominable Snowman",
           country="CN",
           area="Himalayas",
           description="Hirsute Himalayan"),
  Creature(name="bigfoot",
           description="Yeti's Cousin Eddie",
           country="US",
           area="*",
           aka="Sasquatch"),
]

def get_all() -> list[Creature]:
  return _creatures

def get_one(name: str) -> Creature | None:
  for _creature in _creatures:
    if _creature.name.lower() == name:
      return _creature
  
  return None

def create(creature: Creature) -> Creature:
  return creature

def modify(creature: Creature) -> Creature:
  return creature

def replace(creature: Creature) -> Creature:
  return creature

def delete(creature: Creature) -> Creature:
  return creature