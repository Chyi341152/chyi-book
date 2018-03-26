C++ is a statically typed, compiled, general-purpose, case-sensitive, free-form programming language that supports procedural, object-oriented, and generic programming.

Object-Oriented Programming
	C++ fully supports object-oriented programming, including the four pillars of object-oriented development -
		Encapsulation  封装 
		Data hiding    数据隐藏
		Inheritance    继承
		Polymorphism   多态

Standard Libraries
	The core language giving all the building blocks including variables, data types and literals, etc
	The C++ Standard library giving a rich set of functions manipulating files,strings,etc
	The Standard Template Library (STL) giving a rich set of methods manipulating data structures,etc 

The ANSI Standard 
	The ANSI standard is an attempt to ensure that C++ is portable; The ANSI standard has been stable for a while, and all the major C++ compiler manufacturers support the ANSI standard.


Local Environment Setup
	C++ typically are named with the extension .cpp, .cp, or .c 
	
C++ Compiler
	GNU C/C++ compiler 

Installing GNU C/C++ Compiler 
	$ g++ -v 

C++ Basic Syntax 

Step 1: Write the Source Code:
	

Step 2: Build the Execute Code:
	Compile and link (aka Build) the source "hello.cpp" into executable code ("hello.exe" in Windows or "hello" in Unix/Linux/Mac)
	
	// Windows (CMD shell) - Build "hello.cpp" into "hello.exe"
	> g++ -o hello.exe hello.cpp 

	// Unix/Linux/Mac (Bash shell) - Build "hello.cpp" into "hello"
	> g++ -o hello hello.cpp

Step 3: Run the Executable Code 
	// Windows (CMD shell) - Run "hello.exe" (.exe is optional)
	> hello 

	// Unix/Linux/Mac (Bash shell) - Run "hello" (./ donetes the current directory)
	$ ./hello

