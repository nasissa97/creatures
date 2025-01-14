from models.explorer import Explorer

_explorers = [
  Explorer(name="John Doe",
           country="FN",
           description="Scarce during full moons"),
  Explorer(name="Naserati",
           country="US",
           description="Faster than a Maserati")
]

def get_all() -> list[Explorer]:
  return _explorers

def get_one(name: str) -> Explorer | None:
  for _explorer in _explorers:
    if _explorer.name == name:
      return _explorer
    
  return None

def create(explorer: Explorer) -> Explorer:
  return explorer

def modify(explorer: Explorer) -> Explorer:
  return explorer

def replace(explorer: Explorer) -> Explorer:
  return explorer

def delete(name: str) -> bool:
  return None

