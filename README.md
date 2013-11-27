Automation-of-Mutation-Testing
==============================

A python based automation of mutation testing done for C codes

The code runs with a GUI using easygui module in python. You can select the files to mutate. Then new mutants will be created and compiled also. Now the user will be asked for inputs (if any in the source file) and then all the mutants will be checked. If any fails then it will be killed and others will continue to exist. Another time user can feed the inputs and check if others are killed or can terminate directly.

Types of mutation performed...
Boolean
Replacement of unary operator             ++ by - - and vice versa
Replacement of conditional operator with another
  > by >=,==,<=
  == by >=
  < by <=,==,>=
  >= by >
  <= by <
  Replacement of boolean expressions with true or false
  Replacement of arithmetic operators     eg.  * and +, / and – , % with / and vice versa
  
Also if any mutant goes into an infinite loop then they are also checked and an alarm is raised. Once it is done the corresponding process(code) is terminated and the code continues for the next mutant.
In the end a test suite is displayed to the user to verify that for which inputs what all mutants are killed and how many are alive(if any).

Packages to be installed before running: easygui
