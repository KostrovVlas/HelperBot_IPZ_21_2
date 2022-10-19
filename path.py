import os
def abs_path(f):
    return os.path.join(os.path.abspath(__file__ + "/.."), f)