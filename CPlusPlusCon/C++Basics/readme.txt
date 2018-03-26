C++ is a statically typed, compiled, general-purpose, case-sensitive, free-form programming language that supports procedural, object-oriented, and generic programming.

C++ was developeed by Bjarn Stroustrup starting in 1979 at Bell Labs. 

C++ is a superset of C, and that virtually any legal C program is a legal C++ program. 


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

What a class, object, methods, variabel?
	Object: 
		Object have states and behaviors
	Class:
		A class can be defined as a template/blueprint that describes the behaviors/state that object of its type support 
	Methods:
		A method is basically a behavior 

C++ reserved words:
	asm		else	new		this	auto	enum	operator	throw		bool	explicit	private		true	break	
	export	protected	try		case	extern	public	typedef		catch	false	register	typid	char	float	
	reinterpret_cast	typename	class	for return	union	const	friend	short	unsigned	const_cast	goto	signed 
	using	continue	if	sizeof	virtual		default		inline	static	void	delete	int		static_cast		valatile 
	do	long	struct	wchar_t		double mutable switch while dynamic_cast namespace	template 

a Few characters have an alternative representation, called a trigraph sequence. 
	??=			#
	??/			\ 
	??'			^ 
	??(			[
	??)			]
	??!			|
	??<			{
	??>			}
	??-			~
All the compilers do not sypport trigraph and they are not advised to be used because of their confusing nature. 

Data Types 
	C++ offers he programmer a rich assortment of built-in as well as user defined data types.
	Boolean			bool
	Character		char 
	Integer			int 
	Floating point	float 
	Double			double 
	valueless		void 
	wide character	wchar_t 

Serveral of the basic types can be modifed using one or more of these type modifier.
	signed 
	unsigned 
	short 
	long 

char				1byte		-127 to 127 or 0 to 255 
unsigned char		1 byte		0 to 255 
signed char			1byte		-127 to 127 
int					4bytes		-2146283648	to 2147482648
unsigned int		4bytes		0 - 4294967295 
signed int			4bytes 
short int			2bytes 
unsigned short int	Range 
signed short int	Range 
long int			4 bytes 
signed long int		4bytes 
unsigned long int	4bytes 
float				4bytes	(7 digits)
double				8bytes	(15 digits )
long double			8bytes	(15 digits )
wchar_t				2 or 4 bytes (1 wide character)

The size of variables might be different from those shown in the above 

wchar_t : A wide character type 

