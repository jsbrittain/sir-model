
# SIR Epidemic Simulator — Design Specification

## Purpose

Develop a small Python application that simulates the spread of an infectious disease through a population using a deterministic SIR model.

The application should allow researchers to explore how transmission and recovery parameters affect the progression of an epidemic.

This is a simplified educational model, not a tool for predicting real epidemics.

## Model

The population is divided into three compartments:

- **S** — Susceptible
- **I** — Infected
- **R** — Recovered (or removed)

Assume a closed population of constant size:

N = S + I + R

Use discrete daily time steps with the following rules:

```text
new_infections = beta * S * I / N
new_recoveries = gamma * I

S_next = S - new_infections
I_next = I + new_infections - new_recoveries
R_next = R + new_recoveries
```

Where:

- `beta` is the daily transmission parameter.
- `gamma` is the daily recovery parameter.
- `N` is the total population.

All three compartments must be updated using values from the same preceding day.

Compartment populations may contain fractional values.

## Functional requirements

Implement the application in a single file, `sir.py`.

Provide a function:

```python
simulate_sir(population, infected, beta, gamma, days)
```

The function must:

- Initialise S = population - infected, I = infected, R = 0.
- Simulate the requested number of daily updates.
- Return three lists `(S, I, R)` containing the daily compartment values, including day 0.
- Preserve the total population, subject to floating-point precision.
- Validate inputs and report invalid parameters clearly.

Parameter constraints:

- `population` must be positive.
- `infected` must be between 0 and population.
- `beta` and `gamma` must be between 0 and 1.
- `days` must be a non-negative integer.

## Command-line interface

Allow users to configure the simulation using:

- `--population`
- `--infected`
- `--beta`
- `--gamma`
- `--days`

Provide sensible defaults.

After running the simulation, display:

- The simulation parameters.
- The peak infected population and the day it occurs.
- The final susceptible, infected and recovered populations.

For example:

```bash
python sir.py --population 1000 --infected 10 \
  --beta 0.3 --gamma 0.1 --days 100
```

## Constraints

These constraints define the initial implementation. Later exercises may explicitly authorise extensions to the application.

- Use Python 3.12.
- Prefer the Python standard library.
- Keep the implementation small and understandable.
- Avoid unnecessary abstractions or dependencies.
- Do not implement a graphical interface.
- Do not add vaccination or other interventions.
- Do not add automated tests at this stage.

## Model assumptions

- The population is closed, with no births, deaths or migration.
- Individuals mix homogeneously.
- Transmission and recovery parameters remain constant.
- Recovered individuals do not become susceptible again.
- Vaccination and other interventions are not modelled.
- The model represents expected compartment sizes rather than individual people.

These assumptions should be documented and not silently changed during implementation.

