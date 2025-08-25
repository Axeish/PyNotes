class Treenode:
    def __init__(self,data):
        self.data = data
        self.child =[]
    def add_child(self, child):
        self.child.append(child)

    def print_tree(self,prefix=""):
        print(f"{prefix}{self.data}")
        for i,each in enumerate(self.child):
            new_prefix = " |-- "
            each.print_tree( new_prefix)

    def print_clean_tree(self, prefix="", is_last =True):
        branch= "\u2514\u2500" if is_last else "\u251c\u2500"
        print(prefix+branch+self.data)
        child_prefix =  prefix+ ("  " if is_last else "| ")

        for i, node in enumerate(self.child):
            is_last_c = (i==len(self.child)-1)
            node.print_clean_tree( child_prefix,is_last_c )


a = Treenode("A")
ba = Treenode( "BA")
ca = Treenode ("CA")
db= Treenode("DB")
eb= Treenode("EB")
gc = Treenode("GC")
hc = Treenode( "HC")
ig = Treenode ("IG")
jg= Treenode("JG")
kj= Treenode("KJ")
lj= Treenode("LJ")

a.add_child(ba)
a.add_child(ca)
ba.add_child(db)
ba.add_child(eb)
ca.add_child(gc)
ca.add_child(hc)
gc.add_child(ig)
gc.add_child(jg)
jg.add_child(kj)
jg.add_child(lj)


a.print_clean_tree()