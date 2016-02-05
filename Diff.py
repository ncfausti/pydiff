import json
class Diff:
    def __init__(self):
        self.first = {}
        self.second = {}
        self.results = {}

    def walk(self, obj, parent=""):
        for k,v in obj.iteritems():
            if isinstance(v, dict):
                self.walk(v,k)
            else:
                if parent:
                    if k in self.second[parent]:
                        if v != self.second[parent][k]:
                            self.results[parent] = {k:self.second[parent][k]}
                else:
                    # New Item
                    if k in self.second and k not in self.first:
                        self.results[k] = self.second[k]
                    # Deleted Item
                    if k in self.first and k not in self.second:
                        self.results[k] = "undefined"
                    # Updated Item
                    if k in self.first and k in self.second:
                        if self.first[k] != self.second[k]:
                            self.results[k] = self.second[k]

    # Takes in two raw json strings
    # Returns difference as json object
    def diff(self, first, second):
        self.first = json.loads(first)
        self.second = json.loads(second)
        self.walk(self.first)
        self.walk(self.second)
        return self.results

jsonA1 = """
{
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
jsonA2 = """
{
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

differenceA = json.loads('''
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


jsonB1 = """
{
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
jsonB2 = """
{
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

differenceB = json.loads('''
{

}''')

jsonC1 = """
{
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
  "miss": 999999
}
"""
jsonC2 = """
{
  "foo": {
    "bar": "baz",
    "biz": "foo"
  },
  "fiz": {
    "foo": "baz",
    "new": "zab"
  },
  "bar": "baz",
  "baz": [
    "foo",
    "bar"
  ],
  "miss": 123
}
"""

differenceC = json.loads('''
{
"miss":123
}''')

###       ###
### TESTS ###
###       ###
test = Diff()
resultsA = test.diff(jsonA1,jsonA2)

test = Diff()
resultsB = test.diff(jsonB1,jsonB2)

test = Diff()
resultsC = test.diff(jsonC1,jsonC2)

assert(resultsA == differenceA)
print resultsA

assert(resultsB == differenceB)
print resultsB

print resultsC
assert(resultsC == differenceC)
