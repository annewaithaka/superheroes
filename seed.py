from app import db, Hero, Power, HeroPower  # Adjust according to your app structure

def seed_data():
    # Create power instances
    powers = [
        Power(id=1, name="super strength", description="gives the wielder super-human strengths"),
        Power(id=2, name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(id=3, name="super human senses", description="allows the wielder to use her senses at a super-human level"),
        Power(id=4, name="elasticity", description="can stretch the human body to extreme lengths")
    ]
    
    # Create hero instances
    heroes = [
        Hero(id=1, name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(id=2, name="Doreen Green", super_name="Squirrel Girl"),
        Hero(id=3, name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(id=4, name="Janet Van Dyne", super_name="The Wasp"),
        Hero(id=5, name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(id=6, name="Carol Danvers", super_name="Captain Marvel"),
        Hero(id=7, name="Jean Grey", super_name="Dark Phoenix"),
        Hero(id=8, name="Ororo Munroe", super_name="Storm"),
        Hero(id=9, name="Kitty Pryde", super_name="Shadowcat"),
        Hero(id=10, name="Elektra Natchios", super_name="Elektra")
    ]

    # Create hero_power instances
    hero_powers = [
        HeroPower(id=1, strength="Strong", hero_id=1, power_id=2),
        HeroPower(id=2, strength="Average", hero_id=2, power_id=1),
        HeroPower(id=3, strength="Strong", hero_id=3, power_id=3),
        HeroPower(id=4, strength="Strong", hero_id=4, power_id=4),
        HeroPower(id=5, strength="Strong", hero_id=5, power_id=1),
        HeroPower(id=6, strength="Strong", hero_id=6, power_id=2),
        HeroPower(id=7, strength="Strong", hero_id=7, power_id=1),
        HeroPower(id=8, strength="Strong", hero_id=8, power_id=3),
        HeroPower(id=9, strength="Average", hero_id=9, power_id=4),
        HeroPower(id=10, strength="Strong", hero_id=10, power_id=1)
    ]

    # Add all data to the session
    db.session.add_all(powers)
    db.session.add_all(heroes)
    db.session.add_all(hero_powers)

    # Commit the session to the database
    db.session.commit()
    print("Database seeded!")

if __name__ == '__main__':
    from app import create_app  # Adjust according to your app structure
    app = create_app()
    with app.app_context():
        seed_data()

