
# Imports
# from ..console import main as console
# from ..analysis import main as analysis

import scripts.simulations as simulations

# Functions
def main() -> None:
    """
    Main function of the simulation subdirectory, managing the modules responsible for simulating the simulation.
    """
    sim = simulations.Simulation(10)
    print(sim.get_traits())
    print(sim.creatures[0].get_traits())
    print(sim.creatures)
    print(len(sim.creatures))

    sim.cycle()

    print(sim.get_traits())
    print(sim.creatures[0].get_traits())
    print(sim.creatures)
    print(len(sim.creatures))


# Execution
if __name__ == "__main__":
    main()
