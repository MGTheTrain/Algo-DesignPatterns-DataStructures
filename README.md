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
| Adapter                | Commonly used when integrating systems with incompatible interfaces or when adapting legacy code to work with modern components      | Dependency Inversion Principle (DIP)                     | Structural  |
| Decorator              | Widely used for adding functionality to objects dynamically without altering their existing logic, promoting code reuse and flexibility | Open/Closed Principle (OCP)                              | Structural  |
| Dependency Injection   | Essential for decoupling components, facilitating testing, and improving flexibility by removing hard-coded dependencies | Dependency Inversion Principle (DIP)                     | Behavioral |
| Observer               |  Frequently employed for implementing event handling mechanisms and building distributed systems that require communication between components | Single Responsibility Principle (SRP)                    | Behavioral |
| Strategy               | Valuable for encapsulating algorithms and enabling runtime algorithm selection, providing another option to long if-else statements and promoting code maintainability | Open/Closed Principle (OCP)                              | Behavioral |
| Singleton              |  Often used for managing resources centrally and ensuring a single instance of a class throughout the application | Single Responsibility Principle (SRP)                    | Creational |
| Builder                |  Commonly utilized for constructing complex objects step by step, improving clarity and maintainability in code that deals with object creation | Single Responsibility Principle (SRP)                    | Creational |


## References

- [Space and time Big-O complexities of common algorithms](https://www.bigocheatsheet.com)

## Features

- [x] Coding design patterns for design principles (e.g. SOLID) and their use cases in C++
- [x] Coding design patterns for design principles (e.g. SOLID) and their use cases in Python
- [ ] Efficient array sorting algorithms in terms of complexity in Python
- [ ] Basic data structures including their common operations (insertion, deletion, search) and associated complexities along with practical applications in Python

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

To run C++ applications, execute:

```sh
make run-executable arg1=<e.g. design-patterns> arg2=<e.g. adapter, decorator, builder, dependency-injection, observer, singleton, strategy>
# Example: Decorator sample app 
make run-executable arg1=design-patterns arg2=decorator
```

To run Python scripts, execute:

```sh
make run-python-script arg1=<e.g. design-patterns> arg2=<e.g. adapter, decorator, builder, dependency-injection, observer, singleton, strategy>
# Example: Builder sample app
make run-python-script arg1=design-patterns arg2=builder
```

In order to remove build artifacts from C++ compilation:

```sh
make clean
```
