#include <iostream>
#include <Windows.h>
#include <random>

using namespace std;

int gameOver;
int const screenWidth = GetSystemMetrics(SM_CXSCREEN);
int const screenHeight = GetSystemMetrics(SM_CYSCREEN);
int x, y;

void log(const std::string &message)
{
    std::cout << "[LOG] " << message << std::endl;
}

void Setup()
{
    gameOver = 1;
    std::cout << "Width: " << std::to_string(screenWidth) << std::endl;
    std::cout << "Height: " << std::to_string(screenHeight) << std::endl;
}

void Draw()
{
    std::cout << "Width: " << std::to_string(screenWidth) << std::endl;
    std::cout << "Height: " << std::to_string(screenHeight) << std::endl;
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dis(0, screenWidth - 1);
    int randomWidth = dis(gen);
    std::uniform_int_distribution<int> dist(0, screenHeight - 1);
    int randomHeight = dist(gen);
    system("cls");

    for (int i = 0; i < screenHeight; i++)
    {
        for (int j = 0; j < screenWidth; i++)
        {
            if (j == randomWidth && i == randomHeight)
            {
                std::cout << "#";
            }
            else
            {
                std::cout << " ";
            }
        }
    }
    cout << std::ends;
}

void Input()
{
}

void Logic()
{
}

int main()
{
    Setup();
    while (gameOver < 2)
    {
        Draw();
        Input();
        Logic();
        gameOver++;
    }
}
