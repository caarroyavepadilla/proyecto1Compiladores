TYPES = ["int", "boolean", "char"]

class Scope:
    def __init__(self, id=0, name="global", parent=None, params=None, type = None):
        self.id = id
        self.type = type
        self.name = name
        self.parent = parent
        self.instantiables = []
        self.symbols = []

    def get_instance(self, name):
        for ins in self.instantiables:
            if ins.name == name:
                return ins

    def get_symbol(self, name):
        for sym in self.symbols:
            if sym.name == name:
                return sym

    def get_sub_att(self, instance_name, sub_name):
        for instance in self.instantiables:
            if instance.name == instance_name:
                for sub in instance.sub_att:
                    if sub.name == sub_name:
                        return sub
        return None


    def add_insta(self, id, name, type, ret=None, subs=[], size=0):
        insta = Instantaible(id, name, type, ret, subs, size)
        self.instantiables.append(insta)

    def add_symbol(self, type, id=0, name=None, offset=0):
        symbol = Symbol(type, id, name, offset)
        self.symbols.append(symbol)

class Instantaible:
    def __init__(self, id=0, name=None, type=None, ret=None, subs=[], size=0):
        self.id = id
        self.name = name
        if type == "struct":
            self.type = type
            self.size = size
            self.sub_att = subs
        else:
            self.type = type
            self.ret = ret
            self.params = subs

class Symbol:
    def __init__(self, type, name,  id=0, offset=0):
        self.id = id
        self.type = type
        self.name = name
        self.offset = offset

class Error:
    def __init__(self, prob, line, column):
        self.prob = prob
        self.line = line
        self.column = column

