from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

# MODELS GO BELOW!
class Pet(db.Model):
    __tablename__ = 'pets'

    def __repr__(self):
        """show info about pet"""
        p = self
        return f'<Pet id={p.id} name={p.name} species={p.species} age={p.age} available={p.available} notes={p.notes}>'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.Text,nullable=False)
    species=db.Column(db.Text,nullable=False)
    photo_url=db.Column(db.Text,nullable=True)
    age=db.Column(db.Integer,nullable=True)
    notes=db.Column(db.Text,nullable=True)
    available=db.Column(db.Boolean,nullable=False,default=True)


