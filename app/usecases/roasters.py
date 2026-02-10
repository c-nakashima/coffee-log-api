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
    return repo.list_roasters()
