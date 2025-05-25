# Stellar Evolution HR Diagram Animator

An interactive and animated Hertzsprung-Russell (HR) diagram built with Streamlit and Plotly to visualize stellar evolution tracks for different stellar masses.

## Features

- Select stellar mass to explore evolutionary tracks.
- Play/Pause animation of star evolution across key stages.
- Interactive slider to manually control time progression.
- Color-coded HR diagram zones (Main Sequence, Giants, White Dwarfs).
- Detailed modals with information about each evolutionary stage:
  - Shell structure
  - Surface temperature
  - Luminosity
  - Estimated stellar age
  - Stage description

## Demo

![Demo GIF or Screenshot here if available]

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/stellar-evolution-hr.git
cd stellar-evolution-hr

python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

streamlit run app.py

stellar_evolution_app/
├── app.py             # Main Streamlit app entry point
├── data.py            # Stellar evolutionary tracks data
├── stages.py          # Functions for interpolation and stage info
├── plot.py            # HR diagram plotting functions
├── info.py            # Stage-specific descriptive info module
├── requirements.txt   # Python dependencies
└── README.md          # This file
