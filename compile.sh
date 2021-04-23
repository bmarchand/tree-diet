c++ -O3 -Wall -shared -std=c++17 -fPIC `python3 -m pybind11 --includes` src/graph_cpp_routines.cpp -o lib/graph_cpp_routines`python3-config --extension-suffix`
