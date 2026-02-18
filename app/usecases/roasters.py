import re

from app.infra.repositories import roasters as repo


# normalize roaster's name
def normalize_name(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"[^a-z0-9 ]", "", s)
    return s.replace(" ", "-")

# get roaster's list
def get_roasters():
    return repo.get_roasters()


# create a roaster item in the database
def create_roaster(name: str):
    # validate the name
    if not name or not name.strip():
        raise HTTPException(status_code=400, detail="name is required")

    # normalize the name
    input_name_normalized = normalize_name(name)

    # check if the roaster already exists
    existing_roaster = repo.get_by_name_normalized(input_name_normalized)
    if existing_roaster:
        raise ValueError("Roaster already exists")

    return repo.create_roaster(name, input_name_normalized)