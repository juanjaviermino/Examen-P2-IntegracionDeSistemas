from app import create_app, db
from app.routes import inventory

app = create_app()
app.register_blueprint(inventory, url_prefix='/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Asegurarse de que las tablas existen
    app.run(host='0.0.0.0', port=5003)
