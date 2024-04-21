# Algo-DesignPatterns-DataStructures

## Table of Contents

+ [Summary](#summary)
+ [References](#references)
+ [Features](#features)
+ [Getting started](#getting-started)

## Summary

Curated list of design patterns, data structures, array sorting algorithms and their use cases

### Design Patterns

| Design Pattern         | Practical Use Cases                                            | SOLID Principles and Other Relevant Principles           | Category    |
|------------------------|----------------------------------------------------------------|----------------------------------------------------------|-------------|
| Adapter                | Integrating incompatible interfaces, adapting legacy code      | Dependency Inversion Principle (DIP)                     | Structural  |
| Decorator              | Adding functionality to objects dynamically                    | Open/Closed Principle (OCP)                              | Structural  |
| Dependency Injection   | Decoupling components, facilitating testing and flexibility    | Dependency Inversion Principle (DIP)                     | Behavioral |
| Observer               | Implementing event handling, building distributed systems      | Single Responsibility Principle (SRP)                    | Behavioral |
| Strategy               | Encapsulating algorithms, enabling runtime algorithm selection | Open/Closed Principle (OCP)                              | Behavioral |
| Singleton              | Managing resources centrally, ensuring single instance         | Single Responsibility Principle (SRP)                    | Creational |
| Builder                | Constructing complex objects step by step, maintaining clarity | Single Responsibility Principle (SRP)                    | Creational |


## References

- [Space and time Big-O complexities of common algorithms](https://www.bigocheatsheet.com)

## Features

- [ ] Coding design patterns for design principles (e.g. SOLID) and their use cases
- [ ] Efficient array sorting algorithms in terms of complexity 
- [ ] Basic data structures including their common operations (insertion, deletion, search) and associated complexities along with practical applications

## Getting started

### Preconditions

- If your IDE supports it, install [Dev Containers extension](https://code.visualstudio.com/docs/devcontainers/containers)
- **(Optionally)** Download a [Python Release](https://www.python.org/downloads/) and a [CMake release](https://cmake.org/download/) 
- `make` cli tool

**NOTE:** On Windows you would preferably utilize the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install) in order to utilize the `make` cli tool

### Makefile

To compile the C++ source files into executables, execute the following command:

```sh
make build
```

In order to remove build artifacts:

```sh
make clean
```
