from graphene import Enum


class ModelSpecifications(Enum):
    SATANIC_I = {
        'model': 'satanic_version_i',
        'fpath': 'bible/learning_models/satanic_version_i',
        'about': 'LSTM de 150 camadas ocultas treinada em 1000 epochs sobre ' \
                 'LR 0.01 sobre uma fatia [300:400] pre-processada da' \
                 ' biblia satânica.'
    }
