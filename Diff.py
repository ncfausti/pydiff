import json

first = """{
  "foo": {
    "bar": "baz",
    "biz": "foo"
  },
  "fiz": {
    "foo": "baz"
  },
  "bar": "baz",
  "baz": [
    "foo",
    "bar"
  ],
  "miss": 123
}
"""
second = """{
  "foo": {
    "bar": "baz1",
    "biz": "foo"
  },
  "fiz": {
    "foo": "baz"
  },
  "bar": "baz",
  "baz": [
    "foo1"
  ],
  "new_value": 1
}
"""

different = json.loads(
'''
{
  "foo": {
    "bar": "baz1"
  },
  "baz": [
    "foo1"
  ],
  "miss": "undefined",
  "new_value": 1
}''')
first, second = json.loads(first), json.loads(second)

same = {}
diff = {}

def walk(obj,level, parent=""):
    level += 1
    for k,v in obj.iteritems():
        if isinstance(v, dict):
            print 'walk({0}, {1}, {2})'.format(v,level,k)
            walk(v, level, k)
        else:
            if parent:
                print "parent: ",parent,"k:", k
                if k in second[parent]:
                    print "second[parent][k]: ", second[parent][k]
                    print "second[parent]: ", second[parent]
                    if v != second[parent][k]:
                        print "MISMATCH"
                        diff[parent] = {k:second[parent][k]}
            else:
                print "k: {0},v:{1}".format(k,v)
                # New Item
                if k in second and k not in first:
                    print "IN SECOND, NOT FIRST", k, v
                    diff[k] = second[k]
                # Deleted Item
                if k in first and k not in second:
                    print "IN FIRST, NOT SECOND", k, v
                    diff[k] = "undefined"
                # Updated Item
                if k in first and k in second:
                    if first[k] != second[k]:
                        diff[k] = second[k]
                        print "UPDATED TO: ", k, second[k]

diff = {}

def add(k,v,toObj):
    toObj[k] = v

#for k,v in first.iteritems():
#    add(k,v,diff)
#add("foo", 123, diff)
print 'DIFF'
#walk(diff, -1)

### Loop through second object checking if K:Vs exist in first,
### If not, add to diff
def update(firstObj, fromObj):
    pass

class Diff:
    def __init__(self):
        pass
print 'FIRST'
walk(first,-1,{})

print "SECOND"
walk(second,-1,{})

### ALGORITHM ###
'''
ls  = set([x for x in first.iterkeys()])
ls2 = set([x for x in second.iterkeys()])
diffKeys = ls.union(ls2)
print "DIFF KEYS\n",diffKeys
'''
### TESTS ###

#assert(d.diff(first, second) == different)

### HOW TO RUN ###
print "DIFFFFF"
print diff
