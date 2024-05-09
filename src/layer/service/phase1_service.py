from typing import List


class Phase1Service:
    def get_plot_chart(self) -> List[int]:
        return [1, 2, 3, 4, 5]


class Phase1ServiceProvider:
    @staticmethod
    def init_phase1_service():
        return Phase1Service()
