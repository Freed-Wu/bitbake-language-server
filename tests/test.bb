inherit test

def get_base_dep(d):
    if d.getVar('INHIBIT_DEFAULT_DEPS', False):
        return ""
    return "${BASE_DEFAULT_DEPS}"
