from priv_lib_estimator import Estimator


class Estim_time(Estimator):
    CORE_COL = {'Comput. Time'}

    def __init__(self):
        super().__init__()