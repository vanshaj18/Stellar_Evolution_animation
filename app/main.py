import streamlit as st
import time
from shell_strcture import shell_structure_figure, shell_structure_figure_3d
from data import tracks
from stages import interpolate_stage, get_stage_details
from plot import create_hr_diagram

st.set_page_config(page_title="HR Diagram Animator", layout="wide")
st.markdown("""
<h1 style='text-align: center;'>🌠 Stellar Evolution Explorer 🌠</h1>
<p style='text-align: center;'>Visualize a star’s journey from birth to its spectacular end</p>
""", unsafe_allow_html=True)


# --- Session State Initialization ---
if "auto_run" not in st.session_state:
    st.session_state.auto_run = False
if "step" not in st.session_state:
    st.session_state.step = 0

# ----- define the steps ------
steps = 500

# --- UI Controls ---
with st.sidebar:
    st.title("Controls")
    if st.button("▶️ Play" if not st.session_state.auto_run else "⏸ Pause"):
        st.session_state.auto_run = not st.session_state.auto_run

    if st.button("🔁 Reset"):
        st.session_state.step = 0
        st.session_state.auto_run = False

    selected_mass = st.selectbox("Stellar Mass", list(tracks.keys()))

# ---------- adding lum and temp in session state ---------
if "path_temp" not in st.session_state:
    st.session_state.path_temp = []
if "path_lum" not in st.session_state:
    st.session_state.path_lum = []


# col1, col2, _ = st.columns([0.08, 0.08, 0.99])
# if col1.button("▶️ Play" if not st.session_state.auto_run else "⏸ Pause"):
#     st.session_state.auto_run = not st.session_state.auto_run

# if col2.button("🔄 Reset"):
#     st.session_state.step = 0
#     st.session_state.auto_run = False
#     st.rerun    ()


# selected_mass = st.selectbox("Stellar Mass", list(tracks.keys()))
track = tracks[selected_mass]

# --- Animation Control ---
if not st.session_state.auto_run:
    # st.session_state.step = st.slider("Time Progression", 0, 100, st.session_state.step)
    st.progress(st.session_state.step / steps)

else:
    # Auto increment the step on each run
    if st.session_state.step < steps:
        st.session_state.step += 1
    else:
        st.session_state.auto_run = False  # Stop once max is reached

# --- Interpolation ---
step_frac = st.session_state.step / steps
try:
    temp_interp, lum_interp, stage = interpolate_stage(track, step_frac)
except Exception as e:
    st.error(f"Error during interpolation: {e}")
    st.stop()

try:
    mass_val = float(selected_mass.split()[0])
except Exception:
    mass_val = 1.0

# Append only if new point
if (len(st.session_state.path_temp) == 0 or 
    temp_interp != st.session_state.path_temp[-1] or 
    lum_interp != st.session_state.path_lum[-1]):
    
    st.session_state.path_temp.append(temp_interp)
    st.session_state.path_lum.append(lum_interp)


info = get_stage_details(stage, temp_interp, lum_interp, mass_val)

# --- Display Info ---
# st.markdown(f"### Step: {st.session_state.step}/100")
st.markdown(f"### Current Stage: **{info['stage']}**")
with st.expander(f" Details about the {info['stage']} stage"):
    st.markdown(f"**Shell Structure:** {info['structure']}")
    st.markdown(f"**Surface Temperature:** `{info['temperature']}`")
    st.markdown(f"**Luminosity:** `{info['luminosity']}`")
    st.markdown(f"**Estimated Age at this Stage:** `{info['age_estimate']}`")
    st.markdown(f"**Stage Description:** {info['description']}")

# --- Diagrams ---
fig = create_hr_diagram(track["temp"], track["lum"], temp_interp, lum_interp, stage)


# tab1, tab2, tab3 = st.tabs(["📈 HR Diagram", "🌀 Shell Structure", "📘 Stage Details"])

# with tab1:
#     st.plotly_chart(fig, use_container_width=True)

# with tab2:
#     st.plotly_chart(shell_fig, use_container_width=True)

# with tab3:
#     st.markdown(f"### Step: {st.session_state.step}/100")
#     st.markdown(f"### Current Stage: **{info['stage']}**")
    # rest of the stage info here...


col_hr, col_shell = st.columns([3, 2])

with col_hr:
    st.plotly_chart(fig, use_container_width=True, key="hr_chart")

with col_shell:
    shell_fig = shell_structure_figure_3d(stage)
    st.plotly_chart(shell_fig, use_container_width=True, key="shell_structure")

time.sleep(0.2)
# rendering the continuos animation by series of reruns    
st.rerun()
st.stop()