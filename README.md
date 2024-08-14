# 🤖 KakuroSolver-AI

## Overview
This repository contains a Python-based AI solution for solving Kakuro puzzles. Kakuro, a numerical crossword-like puzzle, can be challenging to solve manually, but this project leverages artificial intelligence techniques to automate the process, offering a quick and accurate solution.

## 🧩 What is Kakuro?
Kakuro is a logic-based puzzle that combines elements of crossword puzzles and Sudoku. The goal is to fill in the grid with numbers that add up to the specified clues, ensuring that no number repeats within a block.

## ✨ Features
- **AI-Powered Solver**: Utilizes Constraint Satisfaction Problems (CSP) and advanced backtracking algorithms to efficiently solve Kakuro puzzles.
- **Customizable Input**: Allows users to input their own Kakuro grids and get solutions quickly.
- **Flexible Grid Size**: Handles Kakuro puzzles of different sizes and complexities.

## 🧩 Here's a Kakuro Example
![Kakuro Example](kakuro_example.png)


## 🚀 Getting Started

### Prerequisites
- 🐍 Python 3.6 or higher
- Required Python libraries: `numpy`, `pandas`, `itertools`

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/KakuroSolver-AI.git
    ```
2. Navigate to the project directory:
    ```bash
    cd KakuroSolver-AI
    ```
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Solver
1. Run the main script:
    ```bash
    python kakuro_solver.py
    ```
2. Input your Kakuro puzzle grid following the provided instructions.
3. View the output solution in the terminal or save it to a file.

## 🧠 Code Explanation
The AI for solving Kakuro puzzles in this project is built using:
1. **Constraint Satisfaction Problems (CSP)**: Defines the Kakuro puzzle as a CSP, where each cell is a variable, and the constraints are based on the sums and unique number rules.
2. **Backtracking Algorithm**: The core algorithm that tries different number combinations while ensuring the constraints are met.
3. **Constraint Propagation**: Reduces the search space by eliminating impossible numbers early in the process.
4. **Heuristics**: Implements intelligent guessing to speed up the solving process, especially in large or complex grids.

## 🎛️ Customization
You can modify the input grid and adjust the solver parameters to handle different puzzle sizes and difficulties.

## 🤝 Contributions
Contributions are welcome! If you find any issues, have ideas for improvements, or want to add new features, feel free to open an issue or submit a pull request.


## 📬 Contact
For any questions, feedback, or further information, feel free to reach out:
📧 [aparsa.khadem@gmail.com](mailto:aparsa.khadem@gmail.com)
