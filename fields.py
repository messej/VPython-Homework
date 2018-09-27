from visual import vector, mag
# might import const
def get_e_field(p, *charges):
    f = vector(0,0,0)
    kel = 9e9     # Coulomb constant
    for c in charges:
        f = f + (p.pos-c.pos) * kel * c.q / mag(p.pos-c.pos)**3
    return f

def get_e_field2(pos, *pos_charge_tuples):
    f = vector(0,0,0)
    kel = 9e9     # Coulomb constant
    for c in pos_charge_tuples:
        f = f + (pos-c[0]) * kel * c[1] / mag(pos-c[0])**3
    return f

def get_g_field(p, *sources):
    f = vector(0,0,0)
    G = 6.674e-11
    for s in sources:
        f = f + (p.pos-s.pos) * G * s.m / mag(p.pos-s.pos)**3
    return f
# I could be cute and make a single function for both e and g
# this function would vary by:
# relavent physical constant and the attribute accessed from sources
# could make it a callable object and store the relavent attrb
