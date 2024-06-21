
//Escribir un programa que pida al usuario dos números y los sume. ¡Pero esta vez hazlo en C++! :)//
#include <iostream>

int main() {
    int num1, num2, suma;

    std::cout << "primer número: ";
    std::cin >> num1;

    std::cout << "segundo número: ";
    std::cin >> num2;

    suma = num1 + num2;

    std::cout << "La suma de " << num1 << " y " << num2 << " es " << suma << std::endl;

    return 0;
}

