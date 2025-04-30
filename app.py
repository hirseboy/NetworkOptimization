from pathlib import Path
from app.core import find_mass_flux
def main():
    # data/test_scenarios/enough_supply_for_all_nodes.vicus
    # file_path = Path(__file__).resolve().parents[0] / 'data' / 'test_scenarios'/'testcase04.vicus'
    # file_path = Path(__file__).resolve().parents[0] / 'data' / 'test_scenarios'/'connected_testcase04.vicus'
    # print(file_path)
    # find_mass_flux(file_path)

    folder_path = Path(__file__).resolve().parents[0] / 'data' / 'test_scenarios'

    # Get all .vicus files in the folder
    vicus_files = folder_path.glob('*.vicus')

    # Run the function on each file
    for file_path in vicus_files:
        print(f"Running on: {file_path}")
        find_mass_flux(file_path)

if __name__ == "__main__":
    main()
