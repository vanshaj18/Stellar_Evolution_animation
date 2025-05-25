def get_stage_info(stage, temp, lum, mass):
    """
    Return details about the star's evolutionary stage.
    """
    info = {
        "stage": stage,
        "temperature": f"{temp:.0f} K",
        "luminosity": f"{lum:.2f} L☉",
        "structure": "",
        "description": "",
        "age_estimate": ""
    }

    # Age estimation logic (rough)
    if mass <= 1:
        main_seq_lifetime = 10e9  # years
    elif mass <= 5:
        main_seq_lifetime = 0.5e9
    else:
        main_seq_lifetime = 0.01e9  # years

    if stage == "Main Sequence":
        info["structure"] = "Hydrogen fusion in the core"
        info["description"] = (
            "Stable phase where hydrogen fuses into helium. This phase dominates a star’s lifetime."
        )
        info["age_estimate"] = f"~{main_seq_lifetime / 1e9:.2f} billion years"

    elif stage in ["Subgiant", "Red Giant", "Giant"]:
        info["structure"] = "Helium core, hydrogen shell burning"
        info["description"] = (
            "Hydrogen shell burning surrounds an inert helium core. Star expands and cools."
        )
        info["age_estimate"] = f"{0.01 * main_seq_lifetime / 1e9:.2f} billion years"

    elif stage == "Supergiant":
        info["structure"] = "Helium/C/O shell burning with iron core"
        info["description"] = (
            "Massive stars develop multiple shells of fusion around a dense iron core. Highly luminous."
        )
        info["age_estimate"] = f"{0.005 * main_seq_lifetime / 1e9:.3f} billion years"

    elif stage == "White Dwarf":
        info["structure"] = "Carbon-oxygen core, no fusion"
        info["description"] = (
            "Degenerate remnant, slowly cooling. Supported by electron degeneracy pressure."
        )
        info["age_estimate"] = "Cools over billions of years"

    elif stage == "Supernova":
        info["structure"] = "Iron core collapse"
        info["description"] = (
            "Dramatic core collapse leads to massive explosion. Heavier elements scattered into space."
        )
        info["age_estimate"] = "Short duration (~days to weeks)"

    elif stage == "Neutron Star":
        info["structure"] = "Degenerate neutron matter"
        info["description"] = (
            "Extremely dense remnant of a supernova, composed mainly of neutrons."
        )
        info["age_estimate"] = "Cools over billions of years"

    else:
        info["structure"] = "Unknown"
        info["description"] = "Unknown stage."
        info["age_estimate"] = "N/A"

    return info
