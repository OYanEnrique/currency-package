# 💵 Currency Utility Package

This project is a Python package named `utilitiescv` designed to handle common currency-related tasks and robust user input. It includes modules for formatting, calculation, and safe data entry, along with a test script (`coin_test.py`) that shows how to use it.

## Project Structure

The repository is organized as a Python package:

```
Currency project/
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
    - `summary()`: Prints a neatly formatted summary of all calculations.
* **Safe Input (`data.py`)**:
    - `readint()`: A robust function that prompts for an integer and handles `ValueError`, `TypeError`, and `KeyboardInterrupt`.
    - `readfloat()`: A robust function that prompts for a float and handles the same errors.

## How to Use

1.  Ensure you have the complete file structure as shown above.
2.  Navigate to the root directory (`Currency project/`) in your terminal.
3.  Run the main test script:
    ```sh
    python coin_test.py
    ```
4.  The program will prompt you to enter a price and then display the full summary, followed by prompts for an integer and a float.

### Example Session

```sh
> python coin_test.py
Enter the price: $150
------------------------------
    Value Summary         
------------------------------
Analyzed price: 	$150,00
Double the price: 	$300,00
Half the price: 	$75,00
20% increase: 	$180,00
12% reduction: 	$132,00
Enter an integer: $abc
 ERROR: please enter a valid integer.
Enter an integer: $5
Enter a real number: $12.5
The integer value entered was 5 and the real value was 12.5
```
