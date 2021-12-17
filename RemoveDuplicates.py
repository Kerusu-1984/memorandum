import json

def RemoveDuplicates(dictlist1,dictlist2):
    distinct_dictlist = list(map(json.loads,set(map(json.dumps,dictlist1)-set(map(json.dumps,dictlist2)))))
    return distinct_dictlist