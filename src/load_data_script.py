from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dataset_model import Planning, Base
import pathlib
import json

BASE_DIR = pathlib.Path(__file__).parent.parent.resolve()

engine = create_engine('sqlite:///planning.bd')


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(engine)
session = Session()


dataset_file = BASE_DIR / "planning.json"

f = open(dataset_file, "r")
data = json.loads(f.read())
for record in data:
    planning_record = Planning(record)
    session.add(planning_record)

session.commit()
session.close()
