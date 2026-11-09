"""Deterministic SIR epidemic simulator.

This educational model assumes a closed, homogeneously mixing population with
constant transmission and recovery parameters. Optional initial vaccination
is modelled; other interventions are not. This is not intended for real-world
forecasting.
"""

import argparse
import math
from numbers import Real


def _validate_number(name, value):
    if (
        isinstance(value, bool)
        or not isinstance(value, Real)
        or not math.isfinite(value)
    ):
        raise ValueError(f"{name} must be a finite number")


def simulate_sir(population, infected, beta, gamma, days, vaccination=0.0):
    """Return daily compartment histories after optional initial vaccination."""
    for name, value in (
        ("population", population),
        ("infected", infected),
        ("beta", beta),
        ("gamma", gamma),
        ("vaccination", vaccination),
    ):
        _validate_number(name, value)

    if population <= 0:
        raise ValueError("population must be positive")
    if not 0 <= infected <= population:
        raise ValueError("infected must be between 0 and population")
    if not 0 <= beta <= 1:
        raise ValueError("beta must be between 0 and 1")
    if not 0 <= gamma <= 1:
        raise ValueError("gamma must be between 0 and 1")
    if not 0 <= vaccination <= 1:
        raise ValueError("vaccination must be between 0 and 1")
    if isinstance(days, bool) or not isinstance(days, int) or days < 0:
        raise ValueError("days must be a non-negative integer")

    initially_susceptible = population - infected
    vaccinated = vaccination * initially_susceptible

    susceptible = [initially_susceptible - vaccinated]
    infected_history = [infected]
    recovered = [vaccinated]

    for _ in range(days):
        current_susceptible = susceptible[-1]
        current_infected = infected_history[-1]
        current_recovered = recovered[-1]

        new_infections = beta * current_susceptible * current_infected / population
        new_recoveries = gamma * current_infected

        susceptible.append(current_susceptible - new_infections)
        infected_history.append(current_infected + new_infections - new_recoveries)
        recovered.append(current_recovered + new_recoveries)

    return susceptible, infected_history, recovered


def main():
    parser = argparse.ArgumentParser(
        description="Simulate a deterministic SIR epidemic."
    )
    parser.add_argument("--population", type=float, default=1000)
    parser.add_argument("--infected", type=float, default=10)
    parser.add_argument("--beta", type=float, default=0.3)
    parser.add_argument("--gamma", type=float, default=0.1)
    parser.add_argument("--days", type=int, default=100)
    args = parser.parse_args()

    try:
        susceptible, infected, recovered = simulate_sir(
            args.population, args.infected, args.beta, args.gamma, args.days
        )
    except ValueError as error:
        parser.error(str(error))

    peak_day = max(range(len(infected)), key=infected.__getitem__)
    print("Simulation parameters:")
    print(f"  Population: {args.population:g}")
    print(f"  Initial infected: {args.infected:g}")
    print(f"  Beta: {args.beta:g}")
    print(f"  Gamma: {args.gamma:g}")
    print(f"  Days: {args.days}")
    print(f"Peak infected population: {infected[peak_day]:.6f} on day {peak_day}")
    print("Final populations:")
    print(f"  Susceptible: {susceptible[-1]:.6f}")
    print(f"  Infected: {infected[-1]:.6f}")
    print(f"  Recovered: {recovered[-1]:.6f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
