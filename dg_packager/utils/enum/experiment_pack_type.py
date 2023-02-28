from enum import Enum
from dg_packager.error.error import EnumValueError

class ExperimentPackType(Enum):
    '''
    実験パッケージの要素
    '''

    EXPERIMENTS = 'experiments'
    INPUT_DATA = 'input_data'
    SOURCE = 'source'
    OUTPUT_DATA = 'output_data'
    PARAM = 'param'
    GIT_KEEP = '.gitkeep'

    @classmethod
    def value_of(cls, target_value):
        for e in ExperimentPackType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in ExperimentPackType Class.'.format(target_value))