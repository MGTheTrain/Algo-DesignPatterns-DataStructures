# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++11

# Directories
SRC_DIR = ./cpp
BUILD_DIR = ./build

# CMake commands
CMAKE = cmake
CMAKE_BUILD = $(CMAKE) --build $(BUILD_DIR)

# Target: build
.PHONY: build
build:
	@$(CMAKE) -B $(BUILD_DIR) -S $(SRC_DIR)
	@$(CMAKE_BUILD)

# Target: clean
.PHONY: clean
clean:
	@rm -rf $(BUILD_DIR)

# Target: run-executable
.PHONY: run-executable
run-executable:
	@./build/$(arg1)/$(arg2)/$(arg2)

# Target: run-python-script
.PHONY: run-python-script
run-python-script:
	@python3 python/$(arg1)/$(arg2).py
