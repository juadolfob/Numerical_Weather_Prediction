# Global Variables

# U - Speed of propagation of the fastest waves described by the equations.
# UΔt/Δx<C
U = 1


def T(N_v, N_c, N_t, R):
    """
    Calculates the time required to make a prediction.

    :param N_v: Number of variables to be processed.
    :param N_c: Number of calculations to be made per variable for a time step Δt.
    :param N_t: Number of time steps needed to reach a given time range H, namely, N_t = H/Δt.
    :param R:  Computer’s calculating speed R; is expressed as flops.
    :return: T – time required to make a prediction for a given time range H.
    """
    return N_v * N_c * N_t / R


