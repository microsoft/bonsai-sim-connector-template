from connector.adder import Adder
from typing import NamedTuple, Dict, Any

class SimulatorModel:
    """
    Manages the Adder that represents the simulation for this sample.
    Implements the reset and step methods required for a Bonsai simulator.
    """

    def __init__(self):
        """ Perform global initialization here if needed before running episodes. """
        # TODO: Perform any global runtime simulator initialization that is needed here.
        pass

    def reset(self, config) -> Dict[str, Any]:
        """ Reset any state from the previous episode and get ready to start a new episode. """
        # TODO: Reset state from the previous episode that needs to be cleared.
        # TODO: Perform initialization in preparation for running an episode using the values in the config dictionary.
        self.adder = Adder(config['initial_value'])
        # TODO: Return initial episode simulation state dictionary.
        return { 'sim_halted': False, 'value': self.adder.value }

    def step(self, action) -> Dict[str, Any]:
        """ Apply the specified action and perform one simulation step. """
        # TODO: Perform a simulation step using the values in the action dictionary.
        self.adder.add(action['addend'])
        # TODO: Return an updated simulation state dictionary from the simulation.
        # TODO: If 'sim_halted' is set to True, that indicates that the simulator is unable to continue and the
        # episode will be discarded. If your simulator can reach an unrecoverable state, set 'sim_halted' to False.
        return { 'sim_halted': False, 'value': self.adder.value }
