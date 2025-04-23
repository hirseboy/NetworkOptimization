from pathlib import Path
from app.core import find_mass_flux
def main():
    # data/test_scenarios/enough_supply_for_all_nodes.vicus
    # file_path = Path(__file__).resolve().parents[0] / 'data' / 'test_scenarios'/'testcase04.vicus'
    file_path = Path(__file__).resolve().parents[0] / 'data' / 'test_scenarios'/'enough_supply_for_all_nodes.vicus'
    print(file_path)
    find_mass_flux(file_path,"GLPK")

if __name__ == "__main__":
    main()
