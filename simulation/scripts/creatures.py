
# Imports
...

# Classes
class Creature:
    """
    A creature of a simulation with traits. It lives its life in the simulation, reproducing and dying. It also passes its traits on to its children.

    Attributes
    ----------
        id : int
             A unique identifier for this creature.
    """

    def __init__(self, id: int) -> None:
        """
        A creature of a simulation with traits. It lives its life in the simulation, reproducing and dying. It also passes its traits on to its children.

        Parameters
        ----------
            id : int
                A unique identifier for this creature.
        
        Returns
        -------
            None
        """
        self.id = id
