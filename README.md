# fuzzy-inference-system

This repository contains the implementation of a Fuzzy Inference System.

An inference system is made up of 4 main components: a knowledge base, fuzzification systems, inference systems, and defuzzification systems.

## Fuzzification

This component assigns the input variables different degrees of membership in the different classes. For this, the input values are mapped to values from 0 to 1 using a set of membership functions.

The membership functions implemented in our system were:

- Triangular function
- Trapezoidal function
- S function

Each of the membership functions was implemented in `membership.py`, where each function is a class that receives each of the previously exposed variables as a parameter. They are then evaluated for each of the points other than *x*.

## Operations with fuzzy sets

The three basic operations of fuzzy sets were defined:

- Union
- Intersection
- Complement

Each of this operations is implemented in `operators.py`

## Inference Systems

The inference mechanisms relate the input and output fuzzy sets, and represent the rules that define the system. The inputs to this component are fuzzy sets (degrees of membership) and the outputs are also fuzzy sets, associated with the output variable. For the implementation of this inference system, 2 aggregation methods were implemented. For the creation of the system, it receives as input the name of one of these methods

### Aggregation Methods

- Mamdani Method
- Larsen Method

These methods are implemented in `aggregation.py`as classes that receive the set of rules to analyze, as well as the domain and precision with which the different values of the output fuzzy set are analyzed.

## Defuzzification

In this stage, the opposite function of the diffuser is performed. The input it receives is the output fuzzy set, the result of the inference stage, and the output is a specific value of the output variable. To obtain, from the output fuzzy set resulting from the aggregation of all the rules, a scalar result, mathematical methods are applied. These algorithms were implemented in defuzzification.py. Here is a summary of them:

- Mean of Maximum (MOM)
- Left of Maximum (LOM)
- Right of Maximum (ROM)
- Median of Maximum (MMOM)
- Centroid of Area (COA)
- Bisector of Area (BOA)

## Problem

The chosen problem to analyze and validate the proposed system is an autofocus system. To run this example, simply run the file `sample.py`, where the values of the input variables, the aggregation method to use and the defuzzification method will be requested.

The chosen problem to analyze and validate the proposed system is an autofocus system.

To run this example, simply run the file sample.py, where the values of the input variables, the aggregation method to use and the defuzzification method will be requested.