from app.core import find_mass_flux
import os
def test_solvers_on_files(input_folder="data/test_scenarios"):
    solvers = ["CBC", "GLPK", "GUROBI", "CPLEX"]
    files = [f for f in os.listdir(input_folder) if f.endswith(".vicus")]
    results = []

    print("Running solver tests...\n")

    for file_name in files:
        file_path = os.path.join(input_folder, file_name)
        for solver in solvers:
            try:
                # print(f"\t\t\t============================================Testing {solver} on {file_name}========================")
                status, cost = find_mass_flux(file_path, solver)
                # results.append(res)
                results.append({
                    "file": file_name,
                    "solver": solver,
                    "status": status,
                    "total_cost": cost
                })
            except Exception as e:
                print(f"Error using {solver} on {file_name}: {e}")
                results.append({
                    "file": file_name,
                    "solver": solver,
                    "status": "ERROR",
                    "total_cost": None,
                })

    print("\n==== Test Summary ====",len(results))
    for r in results:
        cost = f"{r['total_cost']:.2f}" if r['total_cost'] is not None else "N/A"
        print(f"{r['file']:25s} | {r['solver']:7s} | {r['status']:10s} | {cost:10s} ")

    return results