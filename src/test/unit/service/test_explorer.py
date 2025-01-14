from models.explorer import Explorer
from service import explorer as code

sample = Explorer(name="Naserati",
                  country="US",
                  description="Faster than a Maserati",
                  )

def test_create():
  resp = code.create(sample)
  assert resp == sample

def test_get_exists():
  resp = code.get_one("Naserati")
  assert resp == sample

def test_get_missing():
  resp = code.get_one("Bob")
  assert resp is None