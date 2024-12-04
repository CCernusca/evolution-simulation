
# Imports
...

# Classes
class Trait:
    """
    A mutatable trait, which is given to creatures by their simulation and then influences their life. Traits are also passed on to children creatures, with slight mutations.

    Attributes
    ----------
        name : str
               The name of the trait.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a trait.

        Parameters
        ----------
            name : str
                The name of the trait.
        
        Returns
        -------
            None
        """
        self.name = name
