/*
  Blank Simple Project.c
  http://learn.parallax.com/propeller-c-tutorials 
*/
#include "simpletools.h"                      // Include simple tools

int main()                                    // main function
{
  while(1)                                    // Endless loop
  {
    high(5);                                  // Set P5 high
    pause(1);                                 // Wait for circuit to charge
    int t = rc_time(5, 1);                    // Measure decay time on P5
    print("t = %d\n", t);                     // Display decay time
    pause(100);                               // Wait 1/10th of a second
  }
}
 