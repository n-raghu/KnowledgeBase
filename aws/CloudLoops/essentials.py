from yaml import safe_load

with open('app.yml') as ymlfile:
    yfile = safe_load(ymlfile)


def get_svc_cfg():
    return yfile


def tree_traverse(tree, key):
    for k, v  in tree.items():
        if k == key:
            return v
        elif isinstance(v, dict):
            found = tree_traverse(v, key) 
            if found is not None:  # check if recursive call found it
                return found
