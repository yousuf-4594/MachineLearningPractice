#include <iostream>
#include <cstdlib>
#include <windows.h> // Include the Windows API header

int main() {
    // Specify the full path to the Python executable
    const char* command = "C:\\Python311\\python.exe GeometricAnalysis.py";

    int returnCode = std::system(command);

    if (returnCode == 0) {
        std::cout << "Python script executed successfully." << std::endl;
    } else {
        std::cout << "Error executing the Python script." << std::endl;
    }

    // Introduce a delay (e.g., 5000 milliseconds) before waiting for a key press
    Sleep(5000);

    // Wait for a key press before closing the window
    std::cin.get();

    return 0;
}

