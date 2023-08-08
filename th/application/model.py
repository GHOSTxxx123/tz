from application import app, db
from sqlalchemy.sql import func
from dataclasses import dataclass

@dataclass
class Birds(db.Model):
    id: int
    name: str
    color_feather: str
    cover: str
    created_at: str
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    color_feather = db.Column(db.String(100), nullable=False)
    cover = db.Column(db.String(50), nullable=False, default='default.jpg')
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<Birds {self.name}>'
        

@dataclass
class Histori(db.Model):
    id: int
    birds_id: int
    created_at: str
    

    id = db.Column(db.Integer, primary_key=True)
    birds_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __repr__(self):
        return f'<Histori {self.id}>'
    