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

### Data structures

| Data Structure    | Common Use Cases                                                                                                     | C++ (STL)                                            | Python                                               |
|-------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| Binary Tree       | - Binary Search Trees (BSTs) for dictionary and associative array implementations.                                    | `std::map`, `std::set`, `std::multimap`, `std::multiset` | `dict`, `set`                                        |
|                   | - Sorting and searching algorithms like binary search.                                                                 | `std::map`, `std::set`, `std::multimap`, `std::multiset`, `std::binary_search`, `std::lower_bound`, `std::upper_bound` | `sortedcontainers.SortedDict`, `sortedcontainers.SortedSet` |
|                   | - Expression trees for representing mathematical expressions.                                                         | `std::set`, `std::multiset` (for unique and duplicate keys) | Not directly available in the standard library, but libraries like `sortedcontainers` or `bintrees` can be used |
|                   | - Huffman coding for data compression.                                                                                | -                                                    | -                                                    |
| Doubly Linked List| - LRU (Least Recently Used) cache implementation.                                                                     | `std::list`                                          | `collections.deque`                                 |
|                   | - Undo functionality in text editors or software applications.                                                        | `std::list`                                          | -                                                    |
|                   | - Scheduling algorithms like round-robin scheduling.                                                                  | `std::list`                                          | -                                                    |
|                   | - Implementing deque (double-ended queue) data structure.                                                             | `std::deque`                                         | `collections.deque`                                 |
| Dynamic Array     | - Resizable array for storing elements.                                                                                | `std::vector`                                        | `list`                                               |
|                   | - Implementing lists in programming languages (e.g., Python's list, C++'s std::vector, Java's ArrayList).            | `std::vector`                                        | `list`                                               |
|                   | - Dynamic programming algorithms with varying input sizes.                                                             | `std::vector`                                        | `list`                                               |
| Graph             | - Social network analysis representing users as nodes and relationships as edges.                                     | Custom implementations or libraries like Boost.Graph | `networkx`                                           |
|                   | - Network routing algorithms to find shortest paths.                                                                   | Custom implementations or libraries like Boost.Graph | `networkx`                                           |
|                   | - Modeling dependencies between tasks or processes in project management.                                             | Custom implementations or libraries like Boost.Graph | `networkx`                                           |
| Hash Table        | - Associative arrays, dictionaries, or maps implementations.                                                           | `std::unordered_map`, `std::unordered_set`, `std::unordered_multimap`, `std::unordered_multiset` | `dict`, `set`                                        |
|                   | - Efficient lookup, insertion, and deletion operations.                                                                | `std::unordered_map`, `std::unordered_set`, `std::unordered_multimap`, `std::unordered_multiset` | `dict`, `set`                                        |
|                   | - Implementing symbol tables in compilers or interpreters.                                                             | -                                                    | -                                                    |
|                   | - Handling collisions using techniques like chaining or open addressing.                                              | -                                                    | -                                                    |


## References

- [Space and time Big-O complexities of common algorithms](https://www.bigocheatsheet.com)

## Features

- [x] Coding design patterns for design principles (e.g. SOLID) and their use cases in C++
- [x] Coding design patterns for design principles (e.g. SOLID) and their use cases in Python
- [ ] Efficient array sorting algorithms in terms of complexity in Python
- [x] Basic data structures including their common operations (insertion, deletion, search) and  practical applications in Python

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
