import random

from model_properties.network_params import Params
from policy.states_policy import Policy


class SelectionPolicy:

    POLICY = None

    @classmethod
    def set_policy(cls, strategy: tuple, states_with_policy: list, params: Params):
        SelectionPolicy.POLICY = Policy(strategy, states_with_policy, params)

    @classmethod
    def set_strategy(cls, strategy: tuple):
        SelectionPolicy.POLICY.strategy = strategy

    @classmethod
    def according_to_policy(cls, state: list):
        # TODO: преобразовать state в tuple вида ((q1, q2), ((a1...an), (b1...bm)))
        # state = (state[0], state[1]), (tuple(sorted()), tuple(sorted()))
        return SelectionPolicy.POLICY.strategy[SelectionPolicy.POLICY.states_with_policy.index(state)]

    @staticmethod
    def direct_order(state: list) -> int:
        return 0

    @staticmethod
    def reverse_order(state: list) -> int:
        return 1

    @staticmethod
    def random_order(state: list) -> int:
        return random.randint(0, 1)
