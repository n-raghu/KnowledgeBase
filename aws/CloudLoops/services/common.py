import sys

def required_attributes(resource) -> list:
    if resource == 'instances':
        return ['ImageId', 'InstanceId', 'InstanceType', 'LaunchTime', 'Architecture']
    if resource == 'images':
        return ['PlatformDetails', 'Name', 'RootDeviceType']


def tree_traverse(tree, key):
    for k, v  in tree.items():
        if k == key:
            return v
        elif isinstance(v, dict):
            found = tree_traverse(v, key) 
            if found is not None:  # check if recursive call found it
                return found
