import os

license_content = os.getenv("GUROBI_LICENSE")

if license_content:
    with open(os.path.expanduser("~/gurobi.lic"), "w") as f:
        f.write(license_content)
    print("Gurobi license file written.")
else:
    print("Gurobi license not found in environment.")
