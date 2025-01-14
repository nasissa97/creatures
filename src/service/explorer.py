from models.explorer import Explorer
import fake.explorer as data

def get_all() -> list[Explorer]:
  return data.get_all()

def get_one(name: str) -> Explorer | None:
  return data.get_one(name)

def create(creature: Explorer) -> Explorer | None:
  return data.create(creature)

def replace(id: str, creature: Explorer) -> Explorer:
  return data.replace(id, creature)

def modify(id: str, creature: Explorer) -> Explorer:
  return data.modify(id, creature)

def delete(id: str) -> bool:
  return data.delete(id)
