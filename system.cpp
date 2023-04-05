#include <io.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <cstdlib>
#include <cstring>
#include <windows.h>
#include <urlmon.h>

#pragma comment(lib, "urlmon.lib")
#define DLLEXPORT extern "C" __declspec(dllexport)
DLLEXPORT void check()
{
    try{
        if (_access("enemy.py",0)!=0)
            throw -1;
        if (_access("main.py",0)!=0)
            throw -1;
        if (_access("player.py",0)!=0)
            throw -1;
    }
    catch (const char *error){
        printf("%s\n",error);
        system("pause");
    }
}