import os

import pytest

path_file = "prod_file.pkl"

@pytest.fixture(autouse=True)
def delete_prod_file():
    if os.path.isfile(path_file):
        os.remove(path_file)
        print("File delete")
    else:
        print("File not found")