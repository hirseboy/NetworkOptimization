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
                print(f"Testing {solver} on {file_name}...")
                res = find_mass_flux(file_path, solver)
                results.append(res)
            except Exception as e:
                print(f"Error using {solver} on {file_name}: {e}")
                results.append({
                    "file": file_name,
                    "solver": solver,
                    "status": "ERROR",
                    "total_cost": None,
                    "solve_time_sec": None
                })

    print("\n==== Test Summary ====",len(results))
    # for r in results:
    #     if r['file'] :
    #         print(f"{r['file']:25s} | {r['solver']:6s} | Status: {r['status']:9s} | "
    #           f"Cost: {r['total_cost']:.0f} | Time: {r['solve_time_sec']}s")

    return results