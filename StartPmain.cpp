#include<io.h>
#include<iostream>
#include <fstream>
#include<graphics.h>
void repair(int s)
{
	if (s == 1)
	{
		std::ofstream refile;
		if (!refile)
		{
			std::cout << "Wroing";
			system("pause");
			exit(0);
		}
		else
		{
			refile.open("./init.py");
			refile << "import sys\nimport pygame\npy=pygame\npy.init()\nscr=py.display.set_mode((325,400))\npy.display.set_caption" << "('Fight War')\n";
			refile << "f=py.font.Font('C:/Windows/Fonts/simhei.ttf',50)\ndef outtext(d):\n";
			refile <<"	tx=f.render(d,True,(255,255,255),(0,0,0))\n";
			refile <<"	txR=tx.get_rect()\n";
			refile <<"	txR.center=(325/2,200)\n";
			refile <<"	scr.blit(tx,txR)\n";
			refile << "outtext('START')"<<std::endl;
			refile.close();
		}
	}
}
void checkfile()
{
	if (_access("./init.py", 0) != 0)
	{
		std::cout << "init.py can not find!" << std::endl;
		system("pause");
		std::cout << "Repairing...\n";
		repair(1);
	}
	if (_access("./main.py", 0) != 0)
	{
		std::cout << "main.py can not find!"<<std::endl;
		system("pause");
	}
}
int main()
{
	checkfile();
}