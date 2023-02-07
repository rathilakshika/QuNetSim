import random


class PhaseFlip(object):
    """
    The model for a phase flip quantum connection.
    """

    def __init__(self, probability=0.0):
        if not isinstance(probability, int) and not isinstance(probability, float):
            raise ValueError("Phase Flip probability must be float or int")
        elif probability < 0 or probability > 1:
            raise ValueError("Phase Flip probability must lie in the interval [0, 1]")
        else:
            self._p = probability

    @property
    def phaseflip_probability(self):
        """
        Probability of phase flip of qubit

        Returns
            (float) : Probability that a qubit's phase is flipped during transmission
        """
        return self._p

    @phaseflip_probability.setter
    def phaseflip_probability(self, probability):
        """
        Set the phase flip probability of the channel

        Args
            probability (float) : Probability that a qubit's phase is flipped during transmission
        """
        if not isinstance(probability, int) and not isinstance(probability, float):
            raise ValueError("Phase flip probability must be float or int")
        elif probability < 0 or probability > 1:
            raise ValueError("Phase flip probability must lie in the interval [0, 1]")
        else:
            self._p = probability

    def qubit_func(self, qubit):
        """
        Function to modify the qubit based on channel properties
        In this case - Returns None if qubit is erased, otherwise returns the original qubit
        Required in all channel models

        Returns
            (object) : Modified qubit
        """
        if random.random() > (1.0 - self.phaseflip_probability):
            if qubit is not None:
                #qubit.release()
                qubit.Z()
            return qubit
        else:
            return qubit
