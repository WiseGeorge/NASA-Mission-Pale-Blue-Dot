from joblib import load, dump


class WTV_Models:

    def __init__(self, USAC_Path='WorldTemperatureViewerModels/usa_cities.joblib') -> None:
        self.model = load(USAC_Path)
        self.cities = list(self.model.keys())
