SO_LIB_NAME = lib/tree_diet_cpp`python3-config --extension-suffix`
FLAGS = -O3 -Wall -shared -std=c++17 -fPIC `python3 -m pybind11 --includes`
SRC_FILE = src/tree_diet_dp_implem.cpp 

linux:
	c++ $(FLAGS) $(SRC_FILE) -o $(SO_LIB_NAME)


clean:
	rm lib/*.so
