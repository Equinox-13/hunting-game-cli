# hunting-game-cli

The project is part of the Applied AI Consulting technical assignment that implements a CLI based hunting game.

## Table of Contents

- [Overview & Class Diagram](#overview-class-diagram)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

## Overview & Class Diagram

1. User would be able to select one gun
2. User will be able to shoot the animals
3. On shooting a particular animal he will collect points
4. At the end show the points earned.

![Class diagram](./assets/class_diagram_game.jpg)

## Directory Structure
- **hunting-game-cli/**
  - `assets/class_diagram_game.jpg`: Contains class diagram.
  - `hunting_game.py`: Main script file to play the game.
  - `test_functions.py`: Contains unit tests for the functions
  - `README.md`: Project overview, installation, and usage details.
  - `.gitignore`: Specifies intentionally untracked files to ignore in version control.

## Installation
Clone the repository:

```bash
git clone https://github.com/Equinox-13/hunting-game-cli
cd hunting-game-cli
```

## Usage
Execute the hunting_game.py with the below command.

```bash
python hunting_game.py
```
Output:

```commandline
Welcome to the Hunting Game!
Select your gun:
1. Pistol (10 power)
2. Shotgun (20 power)
3. Rifle (30 power)
Enter your choice: 1
You've encountered a Rabbit!
Do you want to shoot? (yes/no): yes
You shot the Rabbit and earned 100 points!
Do you want to continue hunting? (yes/no): no
Game Over! You earned 100 points.
```


## Testing
Run the unit tests using the unittest module 

```bash
python -m unittest test_functions.py
```

