# Superheroes API

Welcome to the Superheroes API project! This application provides an API to manage superheroes, their powers, and their relationships.

## Table of Contents

- [Technologies](#technologies)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Seeding the Database](#seeding-the-database)
- [Contributing](#contributing)

## Technologies

This project is built using:
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/annewaithaka/superheroes.git
   cd superheroes

2. **Create a virtual environment**:
python3 -m venv venv

3. **Activate the virtual environment**:
source venv/bin/activate

4. **Install dependencies**:
pip install -r requirements.txt

5. **Create the database**:
python -c "from app import db; db.create_all()"

### API Endpoints
**Heroes**
GET /heroes

Returns a list of all heroes.
GET /heroes/int:id

Returns details of a specific hero by ID.
**Powers**
GET /powers

Returns a list of all powers.
GET /powers/int:id

Returns details of a specific power by ID.
PATCH /powers/int:id

Updates the description of a specific power by ID.
**Hero Powers**
POST /hero_powers
Creates a new association between a hero and a power.

### Seeding the Database
Run the command: python seed.py

### Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.
