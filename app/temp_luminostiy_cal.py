#based on the opacity relations, the Luminostiy varies for 
# the main sequence stars.

def calculate_luminosity(mass, radius=None, mass_constant=1.5):
    """
    Calculate the luminosity of a star near the main sequence.

    Parameters:
    - mass: float, mass of the star (in solar masses)
    - radius: float or None, radius of the star (in solar radii), required if mass <= mass_constant
    - mass_constant: float, threshold mass to switch luminosity relation

    Returns:
    - luminosity: float, luminosity of the star (in solar luminosities)
    """
    if mass > mass_constant:
        # For higher mass stars: L ∝ M^3
        luminosity = mass ** 3
    else:
        if radius is None:
            raise ValueError("Radius must be provided for mass <= mass_constant")
        luminosity = (mass ** 3.5) 
        
    return luminosity

def calculate_kelvin_helmholtz_time(mass, luminosity):
    """
    Calculate the Felvin-Helmholtz time for a star collapse under the liberation of gravitational potential energy.
    Parameters: 
        - mass: float, mass of the star (in solar masses)
        - luiminosity: float, luminosity of the star (in solar luminosities)

    Returns:
        - time: float, Kelvin-Helmholtz time (in years)
    """

    t_kh_const = 8 * 10**7 # constant
    t_kh_time = t_kh_const * (mass / luminosity)