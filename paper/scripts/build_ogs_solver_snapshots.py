#!/usr/bin/env python3
"""Build OGS state snapshot panels for the paper chapter."""

from __future__ import annotations

import argparse
import base64
import lzma
import os
import zlib
from pathlib import Path
from typing import Any

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import meshio
import numpy as np
from meshio.vtu import _vtu


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_VTU = (
    REPO_ROOT
    / "SOTA_OGS_Mont_Terri_work"
    / "inversion_workflow"
    / "runs"
    / "local_basis_sampler_002_basis_024_det_l_0p0075_s_1p000"
    / "ogs_output"
    / "results_cd-a_03_01_ts_0163_t_140000000.000000.vtu"
)
DEFAULT_OUTPUT = REPO_ROOT / "mont_terri_questions_rewrite" / "paper" / "resources" / "figures" / "ogs_solver_snapshots.png"


def patch_meshio_vtu_compressed_appended_reader() -> None:
    """Read OGS 6.5.4 appended-base64 VTUs with bounded DataArray payloads."""

    def read_compressed_binary_bounded(self: Any, data: str | bytes, dtype: np.dtype) -> np.ndarray:
        header_dtype = _vtu.vtu_to_numpy_type[self.header_type]
        if self.byte_order is not None:
            header_dtype = header_dtype.newbyteorder("<" if self.byte_order == "LittleEndian" else ">")
        num_bytes_per_item = np.dtype(header_dtype).itemsize
        num_chars = _vtu.num_bytes_to_num_base64_chars(num_bytes_per_item)
        byte_string = base64.b64decode(data[:num_chars])[:num_bytes_per_item]
        num_blocks = np.frombuffer(byte_string, header_dtype)[0]

        num_header_items = 3 + int(num_blocks)
        num_header_bytes = num_bytes_per_item * num_header_items
        num_header_chars = _vtu.num_bytes_to_num_base64_chars(num_header_bytes)
        byte_string = base64.b64decode(data[:num_header_chars])
        header = np.frombuffer(byte_string, header_dtype)
        block_sizes = header[3:]
        compressed_bytes = int(np.sum(block_sizes))
        compressed_chars = _vtu.num_bytes_to_num_base64_chars(compressed_bytes)
        encoded_payload = data[num_header_chars : num_header_chars + compressed_chars]
        byte_array = base64.b64decode(encoded_payload)[:compressed_bytes]

        if self.byte_order is not None:
            dtype = dtype.newbyteorder("<" if self.byte_order == "LittleEndian" else ">")

        byte_offsets = np.empty(block_sizes.shape[0] + 1, dtype=block_sizes.dtype)
        byte_offsets[0] = 0
        np.cumsum(block_sizes, out=byte_offsets[1:])

        compressor = {"vtkLZMADataCompressor": lzma, "vtkZLibDataCompressor": zlib}[self.compression]
        return np.concatenate(
            [
                np.frombuffer(
                    compressor.decompress(byte_array[byte_offsets[index] : byte_offsets[index + 1]]),
                    dtype=dtype,
                )
                for index in range(int(num_blocks))
            ]
        )

    _vtu.VtuReader.read_compressed_binary = read_compressed_binary_bounded


def triangle_block(mesh: meshio.Mesh) -> np.ndarray:
    for block in mesh.cells:
        if block.type == "triangle6":
            return block.data[:, :3]
        if block.type == "triangle":
            return block.data
    raise ValueError("No triangle or triangle6 cell block found in VTU output.")


def add_panel(ax: plt.Axes, triang: mtri.Triangulation, values: np.ndarray, title: str, label: str, cmap: str) -> None:
    pc = ax.tripcolor(triang, values, shading="gouraud", cmap=cmap)
    ax.set_title(title, fontsize=11)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.tick_params(labelsize=8)
    cb = plt.colorbar(pc, ax=ax, fraction=0.046, pad=0.02)
    cb.set_label(label, fontsize=9)
    cb.ax.tick_params(labelsize=8)


def build_snapshot(vtu_path: Path, output_path: Path) -> None:
    patch_meshio_vtu_compressed_appended_reader()
    mesh = meshio.read(vtu_path)
    points = mesh.points[:, :2]
    triangles = triangle_block(mesh)
    triang = mtri.Triangulation(points[:, 0], points[:, 1], triangles)

    pressure_mpa = np.asarray(mesh.point_data["pressure"], dtype=float) / 1.0e6
    saturation = np.asarray(mesh.point_data["saturation"], dtype=float)
    displacement = np.asarray(mesh.point_data["displacement"], dtype=float)
    displacement_mm = np.linalg.norm(displacement, axis=1) * 1.0e3

    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2), constrained_layout=True)
    add_panel(axes[0], triang, pressure_mpa, "Liquid pressure", r"$p_l$ [MPa]", "coolwarm")
    add_panel(axes[1], triang, saturation, "Liquid saturation", r"$S_l$ [-]", "viridis")
    add_panel(axes[2], triang, displacement_mm, "Displacement magnitude", r"$\|\mathbf{u}\|$ [mm]", "magma")
    fig.suptitle("OGS final-state snapshots, current permeability-field run, t = 140000000 s", fontsize=12)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=220)
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vtu", type=Path, default=DEFAULT_VTU)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_snapshot(args.vtu, args.output)
    print(args.output)


if __name__ == "__main__":
    main()
