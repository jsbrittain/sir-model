# SIR Epidemic Simulator

A starter project for the Oxford Research Software Engineering course on AI-assisted software development.

## Getting started

This repository contains a specification and instructions for developing a small SIR epidemic simulator using an AI coding agent.

The repository includes a command-line simulator and interactive dashboard.

1. Create your own repository using **Use this template**.
2. Open your new repository in GitHub Codespaces.
3. Read `DESIGN.md` and `AGENTS.md`.
4. Follow the course practicals to implement and extend the simulator.

## Running the dashboard

Install the application dependency:

```bash
python -m pip install -r requirements.txt
```

Start the interactive SIR simulator dashboard:

```bash
streamlit run app.py
```

Use the sidebar to adjust the population, initial infected population,
transmission and recovery parameters, initial vaccination proportion, and
simulation duration. The chart shows susceptible, infected, and recovered
populations over time.

## Repository contents

- `DESIGN.md` — application requirements and scientific assumptions.
- `AGENTS.md` — instructions and boundaries for AI coding agents.
- `app.py` — Streamlit dashboard for the SIR simulator.
- `docker/` — files used in the environments practical.

## Course progression

During the course, you will:

1. Implement a command-line SIR simulator.
2. Explore dependency management and containers.
3. Introduce automated testing and vaccination.
4. Record your changes using Git.
5. Configure GitHub Actions.
6. Delegate a Streamlit dashboard and review its pull request.

## Important

This is an educational example, not a validated epidemiological forecasting tool.

The repository will evolve as you complete the practicals.

