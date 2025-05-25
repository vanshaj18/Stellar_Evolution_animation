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
        # For lower mass stars: L ∝ M^5.5 * R^-0.5
        luminosity = (mass ** 5.5) * (radius ** -0.5)
        
    return luminosity
