"""
Course End Project
Title: DC Circuit Solver Using Mesh Analysis

This console-based program solves DC circuits using the mesh-current method.
It follows the Course End Project requirement of using a programming-based
analytical model with input validation, clear units, and structured output.

Mathematical model:
    [R][I] = [V]

Where:
    R = mesh resistance matrix
    I = unknown mesh-current vector
    V = source-voltage vector

For each mesh:
    Rii = total resistance in mesh i
    Rij = - shared resistance between mesh i and mesh j
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

EPSILON = 1e-10
OUTPUT_DIRECTORY = Path(__file__).resolve().parent.parent / "screenshots"


def read_int(prompt: str, minimum: int = 1) -> int:
    """Read an integer that is at least `minimum`."""
    while True:
        raw_value = input(prompt).strip()
        try:
            number = int(raw_value)
            if number < minimum:
                print(f"Enter an integer greater than or equal to {minimum}.")
                continue
            return number
        except ValueError:
            print("Invalid input. Enter a whole number.")


def read_float(prompt: str, minimum: float | None = None) -> float:
    """Read a floating-point value with an optional lower bound."""
    while True:
        raw_value = input(prompt).strip()
        try:
            number = float(raw_value)
            if minimum is not None and number < minimum:
                print(f"Enter a value greater than or equal to {minimum}.")
                continue
            return number
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def solve_linear_system(matrix: list[list[float]], constants: list[float]) -> list[float]:
    """Solve a linear system by Gaussian elimination with partial pivoting."""
    size = len(matrix)
    augmented = [row[:] + [constants[index]] for index, row in enumerate(matrix)]

    for pivot_column in range(size):
        pivot_row = max(
            range(pivot_column, size),
            key=lambda row_index: abs(augmented[row_index][pivot_column]),
        )

        if abs(augmented[pivot_row][pivot_column]) < EPSILON:
            raise ValueError(
                "The circuit equations are singular. "
                "Check the resistance data and shared branches."
            )

        if pivot_row != pivot_column:
            augmented[pivot_column], augmented[pivot_row] = (
                augmented[pivot_row],
                augmented[pivot_column],
            )

        pivot_value = augmented[pivot_column][pivot_column]
        for row_index in range(pivot_column + 1, size):
            factor = augmented[row_index][pivot_column] / pivot_value
            for column_index in range(pivot_column, size + 1):
                augmented[row_index][column_index] -= (
                    factor * augmented[pivot_column][column_index]
                )

    solution = [0.0] * size
    for row_index in range(size - 1, -1, -1):
        rhs_value = augmented[row_index][size]
        for column_index in range(row_index + 1, size):
            rhs_value -= augmented[row_index][column_index] * solution[column_index]
        solution[row_index] = rhs_value / augmented[row_index][row_index]

    return solution


def build_matrix(
    self_resistances: list[float], shared_resistances: list[list[float]]
) -> list[list[float]]:
    """Build the mesh resistance matrix."""
    size = len(self_resistances)
    matrix = [[0.0] * size for _ in range(size)]

    for row in range(size):
        for column in range(size):
            if row == column:
                matrix[row][column] = self_resistances[row]
            else:
                matrix[row][column] = -shared_resistances[row][column]

    return matrix


def print_equations(matrix: list[list[float]], voltages: list[float]) -> None:
    """Display the mesh equations in readable form."""
    print("\nMesh equations formed from the input data:")
    for row_index, row in enumerate(matrix):
        terms = []
        for column_index, coefficient in enumerate(row):
            if abs(coefficient) < EPSILON:
                continue
            terms.append(f"{coefficient:+.3f} * I{column_index + 1}")
        equation = " ".join(terms).lstrip("+")
        print(f"Mesh {row_index + 1}: {equation} = {voltages[row_index]:.3f} V")


def print_shared_branch_currents(
    mesh_currents: list[float], shared_resistances: list[list[float]]
) -> None:
    """Show current through shared branches, when they exist."""
    print("\nCurrent through shared branches:")
    found_shared_branch = False

    for first_mesh in range(len(mesh_currents)):
        for second_mesh in range(first_mesh + 1, len(mesh_currents)):
            if shared_resistances[first_mesh][second_mesh] > EPSILON:
                branch_current = mesh_currents[first_mesh] - mesh_currents[second_mesh]
                print(
                    f"Between Mesh {first_mesh + 1} and Mesh {second_mesh + 1}: "
                    f"{branch_current:.4f} A "
                    f"(positive from Mesh {first_mesh + 1} to Mesh {second_mesh + 1})"
                )
                found_shared_branch = True

    if not found_shared_branch:
        print("No shared resistors were entered.")


def verify_kvl(
    matrix: list[list[float]], mesh_currents: list[float], voltages: list[float]
) -> None:
    """Check the solution against the original equations."""
    print("\nKVL verification:")
    for row_index, row in enumerate(matrix):
        lhs_value = sum(
            row[column_index] * mesh_currents[column_index]
            for column_index in range(len(mesh_currents))
        )
        error = lhs_value - voltages[row_index]
        print(
            f"Mesh {row_index + 1}: Left side = {lhs_value:.4f} V, "
            f"Right side = {voltages[row_index]:.4f} V, "
            f"Error = {error:.6f}"
        )


def solve_mesh_currents_for_sources(
    self_resistances: list[float],
    shared_resistances: list[list[float]],
    voltages: list[float],
) -> list[float]:
    """Solve mesh currents for the given source voltages."""
    resistance_matrix = build_matrix(self_resistances, shared_resistances)
    return solve_linear_system(resistance_matrix, voltages)


def generate_graphs(
    self_resistances: list[float],
    shared_resistances: list[list[float]],
    base_voltages: list[float],
    mesh_currents: list[float],
) -> list[Path]:
    """Generate graphs required for the project report."""
    OUTPUT_DIRECTORY.mkdir(parents=True, exist_ok=True)
    graph_paths: list[Path] = []

    mesh_labels = [f"Mesh {index + 1}" for index in range(len(mesh_currents))]
    plt.figure(figsize=(8, 5))
    plt.bar(mesh_labels, mesh_currents, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
    plt.title("Mesh Currents for the Given DC Circuit")
    plt.xlabel("Mesh")
    plt.ylabel("Current (A)")
    plt.grid(True, axis="y", linestyle="--", alpha=0.5)
    current_graph = OUTPUT_DIRECTORY / "mesh_currents_bar_graph.png"
    plt.tight_layout()
    plt.savefig(current_graph, dpi=200)
    plt.close()
    graph_paths.append(current_graph)

    if base_voltages:
        voltage_values = list(range(2, 22, 2))
        varied_currents = []
        for voltage in voltage_values:
            varied_source_vector = base_voltages[:]
            varied_source_vector[0] = float(voltage)
            solved_currents = solve_mesh_currents_for_sources(
                self_resistances,
                shared_resistances,
                varied_source_vector,
            )
            varied_currents.append(solved_currents[0])

        plt.figure(figsize=(8, 5))
        plt.plot(
            voltage_values,
            varied_currents,
            marker="o",
            linewidth=2,
            color="#2ca02c",
        )
        plt.title("Variation of Mesh 1 Current with Source Voltage")
        plt.xlabel("Source Voltage V1 (V)")
        plt.ylabel("Mesh 1 Current I1 (A)")
        plt.grid(True, linestyle="--", alpha=0.5)
        variation_graph = OUTPUT_DIRECTORY / "mesh1_current_vs_voltage.png"
        plt.tight_layout()
        plt.savefig(variation_graph, dpi=200)
        plt.close()
        graph_paths.append(variation_graph)

    return graph_paths


def get_sample_data() -> tuple[list[float], list[list[float]], list[float]]:
    """Return a small validated example circuit."""
    self_resistances = [6.0, 8.0]
    shared_resistances = [
        [0.0, 2.0],
        [2.0, 0.0],
    ]
    voltages = [10.0, 5.0]
    return self_resistances, shared_resistances, voltages


def get_manual_input() -> tuple[list[float], list[list[float]], list[float]]:
    """Collect mesh-analysis data from the user."""
    mesh_count = read_int("Enter the number of meshes: ", minimum=1)

    print(
        "\nEnter the self resistance of each mesh."
        "\nSelf resistance means the total resistance in that mesh, in ohms."
    )
    self_resistances = [
        read_float(f"Self resistance R{mesh_index + 1}{mesh_index + 1} (ohms): ", minimum=0.0)
        for mesh_index in range(mesh_count)
    ]

    shared_resistances = [[0.0] * mesh_count for _ in range(mesh_count)]
    if mesh_count > 1:
        print(
            "\nEnter the shared resistance between meshes."
            "\nIf two meshes do not share a resistor, enter 0."
        )
        for first_mesh in range(mesh_count):
            for second_mesh in range(first_mesh + 1, mesh_count):
                value = read_float(
                    f"Shared resistance between Mesh {first_mesh + 1} and "
                    f"Mesh {second_mesh + 1} (ohms): ",
                    minimum=0.0,
                )
                shared_resistances[first_mesh][second_mesh] = value
                shared_resistances[second_mesh][first_mesh] = value

    print(
        "\nEnter the algebraic sum of voltage sources for each mesh."
        "\nUse positive value if the source aids the clockwise mesh current,"
        "\nand negative value if it opposes the clockwise mesh current."
    )
    voltages = [
        read_float(f"Source voltage for Mesh {mesh_index + 1} (volts): ")
        for mesh_index in range(mesh_count)
    ]

    return self_resistances, shared_resistances, voltages


def main() -> None:
    print("=" * 68)
    print("DC CIRCUIT SOLVER USING MESH ANALYSIS")
    print("=" * 68)
    print("All mesh currents are assumed clockwise.")
    print("Units: resistance in ohms, voltage in volts, current in amperes.")

    print("\nChoose input mode:")
    print("1. Use built-in sample circuit")
    print("2. Enter circuit data manually")
    choice = read_int("Enter your choice (1 or 2): ", minimum=1)
    while choice not in (1, 2):
        print("Choose 1 for sample input or 2 for manual input.")
        choice = read_int("Enter your choice (1 or 2): ", minimum=1)

    if choice == 1:
        self_resistances, shared_resistances, voltages = get_sample_data()
        print("\nUsing sample circuit:")
        print("Self resistances: 6 ohms, 8 ohms")
        print("Shared resistance between Mesh 1 and Mesh 2: 2 ohms")
        print("Source voltages: 10 V, 5 V")
    else:
        self_resistances, shared_resistances, voltages = get_manual_input()

    resistance_matrix = build_matrix(self_resistances, shared_resistances)
    print_equations(resistance_matrix, voltages)

    try:
        mesh_currents = solve_linear_system(resistance_matrix, voltages)
    except ValueError as error:
        print(f"\nUnable to solve the circuit: {error}")
        return

    print("\nCalculated mesh currents:")
    for index, current in enumerate(mesh_currents, start=1):
        direction = "clockwise" if current >= 0 else "opposite to clockwise"
        print(f"I{index} = {current:.4f} A ({direction})")

    print_shared_branch_currents(mesh_currents, shared_resistances)
    verify_kvl(resistance_matrix, mesh_currents, voltages)

    print("\nResult summary:")
    print("The program successfully formed the mesh equations and solved the DC circuit.")
    print("Use these values in your report under sample input, output, and analysis.")

    try:
        graph_paths = generate_graphs(
            self_resistances,
            shared_resistances,
            voltages,
            mesh_currents,
        )
        print("\nGraphs generated successfully:")
        for graph_path in graph_paths:
            print(f"- {graph_path}")
    except Exception as error:
        print(f"\nGraph generation skipped: {error}")
        print("Install matplotlib correctly if you want graph images for the report.")


if __name__ == "__main__":
    main()
