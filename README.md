# DC Circuit Solver Using Mesh Analysis

Course End Project for `A9205 - Basic Electrical Engineering Laboratory (VCE-R25)`.

This project is a console-based Python program that solves DC circuits using the mesh analysis method. It forms the mesh equations from the given circuit data, solves the unknown mesh currents numerically, verifies the result using Kirchhoff's Voltage Law (KVL), and generates graphs for report submission.

## Group Members

- ANIRUDH UPADHYAY  Roll No: `25881A05Y7`
- MAMIDIPALLY HANSIKA  Roll No: `25881A05Z6`
- AMATHUL LUBNA  Roll No: `25881A05AH`

## Problem Description

The aim of this project is to develop a programming-based analytical model for solving DC circuits using mesh analysis.

The program:

- accepts self-resistance values for each mesh
- accepts shared resistance values between meshes
- accepts source voltages for each mesh
- forms the mesh resistance matrix
- solves the mesh currents using Gaussian elimination
- displays shared-branch currents
- verifies the result using KVL
- generates graph images in the `screenshots/` folder

## Theoretical Background

Mesh analysis is a systematic method used to determine currents in planar DC circuits. A mesh current is assumed in each loop, usually in the clockwise direction. Using Kirchhoff's Voltage Law, the algebraic sum of voltage drops and voltage sources around a closed loop is zero.

For a circuit with multiple meshes:

- the diagonal term of the matrix is the total resistance in that mesh
- the off-diagonal term is the negative of the resistance shared between two meshes

## Mathematical Formulation

The mesh equations are written in matrix form as:

```text
[R][I] = [V]
```

Where:

- `[R]` is the mesh resistance matrix
- `[I]` is the mesh current vector
- `[V]` is the source voltage vector

For each mesh:

```text
Rii = total resistance in mesh i
Rij = - shared resistance between mesh i and mesh j
```

Example for a two-mesh circuit:

```text
R11*I1 - R12*I2 = V1
-R21*I1 + R22*I2 = V2
```

## Input And Output Format

### Input

The program supports two modes:

1. Built-in sample circuit
2. Manual input mode

Manual input requires:

- number of meshes
- self resistance of each mesh in ohms
- shared resistance between meshes in ohms
- source voltage of each mesh in volts

### Output

The program displays:

- generated mesh equations
- calculated mesh currents in amperes
- current through shared branches
- KVL verification values
- graph files with proper labels and grid
- result summary

## Repository Structure

```text
project-root/
|-- src/
|   |-- dc_mesh_analysis_solver.py
|-- report/
|   |-- FINAL_REPORT.md
|-- screenshots/
|   |-- .gitkeep
|   |-- mesh_currents_bar_graph.png
|   `-- mesh1_current_vs_voltage.png
|-- README.md
`-- requirements.txt
```

## How To Run The Program

Make sure Python 3 is installed, then run:

```bash
pip install -r requirements.txt
python src/dc_mesh_analysis_solver.py
```

On Windows PowerShell:

```powershell
pip install -r requirements.txt
python src\dc_mesh_analysis_solver.py
```

## Sample Input

Using the built-in sample circuit:

```text
Enter your choice (1 or 2): 1
```

Sample circuit used by the program:

- Self resistances: `6 ohms`, `8 ohms`
- Shared resistance: `2 ohms`
- Source voltages: `10 V`, `5 V`

## Sample Output

```text
Mesh equations formed from the input data:
Mesh 1: 6.000 * I1 -2.000 * I2 = 10.000 V
Mesh 2: -2.000 * I1 +8.000 * I2 = 5.000 V

Calculated mesh currents:
I1 = 2.0455 A (clockwise)
I2 = 1.1364 A (clockwise)

Current through shared branches:
Between Mesh 1 and Mesh 2: 0.9091 A
```

## Validation

The program verifies the result using KVL after solving the equations. For the built-in sample case:

- Mesh 1 left side = `10.0000 V`
- Mesh 2 left side = `5.0000 V`
- numerical error is approximately zero

## Files Required By CEP

According to `A9205_BEE_Course_End_Project`, the repository should include:

- `src/` for source code
- `report/` for the final report PDF
- `screenshots/` for output screenshots
- `README.md` with project details
- `requirements.txt` for Python projects

This repository now includes all of those basic items.

## Graphs Included

The program generates the following graph files in `screenshots/`:

- `mesh_currents_bar_graph.png`
- `mesh1_current_vs_voltage.png`

## What You Should Add Before Submission

- add screenshots of program output in `screenshots/` if your faculty wants terminal captures in addition to graphs
- convert `report/FINAL_REPORT.md` into a final PDF and place it in `report/`
- create the GitHub repository with the required name format such as `BEE_CEP_2026_Group07`

## References

- Basic Electrical Engineering textbook prescribed for your course
- Class notes on mesh analysis and Kirchhoff's Voltage Law
