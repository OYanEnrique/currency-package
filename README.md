# 💵 Currency Utility Package

This project is a Python package named `utilitiescv` designed to handle common currency-related tasks. It includes modules for formatting, calculation, and safe user input. A test script, `coin_test.py`, is provided to demonstrate how to use the package.

## Project Structure

The repository is organized as a Python package:

```
currency-package/
├── coin_test.py         # Main script to run the demonstration
└── utilitiescv/
    ├── __init__.py      # Makes the directory a Python package
    ├── coin.py          # Module with currency calculation functions
    └── data.py          # Module with input validation functions
```

## Features

The `utilitiescv` package provides the following functionalities:

* **Currency Calculations (`coin.py`)**:
    - `increase()`: Increases a value by a given percentage.
    - `decrease()`: Decreases a value by a given percentage.
    - `double()`: Doubles a value.
    - `half()`: Halves a value.
* **Safe Input (`data.py`)**:
    - `readmoney()`: A robust function that prompts the user for a price, handling invalid (non-numeric) input and re-prompting until a valid value is entered.
* **Formatted Summary (`coin.py`)**:
    - `summary()`: A function that takes a price and tax rates, and prints a neatly formatted summary of all calculations.

## How to Use

1.  Ensure you have the complete file structure as shown above.
2.  Navigate to the root directory (`currency-package/`) in your terminal.
3.  Run the main test script:
    ```sh
    python coin_test.py
    ```
4.  The program will prompt you to enter a price and then display the full summary.

### Example Session

```sh
> python coin_test.py
Enter the price: $150.50
------------------------------
    Value Summary         
------------------------------
Analyzed price: 	$150,50
Double the price: 	$301,00
Half the price: 	$75,25
20% increase: 	$180,60
12% reduction: 	$132,44
```
