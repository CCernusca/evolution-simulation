
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

    def __init__(self, creature_start_count: int, *trait_list: traits.Trait) -> None:
        """
        Initializes a simulation.

        Parameters
        ----------
            creature_start_count : int
                The number of creatures the simulation starts with.
            trait_list : list[traits.Trait]
                The mutatable traits of the simulation, which the simulation passes on to its creatures at their creation.
        """
        self.creature_start_count: int = creature_start_count
        self.traits: dict[str: traits.Trait] = {trait.name: trait for trait in trait_list}
        self.creatures: dict[int: creatures.Creature] = {i: creatures.Creature(i, *self.traits) for i in range(creature_start_count)}
    
    def get_traits(self, copy: bool = False) -> dict[str: traits.Trait]:
        """
        Retrieves the traits of the simulation.

        Parameters
        ----------
            copy : bool, optional
                If True, returns a copy of each trait; otherwise, returns the original traits.

        Returns
        -------
            dict[str: traits.Trait]
                A dictionary of traits, where the key is the name of the trait and the value is the trait itself.
        """
        if copy:
            return {name: self.traits[name].copy() for name in self.traits}
        else:
            return self.traits
    
    def cycle(self) -> None:
        """
        Runs one cycle of all creatures in the simulation.
        """
        creatures_copy = self.creatures.copy()
        for creature in self.creatures.values():
            creature.cycle(creatures_copy)
        self.creatures.update(creatures_copy)
