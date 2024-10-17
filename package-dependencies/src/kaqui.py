from z3 import *

def DependeDe(pack, deps):
    if is_expr(deps):
        return Implies(pack, deps)
    else:
        return And([ Implies(pack, dep) for dep in deps ])

def Conflito(*packs):
    return Or([ Not(pack) for pack in packs ])

a, b, c, d, e, f, g, z = Bools('a b c d e f g z')

def install_check(*problema):
    s = Solver()
    s.add(*problema)
    if s.check() == sat:
        m = s.model()
        r = []
        for x in m:
            if is_true(m[x]):
                r.append(x())
        print(r)
    else:
        print("Não é possível instalar a configuração desejada")

print("Instância 1")
install_check(DependeDe(a, [b, c, z]),
              DependeDe(b, d),
              DependeDe(c, [Or(d, e), Or(f, g)]),
              Conflito(d, e),
              a, z)

print("Instância 2")
install_check(DependeDe(a, [b, c, z]),
              DependeDe(b, d),
              DependeDe(c, [Or(d, e), Or(f, g)]),
              Conflito(d, e),
              Conflito(d, g),
              a, z)

print("Instância 3")
install_check(DependeDe(a, [b, c, z]),
              DependeDe(b, d),
              DependeDe(c, [Or(d, e), Or(f, g)]),
              Conflito(d, e),
              Conflito(d, g),
              a, z, g)
