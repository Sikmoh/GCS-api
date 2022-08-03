from errors.v1 import handlers as error_handlers
import connexion


app = connexion.FlaskApp(__name__)

app.add_api('openapi.yaml',
            strict_validation=True,
            arguments={'title': 'Aerolab GCS'})
app.app.register_blueprint(error_handlers.error_handlers)

if __name__ == '__main__':
    app.run()
