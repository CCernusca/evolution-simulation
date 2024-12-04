
# Imports
import scripts.traits as traits

# Classes
class Creature:
    """
    A creature of a simulation with traits. It lives its life in the simulation, reproducing and dying. It also passes its traits on to its children.

    Attributes
    ----------
        id : int
             A unique identifier for this creature.
        traits : dict[str: traits.Trait]
            A dictionary of traits, where the key is the name of the trait and the value is the trait itself.
    """

    def __init__(self, id: int, *trait_list: traits.Trait) -> None:
        """
        A creature of a simulation with traits. It lives its life in the simulation, reproducing and dying. It also passes its traits on to its children.

        Parameters
        ----------
            id : int
                 A unique identifier for this creature.
            traits : dict[str: traits.Trait]
                     A dictionary of traits, where the key is the name of the trait and the value is the trait itself.
        
        Returns
        -------
            None
        """
        self.id = id
        self.traits = {trait.name: trait for trait in trait_list}
    
    def get_traits(self, copy: bool = False) -> dict[str: traits.Trait]:
        """
        Retrieves the traits of the creature.

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
