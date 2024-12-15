from app import create_app, db
from app.routes import api

app = create_app()
app.register_blueprint(api, url_prefix='/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(host='0.0.0.0', port=5001)
