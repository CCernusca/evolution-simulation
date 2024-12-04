
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
        """
        self.id = id
        self.traits = {trait.name: trait for trait in trait_list}
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the creature, containing its id and traits.

        Returns
        -------
            str
                A string representation of the creature.
        """
        return f"{self.__class__.__name__}({self.id}, {self.traits})"

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
    
    def reproduce(self, child_id: int) -> 'Creature':
        """
        Reproduces the creature, returning a new Creature instance with the same traits as this one, but with their values mutated.

        Parameters
        ----------
            child_id : int
                The unique identifier of the child creature.

        Returns
        -------
            Creature
                A new Creature instance with the same traits as this one, but with their values mutated.
        """
        return Creature(child_id, *(trait.mutate() for trait in self.traits.values()))

    def cycle(self, creature_dict: dict[int: 'Creature']) -> None:
        """
        Cycles the creature, causing it to reproduce and add the new creature to the given dictionary of creatures.

        Parameters
        ----------
            creature_dict : dict[int: Creature]
                The dictionary of creatures to which the new child should be added.
        """
        child_id = max(creature_dict) + 1 if len(creature_dict) > 0 else 0
        child = self.reproduce(child_id)
        creature_dict.update({child.id: child})
