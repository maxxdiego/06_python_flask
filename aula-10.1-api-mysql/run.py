from api import app, db

if __name__ == "__main__":
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)
    
