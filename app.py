"""Streamlit dashboard for exploring the SIR epidemic simulator."""

import streamlit as st

from sir import simulate_sir

st.set_page_config(page_title="SIR Simulator", page_icon=":chart_with_upwards_trend:")
st.title("SIR Epidemic Simulator")
st.caption(
    "An educational model of a closed, homogeneously mixing population. "
    "It is not a real-world forecasting tool."
)

with st.sidebar:
    st.header("Simulation parameters")
    population = st.number_input("Population", min_value=1.0, value=1000.0, step=100.0)
    infected = st.number_input(
        "Initial infected",
        min_value=0.0,
        max_value=population,
        value=min(10.0, population),
        step=1.0,
    )
    beta = st.slider("Daily transmission parameter (beta)", 0.0, 1.0, 0.3)
    gamma = st.slider("Daily recovery parameter (gamma)", 0.0, 1.0, 0.1)
    vaccination = st.slider("Initially vaccinated proportion", 0.0, 1.0, 0.0)
    days = st.number_input("Simulation days", min_value=0, value=100, step=1)

try:
    susceptible, infected_history, recovered = simulate_sir(
        population=population,
        infected=infected,
        beta=beta,
        gamma=gamma,
        days=days,
        vaccination=vaccination,
    )
except ValueError as error:
    st.error(str(error))
else:
    st.line_chart(
        {
            "Day": range(days + 1),
            "Susceptible": susceptible,
            "Infected": infected_history,
            "Recovered": recovered,
        },
        x="Day",
        y=["Susceptible", "Infected", "Recovered"],
    )

    peak_day = max(range(len(infected_history)), key=infected_history.__getitem__)
    st.metric("Peak infected population", f"{infected_history[peak_day]:.1f}")
    st.caption(f"Peak occurs on day {peak_day}.")
