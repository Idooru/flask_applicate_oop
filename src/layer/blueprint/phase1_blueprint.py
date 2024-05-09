from flask import Blueprint

from src.layer.controller.phase1_controller import Phase1ControllerProvider


class Phase1BlueprintGenerator:

    @staticmethod
    def generate_blue_print() -> Blueprint:
        phase1: Blueprint = Blueprint(name="phase1", import_name=__name__, url_prefix="/phase1")
        Phase1ControllerProvider.init_phase1_controller(phase1)

        return phase1
