import streamlit as st
import time
from shell_strcture import shell_structure_figure
from data import tracks
from stages import interpolate_stage, get_stage_details
from plot import create_hr_diagram

st.set_page_config(page_title="HR Diagram Animator", layout="wide")
st.title("🌟 Stellar Evolution Animation")

# --- Session State Initialization ---
if "auto_run" not in st.session_state:
    st.session_state.auto_run = False
if "step" not in st.session_state:
    st.session_state.step = 0

# --- UI Controls ---
col1, col2, _ = st.columns([0.08, 0.08, 0.99])
if col1.button("▶️ Play" if not st.session_state.auto_run else "⏸ Pause"):
    st.session_state.auto_run = not st.session_state.auto_run

if col2.button("🔄 Reset"):
    st.session_state.step = 0
    st.session_state.auto_run = False
    st.rerun    ()


selected_mass = st.selectbox("Stellar Mass", list(tracks.keys()))
track = tracks[selected_mass]

# --- Animation Control ---
if not st.session_state.auto_run:
    st.session_state.step = st.slider("Time Progression", 0, 100, st.session_state.step)
else:
    # Auto increment the step on each run
    if st.session_state.step < 100:
        st.session_state.step += 1
    else:
        st.session_state.auto_run = False  # Stop once max is reached

# --- Interpolation ---
step_frac = st.session_state.step / 100
try:
    temp_interp, lum_interp, stage = interpolate_stage(track, step_frac)
except Exception as e:
    st.error(f"Error during interpolation: {e}")
    st.stop()

try:
    mass_val = float(selected_mass.split()[0])
except Exception:
    mass_val = 1.0

info = get_stage_details(stage, temp_interp, lum_interp, mass_val)

# --- Display Info ---
st.markdown(f"### Step: {st.session_state.step}/100")
st.markdown(f"### Current Stage: **{info['stage']}**")
with st.expander(f" Details about the {info['stage']} stage"):
    st.markdown(f"**Shell Structure:** {info['structure']}")
    st.markdown(f"**Surface Temperature:** `{info['temperature']}`")
    st.markdown(f"**Luminosity:** `{info['luminosity']}`")
    st.markdown(f"**Estimated Age at this Stage:** `{info['age_estimate']}`")
    st.markdown(f"**Stage Description:** {info['description']}")

# --- Diagrams ---
fig = create_hr_diagram(track["temp"], track["lum"], temp_interp, lum_interp, stage)
col_hr, col_shell = st.columns([3, 2])

with col_hr:
    st.plotly_chart(fig, use_container_width=True, key="hr_chart")

with col_shell:
    shell_fig = shell_structure_figure(stage, step_frac=0.1)
    st.plotly_chart(shell_fig, use_container_width=True, key="shell_structure")

time.sleep(0.2)
# rendering the continuos animation by series of reruns    
st.rerun()
st.stop()