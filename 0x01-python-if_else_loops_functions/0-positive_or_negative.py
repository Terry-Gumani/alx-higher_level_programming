#!/usr/bin/python3
import random

/**
 *main - Print if a number is positive or negative
 *Return: 0
 */

int main(void)
{
	number = random.randint(-10, 10)
            if number > 0:
                 print(number, "is positive")
            elif number < 0:
                 print(number, "is negative")
            else:
                 print(number, "is zero")
}                 
