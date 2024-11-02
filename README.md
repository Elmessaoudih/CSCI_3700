# Flask and PostgreSQL Fruits Application

This project demonstrates how to connect PostgreSQL with Flask to display data in an HTML table. The application retrieves data from two tables (basket_a and basket_b) in a PostgreSQL database and displays it on a webpage.
Quick Start

### Team Members
- Hamid El Messaoudi
- 
## Quick Start

### Local Test Setup

1. **Set up a Python 3 virtual environment**:
   ```bash
   sudo apt-get install python3-venv

2. **Create and activate the virtual environment**:
   ```bash
python3 -m venv python_venv
source python_venv/bin/activate

3. **Install dependencies**: To install the required Python packages, run:
   ```bash
pip3 install -r requirements.txt

4. **Set up PostgreSQL and create tables: Make sure PostgreSQL is running. Connect to it and create these tables for our baskets**:

   ```sql
CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR(100) NOT NULL
);

CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR(100) NOT NULL
);

INSERT INTO basket_a (a, fruit_a)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber'),
    (5, 'Cherry');

INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');

5. **Update database connection details**:
Make sure the connection details (username, password, host, port, and database name) are correct in main.py.

6. **Run the Flask app: Start the server with**:
   ```bash
python3 main.py

### Endpoints
- `[/api/update_basket_a](http://127.0.0.1:5000/api/update_basket_a)` - Adds "Cherry" to `basket_a`
- `[/api/unique](http://127.0.0.1:5000/api/unique)` - Displays unique fruits from `basket_a` and `basket_b`
