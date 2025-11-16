from cgshop2026_pyutils.instance_database import InstanceDatabase
from cgshop2026_pyutils.zip import ZipSolutionIterator
from cgshop2026_pyutils.verify import check_for_errors
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "../input" / "test_instances.zip"
OUTPUT_PATH = BASE_DIR / "../output" / "test_solutions.zip"

db = InstanceDatabase(INPUT_PATH)
for instance in db:
    print(f"Instance: {instance.instance_uid}")

zip_iterator = ZipSolutionIterator(OUTPUT_PATH)
for solution in zip_iterator:
    print(f"Verifying solution for instance: {solution.instance_uid}")
    instance = db[solution.instance_uid]
    errors = check_for_errors(instance, solution)
    if errors:
        print(f"Errors found in solution: {errors}")
    else:
        print("No errors found in solution. Objective value:", solution.objective_value)
