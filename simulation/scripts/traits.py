
# Imports
import numpy as np

# Constants
MUTATION_FACTOR = 0.1

# Classes
class Trait:
    """
    A mutatable trait, which is given to creatures by their simulation and then influences their life. Traits are also passed on to children creatures, with slight mutations.

    Attributes
    ----------
        name : str
               The name of the trait.
        value : Any
                The value of the trait.
    """

    def __init__(self, name: str, value) -> None:
        """
        Initializes a trait.

        Parameters
        ----------
            name : str
                   The name of the trait.
            value : Any
                    The value of the trait.
        """
        self.name = name
        self.value = value
    
    def copy(self) -> 'Trait':
        """
        Creates a copy of the trait.

        Returns
        -------
            Trait
                A new instance of Trait with the same attributes as this trait.
        """
        return Trait(self.name, self.value)

    def mutate(self) -> 'Trait':
        """
        Mutates the trait by multiplying its value by a number between 1-MUTATION_FACTOR and 1+MUTATION_FACTOR.

        Returns
        -------
            Trait
                A new instance of Trait with the same name as this trait and a mutated value.
        """
        
        return Trait(self.name, self.value * np.random.uniform(1 - MUTATION_FACTOR, 1 + MUTATION_FACTOR))
