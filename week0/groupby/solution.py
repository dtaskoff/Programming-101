from collections import defaultdict

# returns a dictionary with keys the results of 'func'
# on items from 'seq' and values - the items from 'seq'
# i.e. 'groups'['func'(item)] = item
def groupby(func, seq):
    groups = {}
    groups = defaultdict(lambda: [])

    for item in seq:
        groups[func(item)].append(item)

    return dict(groups)