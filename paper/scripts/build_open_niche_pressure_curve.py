#!/usr/bin/env python3
"""Build the active open-niche pressure boundary curve figure."""

from __future__ import annotations

import argparse
import os
import xml.etree.ElementTree as ET
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CURVE = (
    REPO_ROOT
    / "mont_terri_questions_rewrite"
    / "literature"
    / "local_sources"
    / "GesaProjectionModel2025"
    / "08_08_open_niche_seasonal.xml"
)
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "mont_terri_questions_rewrite"
    / "paper"
    / "resources"
    / "figures"
    / "open_niche_pressure_curve.png"
)
SECONDS_PER_YEAR = 365.25 * 24 * 3600


def read_curve(path: Path) -> tuple[np.ndarray, np.ndarray]:
    root = ET.fromstring(f"<root>{path.read_text()}</root>")
    coords_text = root.findtext("coords")
    values_text = root.findtext("values")
    if coords_text is None or values_text is None:
        raise ValueError(f"Curve file {path} must contain coords and values tags.")

    time_s = np.array([float(value) for value in coords_text.split()], dtype=float)
    pressure_pa = np.array([float(value) for value in values_text.split()], dtype=float)
    if time_s.shape != pressure_pa.shape:
        raise ValueError(f"Curve file {path} has mismatched coordinate and value counts.")
    return time_s, pressure_pa


def build_figure(curve_path: Path, output_path: Path) -> None:
    time_s, pressure_pa = read_curve(curve_path)
    time_years = time_s / SECONDS_PER_YEAR
    pressure_mpa = pressure_pa / 1.0e6
    suction_mpa = -pressure_mpa

    fig, ax = plt.subplots(figsize=(7.0, 3.0), constrained_layout=True)
    ax.plot(
        time_years,
        pressure_mpa,
        color="#1f6f8b",
        linewidth=1.15,
        marker="o",
        markersize=1.8,
        markerfacecolor="#0f3f52",
        markeredgewidth=0,
        label=r"tabulated $p_E(t)$ values",
    )
    ax.axhline(0.0, color="0.35", linewidth=0.8)
    ax.axhline(1.5, color="#a83232", linestyle="--", linewidth=1.0, label=r"$p_{\mathrm{square}}=1.5$ MPa")

    ax.set_xlabel("Model time since t=0 [years]", fontsize=10)
    ax.set_ylabel(r"Open-niche liquid pressure $p_E(t)$ [MPa]", fontsize=10)
    ax.set_xlim(float(time_years.min()), float(time_years.max()))
    ax.set_ylim(min(float(pressure_mpa.min()) - 2.0, -55.0), 3.0)
    ax.grid(True, which="major", color="0.88", linewidth=0.8)
    ax.tick_params(labelsize=8.5)
    ax.legend(loc="lower right", frameon=False, fontsize=8)

    ax_suction = ax.secondary_yaxis("right", functions=(lambda y: -y, lambda y: -y))
    ax_suction.set_ylabel(r"Equivalent suction $p_c=-p_E(t)$ [MPa]", fontsize=10)
    ax_suction.tick_params(labelsize=8.5)

    stats = (
        f"{len(time_s)} points, "
        f"{time_years.max():.2f} years, "
        f"$p_E$ range {pressure_mpa.min():.2f} to {pressure_mpa.max():.2f} MPa"
    )
    ax.text(
        0.014,
        0.075,
        stats,
        transform=ax.transAxes,
        fontsize=7.5,
        color="0.25",
        bbox={"facecolor": "white", "edgecolor": "0.75", "boxstyle": "round,pad=0.25", "alpha": 0.9},
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=240)
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--curve", type=Path, default=DEFAULT_CURVE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_figure(args.curve, args.output)
    print(args.output)


if __name__ == "__main__":
    main()
