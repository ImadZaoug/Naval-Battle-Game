# Game Simulation

This repository contains a Python implementation of a naval warfare simulation. The simulation includes various vessels, weapons, and a battlefield where players can engage in strategic battles.

## Folder Structure

- **model**
  - **weapon.py**: Defines the `Weapon` class used by various vessels.
  - **vessel.py**: Contains the `Vessel` class representing naval vessels.
  - **torpedos_launcher.py**: Implements the `TorpedoLauncher` class, a type of weapon.
  - **surface_missile_launcher.py**: Implements the `SurfaceMissileLauncher` class, another type of weapon.
  - **submarine.py**: Defines the `Submarine` class, a specific type of vessel.
  - **destroyer.py**: Defines the `Destroyer` class, another type of vessel.
  - **cruiser.py**: Implements the `Cruiser` class, representing a powerful naval vessel.
  - **frigate.py**: Implements the `Frigate` class, a versatile type of vessel.
  - **air_missile_launcher.py**: Implements the `AirMissileLauncher` class, a weapon for aerial attacks.
  - **aircraft.py**: Defines the `Aircraft` class, representing airborne vessels.
  - **exceptions.py**: Contains custom exception classes used in the simulation.
  - **battlefield.py**: Implements the `Battlefield` class, defining the space where naval battles take place.
  - **player.py**: Defines the `Player` class, representing a participant in the simulation.

- **requirements.txt**: Lists the required Python packages for running the simulation.

## Usage

1. Install the required packages using `pip install -r requirements.txt`.
2. Explore the various model components in the `model` folder.
3. Use the provided classes to create and simulate naval battles in your own Python scripts.

## Notes

- The simulation includes vessels such as submarines, destroyers, cruisers, frigates, and aircraft.
- Each vessel has specific characteristics, including weapons, coordinates, and hit points.
- Weapons include torpedoes, surface missiles, and air-to-surface missiles.
- The `Battlefield` class provides a space for vessels to engage in battles.
- Custom exceptions handle various scenarios, such as running out of ammunition, vessels being destroyed, and out-of-range targets.

Feel free to explore and modify the code to suit your simulation needs!
