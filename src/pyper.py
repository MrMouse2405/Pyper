from importlib import import_module as require

def custom_import(name : str)->object:
    return require(name)

def run_python(name : str):
    pass

if __name__ == "__main__":
    print("Running As Main")
else:
    print("Running As Module")
