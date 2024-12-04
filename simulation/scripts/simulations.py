
# Imports
import scripts.traits as traits
import scripts.creatures as creatures

# Classes
class Simulation:
    """
    A class for a simulaton, which holds creatures and manages simulating their evolution and environment.

    Attributes
    ----------
        creature_start_count : int
                               The number of creatures the simulation starts with.
        creatures : list[creatures.Creature]
                    The creatures inhabiting the simulation.
        traits : list[traits.Trait]
                 The mutatable traits of the simulation, which the simulation passes on to its creatures at their creation.
    """

    def __init__(self, creature_start_count: int) -> None:
        """
        Initializes a simulation.

        Parameters
        ----------
            creature_start_count : int
                                   The number of creatures the simulation starts with.
        
        Returns
        -------
            None
        """
        self.creature_start_count: int = creature_start_count
        self.creatures: list[creatures.Creature] = [''] * creature_start_count
        self.traits: list[traits.Trait] = []

    def add_trait(self, trait: traits.Trait) -> None:
        """
        Adds a new mutatable trait of creatures to the simulation.

        Parameters
        ----------
            trait : traits.Trait
                    The trait to add.
        
        Returns
        -------
            None
        """
        self.traits.append(trait)
