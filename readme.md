Steps to run
- Set the appropriate environment variables
- Run `pip install -r requirements.txt`
- Perform migrations as follows
    - `flask db init`
    - `flask db migrate -m "Initial migration"`
    - `flask db upgrade`
- Start the app
    - `python app.py`
