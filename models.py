from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)
    hero_powers = db.relationship('HeroPower', backref='hero', cascade="all, delete-orphan", lazy='dynamic')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name,
            "powers": [
                {
                    "id": hp.power.id,
                    "name": hp.power.name,
                    "description": hp.power.description,
                    "strength": hp.strength
                }
                for hp in self.hero_powers
            ]
        }

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    hero_powers = db.relationship('HeroPower', backref='power', cascade="all, delete-orphan", lazy='dynamic')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "heroes": [hp.hero_id for hp in self.hero_powers]  # List of hero IDs with this power
        }

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(20), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    VALID_STRENGTHS = ['Strong', 'Weak', 'Average']

    def validate(self):
        if self.strength not in self.VALID_STRENGTHS:
            raise ValueError(f"strength must be one of: {', '.join(self.VALID_STRENGTHS)}")

    def to_dict(self):
        return {
            "id": self.id,
            "strength": self.strength,
            "hero_id": self.hero_id,
            "power_id": self.power_id
        }
