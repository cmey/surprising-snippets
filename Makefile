# Makefile has implicit rules, find them using something like:
#  make -p -f/dev/null | grep LINK
CXX=g++
CC=g++
CXXFLAGS=-std=c++11
LDLIBS=-lboost_unit_test_framework # -lboost_log
all: boost-unit-test boost-units
boost-unit-test: boost-unit-test.o
boost-units: boost-units.o
clean:
	rm -f boost-units.o boost-unit-test.o
