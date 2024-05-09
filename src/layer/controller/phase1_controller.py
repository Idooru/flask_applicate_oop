from flask import Blueprint, jsonify

from src.interface.controller_interface import ControllerInterface
from src.layer.service.phase1_service import Phase1Service, Phase1ServiceProvider


class Phase1Controller(ControllerInterface):
    phase1_service: Phase1Service

    def __init__(self, phase1_service: Phase1Service):
        self.phase1_service = phase1_service

    def get_plot_chart(self):
        result = self.phase1_service.get_plot_chart()

        json: dict = {
            "success": True,
            "result": result
        }

        return jsonify(json)

    def route(self, app: Blueprint):
        app.get("name")(self.get_plot_chart)


class Phase1ControllerProvider:
    @staticmethod
    def init_phase1_controller(blue_print: Blueprint):
        phase1_service = Phase1ServiceProvider.init_phase1_service()
        phase1_controller = Phase1Controller(phase1_service)

        phase1_controller.route(blue_print)
