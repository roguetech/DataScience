from math import log10

def erlangB(A, k):
    """ Erlang B formula
        Also known as the Erlang loss formula

        Parameters
        ----------
        A : float
            offered load. Should be less than `k`
        k : integer
            number of servers or "trunks"

        Returns
        -------
        float
    """
    invB = 1.0
    for m in xrange(1,k+1):
        invB = 1.0 + (m/A)*invB
    return 1.0/invB

A = 25.0
N = 30
erlang = erlangB(A, N)
#Mhat = A * erlang(N,A)
Mhat = A * erlang
print Mhat
Vhat = Mhat * (1 - Mhat + (A / (N + 1 - A + Mhat)))
print Vhat

M = 3 * Mhat
V = 3 * Vhat
Z = V / M

print M
print V
print Z

Astar = V + 3 * Z * (Z-1)
Nstar = (Astar * (M + Z) / M + Z -1) - M - 1

print Astar
print Nstar

#loads = [20.0, 30.0, 25.0]

#macrocost = 3.0
