# Flask and PostgreSQL Unique Fruits Application

### Team Members
- Hamid El Messaoudi

### Quick Start

1. Set up a virtual environment:
    ```bash
    python3 -m venv python_venv
    source python_venv/bin/activate
    ```

2. Install dependencies:
    ```bash
    pip3 install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python3 main.py
    ```

### Endpoints
- `[/api/update_basket_a](http://127.0.0.1:5000/api/update_basket_a)` - Adds "Cherry" to `basket_a`
- `[/api/unique](http://127.0.0.1:5000/api/unique)` - Displays unique fruits from `basket_a` and `basket_b`
