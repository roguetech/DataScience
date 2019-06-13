from math import log10

def erlangB(A, N):
    """ Erlang B formula
        A offered load
        N number of servers or "trunks"
    """
    invB = 1.0
    for m in xrange(1,N+1):
        invB = 1.0 + (m/A)*invB
    return 1.0/invB

""" Declare the three primary loads, one for each primary microcell"""
loads = [20.0, 30.0, 25.0]

""" Start a for loop to iterate over a range of possible servers/number of channels from 10 to 35"""
for servers in range (10, 36):
    """ Star a for loop to iterate over the different loads on the primary cells"""
    for i in range(len(loads)):
        """ declare a variable of the function erlangB with the load and the server, this calls the erlangB function above
            to calculate using the erlangb formula"""
        erlang = erlangB(loads[i], servers)

        """ calculate M hat """
        Mhat = loads[i] * erlang
        """ calculate V hat """
        Vhat = Mhat * (1 - Mhat + (loads[i] / (servers + 1 - loads[i] + Mhat)))

        """ Calculate the M (Mean) which is the number of primary groups multiplied by M hat"""
        M = 3 * Mhat
        """ Calculate the V (Variance) which is the number of primary groups multiplied by V hat"""
        V = 3 * Vhat
        """ Calculate the Z (the peakedness) which is the variance divided by the mean"""
        Z = V / M

        """ As per Rapps Approvimation calculate A* and N* """
        Astar = V + 3 * Z * (Z-1)
        Nstar = (Astar * (M + Z) / M + Z -1) - M - 1

        erlang1 = erlangB(Astar, int(Nstar))

        print("Number of erlangs offered " + str( Astar ) + " Number of servers " + str(Nstar) + " resulting in " + str(erlang1) + " probabilty of loss")
    microcost = 1.0 + float(servers)
    macro = Astar - Nstar
    macrocost = 3.0 * macro
    print("resulting in Micro cost of: " + str(microcost))
    print("resulting in Macro cost of: " + str(macrocost))
    print("=====================================================================================================")
