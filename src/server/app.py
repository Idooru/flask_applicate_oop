from flask import Flask, Blueprint

from src.layer.blueprint.phase1_blueprint import Phase1BlueprintGenerator


class FlaskApp:
    phase1: Blueprint
    app: Flask

    def __init__(self, phase1: Blueprint):
        self.phase1 = phase1
        self.app = Flask(__name__)

    def set_blue_print_to_app(self):
        self.app.register_blueprint(self.phase1)

    def run_app(self):
        self.app.run(debug=True)


class FlaskAppProvider:

    @staticmethod
    def init_flask_app():
        phase1 = Phase1BlueprintGenerator.generate_blue_print()
        flask_app = FlaskApp(phase1)
        flask_app.set_blue_print_to_app()
        flask_app.run_app()


if __name__ == "__main__":
    FlaskAppProvider.init_flask_app()
