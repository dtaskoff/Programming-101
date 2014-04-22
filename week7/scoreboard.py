from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import desc

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"
    position = Column(Integer, primary_key = True)
    name = Column(String)
    points = Column(Integer)

    def __str__(self):
        return "{}. {} with {} points".format(self.position,
            self.name, self.points)


class Scoreboard():
    def __init__(self):
        engine = create_engine("sqlite:///players.db")
        self.session = Session(bind=engine)
        Base.metadata.create_all(engine)

    def update(self, player, points): 
        player = Player(name=player, points=points)
        self.session.add(player)
        player.points = points
        self.session.commit()

    def display(self):
        print("This is the current top ten:")
        all_players =\
            self.session.query(Player).order_by(Player.points.desc()).all()
        print('\n'.join(map(str, all_players)))