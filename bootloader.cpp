#include <iostream>
#include <cstdlib>

int main() {
    // Specify the full path to the Python script
    const char* command = "C:\\Python311\\python.exe D:\\Creations\\GithubCommit\\Commit-Bot-main\\GeometricAnalysis.py";

    int returnCode = std::system(command);

    if (returnCode == 0) {
        std::cout << "Python script executed successfully." << std::endl;
    } else {
        std::cout << "Error executing the Python script." << std::endl;
    }

    // Wait for a key press before closing the window
    std::cin.get();

    return 0;
}
