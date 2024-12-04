
# Imports
# from ..console import main as console
# from ..analysis import main as analysis

import scripts.simulations as simulations
import scripts.traits as traits

# Functions
def main() -> None:
    """
    Main function of the simulation subdirectory, managing the modules responsible for simulating the simulation.
    """
    sim = simulations.Simulation(10, traits.Trait("a", 1), traits.Trait("b", 2), traits.Trait("c", 3))
    print(sim)
    print(sim.get_traits())
    print(len(sim.creatures))
    for creature in sim.creatures.values():
        print(creature)

    sim.cycle()

    print(len(sim.creatures))
    for creature in sim.creatures.values():
        print(creature)


# Execution
if __name__ == "__main__":
    main()
