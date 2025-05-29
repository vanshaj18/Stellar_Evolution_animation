#based on the opacity relations, the Luminostiy varies for 
# the main sequence stars.

import math


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
        # if radius is None:
        #     raise ValueError("Radius must be provided for mass <= mass_constant")
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

    return t_kh_time

def calculate_M_hook(Z):
    """
    Calculate the critical mass for the Hook's law for a star with metallicity Z.
    
    Parameters:
    - Z: float, metallicity of the star (in solar units)

    Returns:
    - M_hook: float, critical mass (in solar masses)
    """
    ki = math.log(Z/0.02)
    
    M_hook = 1.0185 + 0.16015 * ki + 0.0892 * ki**2  
    # taken from the paper: 
    # Comprehensive analytic formulae for stellar evolution as a function of mass and metallicity
    
    return M_hook

async def async_calculate_M_hef (Z):
    ki = math.log(Z/0.02)
    m_hef = (1.995 + 0.25 * ki + 0.087 * ki**2)

    return m_hef
    
async def async_calculate_M_fgb (Z):
    m_fgb = (13.048 * (Z / 0.02)**0.06) / (1 + 0.0012 * (0.02 / Z)**1.27)
    return m_fgb