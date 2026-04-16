# COURSE END PROJECT REPORT

## DC Circuit Solver Using Mesh Analysis

### Submitted By

- ANIRUDH UPADHYAY - `25881A05Y7`
- MAMIDIPALLY HANSIKA - `25881A05Z6`
- AMATHUL LUBNA - `25881A05AH`

### Course Details

- Course: `A9205 - Basic Electrical Engineering Laboratory (VCE-R25)`
- Academic Year: `2025-2026`
- Project Type: `Programming-Based Analytical Model`
- Department: `Electrical and Electronics Engineering`

---

## 1. Abstract

This project presents a console-based Python program for solving DC circuits using the mesh analysis method. Mesh analysis is a systematic technique used to determine unknown loop currents in planar electrical networks by applying Kirchhoff's Voltage Law. In this project, the circuit data is represented in matrix form and the unknown mesh currents are computed numerically using Gaussian elimination.

The developed program accepts self-resistance, shared resistance, and source voltage values as input. It automatically forms the mesh equations, solves them, displays the calculated mesh currents, verifies the result using KVL, and generates graphs for visualization. The project demonstrates how electrical engineering theory can be translated into a structured computational model for accurate and efficient circuit analysis.

---

## 2. Introduction

DC circuit analysis is one of the fundamental topics in Basic Electrical Engineering. In practical electrical networks, multiple loops may be present, making direct manual calculation lengthy and error-prone. Mesh analysis provides a systematic and efficient method to solve such circuits by assigning currents to each independent loop and applying Kirchhoff's Voltage Law.

The main objective of this project is to build a programming-based analytical model that solves DC circuits using mesh analysis. Instead of solving the equations manually every time, the program automates the entire process. This improves speed, reduces computational errors, and helps students better understand the relation between circuit theory and algorithm design.

---

## 3. Problem Definition

The problem is to develop a program that can:

- accept the number of meshes in a DC circuit
- accept resistance values of each mesh
- accept shared resistance values between adjacent meshes
- accept source voltages in each mesh
- form the corresponding mesh equations
- solve the equations numerically
- display the unknown mesh currents with proper units
- verify the correctness of the solution using Kirchhoff's Voltage Law

The program must be console-based, easy to use, and suitable for academic demonstration.

---

## 4. Theory Background

### 4.1 Kirchhoff's Voltage Law

Kirchhoff's Voltage Law states that the algebraic sum of all voltages around any closed loop in an electrical circuit is zero.

```text
Sum of voltage rises = Sum of voltage drops
```

In mesh analysis, this law is applied separately to each independent loop.

### 4.2 Mesh Current

A mesh current is a hypothetical current assigned to a loop in a planar circuit. In this project, all mesh currents are assumed to flow in the clockwise direction. If the computed current is positive, the actual current is in the assumed direction. If it is negative, the actual current flows in the opposite direction.

### 4.3 Self Resistance and Shared Resistance

- Self resistance of a mesh is the total resistance present in that mesh.
- Shared resistance is the resistance common to two neighboring meshes.

When mesh equations are written:

- diagonal terms contain self resistance values
- off-diagonal terms contain negative shared resistance values

This leads naturally to matrix representation.

---

## 5. Mathematical Formulation

For an `n` mesh circuit, the mesh equations can be written in matrix form as:

```text
[R][I] = [V]
```

Where:

- `[R]` = resistance matrix
- `[I]` = mesh current vector
- `[V]` = source voltage vector

For each mesh:

```text
Rii = total resistance in mesh i
Rij = - shared resistance between mesh i and mesh j
```

### 5.1 Two-Mesh Example

For a two-mesh circuit:

```text
R11*I1 - R12*I2 = V1
-R21*I1 + R22*I2 = V2
```

This can be represented as:

```text
[ R11   -R12 ] [ I1 ] = [ V1 ]
[ -R21   R22 ] [ I2 ]   [ V2 ]
```

### 5.2 Assumptions

- the circuit is planar
- all mesh currents are assumed clockwise
- the input values are ideal numerical values
- resistance is measured in ohms
- voltage is measured in volts
- current is measured in amperes

---

## 6. Algorithm

### 6.1 Stepwise Algorithm

1. Start the program.
2. Display the project title and unit information.
3. Ask the user to choose sample input mode or manual input mode.
4. Read the number of meshes.
5. Read self-resistance values for each mesh.
6. Read shared resistance values between meshes.
7. Read source voltage values for each mesh.
8. Form the mesh resistance matrix.
9. Display the generated mesh equations.
10. Solve the linear system using Gaussian elimination with partial pivoting.
11. Display the calculated mesh currents.
12. Calculate and display current through shared branches.
13. Verify the result using KVL.
14. Display the result summary.
15. Stop the program.

### 6.2 Flowchart Description

The flow of the program is:

```text
Start
  |
Display title and instructions
  |
Choose sample or manual input
  |
Read circuit data
  |
Form resistance matrix
  |
Solve [R][I] = [V]
  |
Display mesh currents
  |
Verify KVL
  |
Display summary
  |
Stop
```

---

## 7. Program Implementation

The project is implemented in Python as a console-based application. The main features of the implementation are:

- input validation for integer and floating-point values
- automatic construction of resistance matrix
- Gaussian elimination for solving simultaneous equations
- readable display of mesh equations
- KVL verification after solving
- graph generation using matplotlib
- clear output with proper electrical units

### 7.1 Source Code File

The complete program is available in:

- `src/dc_mesh_analysis_solver.py`

### 7.2 Important Functions Used

- `read_int()` for integer input validation
- `read_float()` for numeric input validation
- `build_matrix()` for forming the resistance matrix
- `solve_linear_system()` for Gaussian elimination
- `print_equations()` for displaying mesh equations
- `verify_kvl()` for checking the correctness of the result
- `generate_graphs()` for creating report graphs

---

## 8. Sample Input And Output

### 8.1 Sample Input

The built-in sample circuit used in the program is:

- Self resistance of Mesh 1 = `6 ohms`
- Self resistance of Mesh 2 = `8 ohms`
- Shared resistance between Mesh 1 and Mesh 2 = `2 ohms`
- Source voltage of Mesh 1 = `10 V`
- Source voltage of Mesh 2 = `5 V`

The console input is:

```text
Enter your choice (1 or 2): 1
```

### 8.2 Sample Output

```text
Mesh equations formed from the input data:
Mesh 1: 6.000 * I1 -2.000 * I2 = 10.000 V
Mesh 2: -2.000 * I1 +8.000 * I2 = 5.000 V

Calculated mesh currents:
I1 = 2.0455 A (clockwise)
I2 = 1.1364 A (clockwise)

Current through shared branches:
Between Mesh 1 and Mesh 2: 0.9091 A (positive from Mesh 1 to Mesh 2)

KVL verification:
Mesh 1: Left side = 10.0000 V, Right side = 10.0000 V, Error = 0.000000
Mesh 2: Left side = 5.0000 V, Right side = 5.0000 V, Error = -0.000000
```

### 8.3 Interpretation

The value of `I1 = 2.0455 A` indicates that the current in Mesh 1 flows in the assumed clockwise direction. Similarly, `I2 = 1.1364 A` shows that Mesh 2 current also flows clockwise. The current through the common branch is `0.9091 A`, flowing from Mesh 1 towards Mesh 2.

---

## 9. Graphs

The program generates the following graphs automatically in the `screenshots/` folder.

### 9.1 Bar Graph of Mesh Currents

File name:

- `mesh_currents_bar_graph.png`

Purpose:

- to compare the magnitude of current in each mesh
- to visually show which mesh carries higher current

Graph details:

- title: `Mesh Currents for the Given DC Circuit`
- x-axis: `Mesh`
- y-axis: `Current (A)`
- grid: enabled

### 9.2 Variation of Mesh 1 Current with Source Voltage

File name:

- `mesh1_current_vs_voltage.png`

Purpose:

- to study how Mesh 1 current changes when source voltage `V1` changes
- to demonstrate the linear relation between source voltage and mesh current in a DC resistive circuit

Graph details:

- title: `Variation of Mesh 1 Current with Source Voltage`
- x-axis: `Source Voltage V1 (V)`
- y-axis: `Mesh 1 Current I1 (A)`
- grid: enabled

These graphs satisfy the CEP requirement that graphical output should include a proper title, axis labels with units, and grid.

---

## 10. Result Analysis

The developed program successfully solves DC mesh equations using numerical methods. The computed values are accurate and satisfy the original KVL equations. This confirms the correctness of both the mathematical formulation and the implementation logic.

The project also demonstrates that computational methods are very useful when circuits have multiple meshes. Instead of solving simultaneous equations manually, the program handles matrix formation, elimination, and validation automatically. This reduces effort and improves reliability.

The KVL verification values show zero or near-zero error, which proves the solution is mathematically correct within numerical precision. The generated graphs also make the output easier to interpret and present in the final report.

---

## 11. Advantages Of The Project

- reduces manual calculation effort
- improves understanding of mesh analysis
- provides accurate and quick numerical results
- demonstrates practical use of programming in electrical engineering
- supports both sample and manual input modes
- automatically generates report-ready graphs
- gives readable output with proper units

---

## 12. Limitations

- the project is currently limited to DC planar circuits
- branch-by-branch circuit drawing is not part of the console model
- ideal component behavior is assumed

---

## 13. Scope For Future Improvement

The project can be extended further by adding:

- file-based input and output
- support for larger circuit libraries
- GUI-based implementation
- AC circuit analysis support
- automatic generation of flowcharts and reports

---

## 14. Conclusion

The project `DC Circuit Solver Using Mesh Analysis` successfully fulfills the objectives of the Course End Project for Basic Electrical Engineering Laboratory. The program converts electrical theory into a structured computational model and provides accurate mesh current solutions for DC circuits.

This project helped in understanding Kirchhoff's Voltage Law, matrix representation of circuit equations, and numerical solution methods. It also showed how programming can be effectively used in engineering analysis. Therefore, the project is both academically relevant and practically useful.

---

## 15. References

1. Prescribed Basic Electrical Engineering textbook.
2. Class notes on Kirchhoff's Laws and mesh analysis.
3. Laboratory manual for A9205 - Basic Electrical Engineering Laboratory.

---

## 16. Appendix: How To Run

Run the program using:

```powershell
pip install -r requirements.txt
python src\dc_mesh_analysis_solver.py
```

Repository contents required by CEP:

- `src/` - source code
- `report/` - final report files
- `screenshots/` - output screenshots
- `README.md` - project details
- `requirements.txt` - Python dependency file
