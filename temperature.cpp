#include <iostream>
#include <cstdlib>
#include <fstream>

int main(int argc, char* argv[])
{

  int tempselection; // Declare variables without data to be used later
  float tempc;

  tempselection = atoi(argv[1]);
  std::cout << "The temp in Fahrenheit : " << tempselection << "\n"; 

  tempc = (tempselection - 32) / 1.8; // Calculate Celsius from Fahrenheit with it's formula.

  std::cout << "The temp is " << tempc << " degrees Celsius.\n"; // Output calculated Celsius value.

  std::ofstream MyFile("results.txt");
  MyFile << "input:" << tempselection << "\n";
  MyFile << "output:" << tempc;
  MyFile.close();
  
}