from pathlib import Path
from app.core import find_mass_flux
def main():
    file_path = Path(__file__).resolve().parents[0] / 'data' / 'testcase04.vicus'
    print(file_path)
    find_mass_flux(file_path,"GLPK")

if __name__ == "__main__":
    main()
