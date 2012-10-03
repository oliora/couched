def DocFilter(filterStr=None):
    if filterStr is None:
        return lambda x: True
    elif filterStr == 'd':
        return lambda x: x.startswith('_design/')
    elif filterStr == 'u':
        return lambda x: not x.startswith('_design/')
    else:
        raise Exception("Unknown filter '{0}'".format(filterStr))