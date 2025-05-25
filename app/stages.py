# stages.py
import numpy as np
from info import get_stage_info

def interpolate_stage(track, step_frac):
    temps = np.array(track.get("temp", []))
    lums = np.array(track.get("lum", []))
    stages = track.get("stages", [])
    n_steps = len(temps)

    if n_steps < 2:
        raise ValueError("Insufficient data points for interpolation.")

    idx = int(step_frac * (n_steps - 1))
    interp_frac = (step_frac * (n_steps - 1)) % 1

    temp_interp = (1 - interp_frac) * temps[idx] + interp_frac * temps[min(idx + 1, n_steps - 1)]
    lum_interp = (1 - interp_frac) * lums[idx] + interp_frac * lums[min(idx + 1, n_steps - 1)]
    stage = stages[idx] if idx < len(stages) else "Unknown"

    return temp_interp, lum_interp, stage


def get_stage_details(stage, temp, lum, mass_val):
    info = get_stage_info(stage.strip(), temp, lum, mass=mass_val)
    # Safely handle missing info keys
    return {
        "stage": info.get("stage", stage),
        "structure": info.get("structure", "Unknown"),
        "temperature": info.get("temperature", "N/A"),
        "luminosity": info.get("luminosity", "N/A"),
        "age_estimate": info.get("age_estimate", "N/A"),
        "description": info.get("description", "No description available.")
    }
