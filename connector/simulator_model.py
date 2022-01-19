from connector.adder import Adder
from typing import Dict, Any

class SimulatorModel:
    """
    Manages the simulation by implementing the reset and step methods required for a Bonsai simulator.
    """

    def __init__(self):
        """ Perform global initialization here if needed before running episodes. """
        # TODO: Perform any global runtime simulator initialization that is needed here.
        pass

    # <snippet_reset>
    def reset(self, config) -> Dict[str, Any]:
        """ Reset any state from the previous episode and get ready to start a new episode. """
        # TODO: Reset state from the previous episode that needs to be cleared.
        # TODO: Perform initialization in preparation for running an episode using the values in the config dictionary.
        self.adder = Adder(config['initial_value'])
        return { 
            'sim_halted': False,
            # TODO: Add simulator state as dictionary with key as the state and value as the state's value.
            'value': self.adder.value,
        }
    # </snippet_reset>

    # <snippet_step>
    def step(self, action) -> Dict[str, Any]:
        """ Apply the specified action and perform one simulation step. """
        # TODO: Perform a simulation step using the values in the action dictionary.
        self.adder.add(action['addend'])
        return {
            # TODO: If 'sim_halted' is set to True, that indicates that the simulator is unable to continue and the
            # episode will be discarded. If your simulator cannot reach an unrecoverable state, always set 'sim_halted'
            # to False.
            'sim_halted': False,
            # TODO: Add simulator state as dictionary with key as the state and value as the state's value.
            'value': self.adder.value,
        }
    # </snippet_step>
