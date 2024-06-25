//una cadena de caracteres ingresada por el usuario es un palíndromo ¡Pero hazlo en C++! :)

#include <iostream>
#include <cctype> 
#include <string>

bool esPalindromo(const std::string& str) {
    int left = 0;
    int right = str.length() - 1;

    while (left < right) {
        
        while (left < right && !std::isalnum(str[left])) {
            ++left;
        }
        while (left < right && !std::isalnum(str[right])) {
            --right;
        }

        
        if (std::tolower(str[left]) != std::tolower(str[right])) {
            return false;
        }

        ++left;
        --right;
    }

    return true;
}

int main() {
    std::string str;

    std::cout << "Ingrese una cadena para verificar si es un palindromo: ";
    std::getline(std::cin, str);

    if (esPalindromo(str)) {
        std::cout << "La cadena es un palindromo.\n";
    } else {
        std::cout << "La cadena no es un palindromo.\n";
    }

    return 0;
}
