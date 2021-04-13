from graphene import Enum


class ModelSpecifications(Enum):
    SATANIC_I = {
        'model': 'satanic_version_i',
        'fpath': 'bible/learning_models/satanic_version_i',
        'about': 'LSTM de 150 camadas ocultas treinada em 1000 epochs sobre ' \
                 'LR 0.01 sobre uma fatia [300:400] pre-processada da' \
                 ' biblia satânica.'
    }
    SATANIC_II = {
        'model': 'satanic_version_ii',
        'fpath': 'bible/learning_models/satanic_version_ii',
        'about': 'LSTM de 180 camadas ocultas treinada em 3000 epochs sobre ' \
                 'LR 0.01 sobre uma fatia [300:400] pre-processada da' \
                 ' biblia satânica.'
    }
    SATANIC_III = {
        'model': 'satanic_version_iii',
        'fpath': 'bible/learning_models/satanic_version_iii',
        'about': 'LSTM de 220 camadas ocultas treinada em 2500 epochs com ' \
                 'LR 0.01 sobre uma fatia [600:700] pre-processada da' \
                 ' biblia satânica com Total Loss 19.8502 de convergência.'
    }
