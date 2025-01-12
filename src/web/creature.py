from fastapi import APIRouter
from model.creature import Creature
import fake.creature as service

router = APIRouter(prefix= "/creature")

@router.get("/")
def get_all():
  return service.get_all()

@router.get("/{name}")
def get_one(name: str) -> Creature | None:
  return service.get_one(name)

@router.post("/")
def create(explorer: Creature) -> Creature:
  return service.create(explorer)

@router.patch("/")
def modify(explorer: Creature) -> Creature:
  return service.modify(explorer)

@router.put("/")
def create(explorer: Creature) -> Creature:
  return service.replace(explorer)

@router.delete("/")
def create(name: str) -> None:
  service.delete(name)
  return None
