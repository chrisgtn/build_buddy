# BuildBuddy

BuildBuddy is a lightweight DevEx tool to automate building and testing small C projects using Make and SCons.

## Example Project

BuildBuddy includes a simple C project: a Terminal Beep Sound Generator.  
It demonstrates how BuildBuddy can automate the building and testing of interactive C programs.


## Features

- Build C code using Make or SCons
- Easy-to-use Python CLI (powered by Typer and Rich)
- Clean build artifacts
- Visualize build settings
- Supports Debug and Release profiles
- Focused on developer experience and reproducibility

## Usage

### Build the project
```bash
python buildbuddy.py build --system=make --profile=debug
python buildbuddy.py build --system=scons --profile=release
```

## Clean build artifacts
```bash
python buildbuddy.py clean
```

## Visualize project setup
```bash
python buildbuddy.py visualize
```
## Test the project

```bash
python buildbuddy.py test --system=make --profile=debug
```

## Requirements

- Python 3.8+
- rich
- typer
- gcc
- make
- scons
