//
// size_of_dataType.cpp
// C++Basics
//
// 🎂"Here's to the crazy ones. The misfits. The rebels.
// The troublemakers. The round pegs in the square holes.
// The ones who see things differently. They're not found 
// of rules. And they have no respect for the status quo.
// You can quote them, disagree with them, glority or vilify
// them. About the only thing you can't do is ignore them. 
// Because they change things. They push the human race forward.
// And while some may see them as the creazy ones, we see genius.
// Because the poeple who are crazy enough to think thay can change
// the world, are the ones who do."
// 
// Created by Chyi Yaqing on 03/26/18.
// Copyright © 2018. Chyi Yaqing. All rights reserved.
//


#include <iostream>

// create a new name for an existing type using typedef 
typedef int INTEGER;

enum color {red=0, green=1, blue=2} c;
c = blue;

int main(int argc, const char * argv[]) 
{
	// Your Programming statements HERE!
    std::cout << "Size of char :" << sizeof(char) << std::endl; // endl, which insert a new-line character after every line and 
    std::cout << "Size of int :" << sizeof(int) << std::endl; 
    std::cout << "Size of short int :" << sizeof(short int) << std::endl;
	std::cout << "Size of long int :" << sizeof(long int) << std::endl; 
    std::cout << "Size of float :" << sizeof(float) << std::endl; 
    std::cout << "Size of double :" << sizeof(double) << std::endl; 
    std::cout << "Size of wchar_t :" << sizeof(wchar_t) << std::endl; 
    std::cout << "Size of INTEGER :" << sizeof(INTEGER) << std::endl;
    std::cout << c << std::endl; 
    std::cout << "Hello, World!\n";
	return 0;
}

