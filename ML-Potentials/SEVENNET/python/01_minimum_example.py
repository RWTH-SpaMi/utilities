"""Minimal example of using the SEVENNET calculator with ASE."""

from ase.build import bulk
from sevenn.sevennet_calculator import SevenNetCalculator

structure_ase = bulk("Cu", "fcc", a=3.6)
structure_ase.calc = SevenNetCalculator("7net-0")
structure_ase.get_potential_energy()
