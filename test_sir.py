import subprocess
import sys
from pathlib import Path

import pytest

from sir import simulate_sir


def _run_cli(*arguments):
    script = Path(__file__).with_name("sir.py")
    return subprocess.run(
        [sys.executable, str(script), *arguments],
        capture_output=True,
        text=True,
        check=False,
    )


def test_population_conservation():
    S, I, R = simulate_sir(1000, 10, 0.3, 0.1, 100)

    for s, i, r in zip(S, I, R):
        assert s + i + r == pytest.approx(1000)


def test_initial_vaccination():
    S, I, R = simulate_sir(
        population=1000,
        infected=10,
        beta=0.3,
        gamma=0.1,
        days=0,
        vaccination=0.2,
    )

    assert S[0] == pytest.approx(792)
    assert I[0] == pytest.approx(10)
    assert R[0] == pytest.approx(198)


def test_cli_defaults_and_summary():
    result = _run_cli()

    assert result.returncode == 0
    assert result.stderr == ""
    assert result.stdout == (
        "Simulation parameters:\n"
        "  Population: 1000\n"
        "  Initial infected: 10\n"
        "  Beta: 0.3\n"
        "  Gamma: 0.1\n"
        "  Days: 100\n"
        "Peak infected population: 315.935725 on day 28\n"
        "Final populations:\n"
        "  Susceptible: 52.822673\n"
        "  Infected: 1.214010\n"
        "  Recovered: 945.963317\n"
    )


def test_cli_accepts_simulation_options():
    result = _run_cli(
        "--population",
        "100",
        "--infected",
        "2",
        "--beta",
        "0",
        "--gamma",
        "0",
        "--days",
        "0",
    )

    assert result.returncode == 0
    assert result.stderr == ""
    assert result.stdout == (
        "Simulation parameters:\n"
        "  Population: 100\n"
        "  Initial infected: 2\n"
        "  Beta: 0\n"
        "  Gamma: 0\n"
        "  Days: 0\n"
        "Peak infected population: 2.000000 on day 0\n"
        "Final populations:\n"
        "  Susceptible: 98.000000\n"
        "  Infected: 2.000000\n"
        "  Recovered: 0.000000\n"
    )


def test_cli_reports_invalid_parameter():
    result = _run_cli("--beta", "1.1")

    assert result.returncode == 2
    assert result.stdout == ""
    assert result.stderr.endswith("sir.py: error: beta must be between 0 and 1\n")
