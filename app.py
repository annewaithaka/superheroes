from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from models import db, Hero, Power, HeroPower  # Import models

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"message": "Welcome to the Superheroes API!"})

    @app.route('/heroes', methods=['GET'])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([hero.to_dict() for hero in heroes])

    @app.route('/heroes/<int:id>', methods=['GET'])
    def get_hero(id):
        hero = Hero.query.get(id)
        if not hero:
            return jsonify({"error": "Hero not found"}), 404
        return jsonify(hero.to_dict())

    @app.route('/powers', methods=['GET'])
    def get_powers():
        powers = Power.query.all()
        return jsonify([power.to_dict() for power in powers])

    @app.route('/powers/<int:id>', methods=['GET'])
    def get_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404
        return jsonify(power.to_dict())

    @app.route('/powers/<int:id>', methods=['PATCH'])
    def update_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404

        data = request.get_json()

        # Validate description
        if 'description' in data:
            if len(data['description']) < 20:
                return jsonify({"errors": ["description must be at least 20 characters long"]}), 400
            power.description = data['description']

        db.session.commit()
        return jsonify(power.to_dict()), 200

    @app.route('/hero_powers', methods=['POST'])
    def create_hero_power():
        data = request.get_json()

        # Validate required fields
        if not all(key in data for key in ['strength', 'power_id', 'hero_id']):
            return jsonify({"errors": ["Missing required fields"]}), 400

        # Create the new HeroPower instance
        new_hero_power = HeroPower(
            strength=data['strength'],
            power_id=data['power_id'],
            hero_id=data['hero_id']
        )

        # Validate the strength
        try:
            new_hero_power.validate()  # Assuming validate() checks for valid strength
            db.session.add(new_hero_power)
            db.session.commit()
        except ValueError as e:
            return jsonify({"errors": [str(e)]}), 400
        except IntegrityError:
            db.session.rollback()
            return jsonify({"errors": ["hero_id or power_id does not exist"]}), 400

        # Prepare the response data
        response_data = {
            "id": new_hero_power.id,
            "hero_id": new_hero_power.hero_id,
            "power_id": new_hero_power.power_id,
            "strength": new_hero_power.strength,
            "hero": {
                "id": new_hero_power.hero.id,
                "name": new_hero_power.hero.name,
                "super_name": new_hero_power.hero.super_name
            },
            "power": {
                "id": new_hero_power.power.id,
                "name": new_hero_power.power.name,
                "description": new_hero_power.power.description
            }
        }

        return jsonify(response_data), 201

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555)
