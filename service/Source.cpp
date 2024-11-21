#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <locale> // ��� �����������
#include <fcntl.h>
#include "general.h"
#include "RSA.h"
#include "rsa_encrypt.h"
#include "elGomal.h"
#include "ident.h"

using namespace std;



int main() {
    //setlocale(LC_ALL, "ru_RU.UTF-8");
    // ������������� ������ ��� ��������� ������� �������� (�����!)
    locale::global(locale(""));

    //rsa_encrypt "3 10 26 15 7 3 29 11 17 10 18 16 8 16 12" 37 31 7
    //el-gamal_crypt "3 10 26 15 7 3 29 11 17 10 18 16 8 16 12" 7 41 13 19
    //ident-protocol 11 13 "0 1 1 0 1" "6 8 10 15 19" 7

    vector <int> mess = { 1 };
    //cout << "ready!" << endl;

    hashMessage(mess, 1, 1);

    while (true)
    {
        cout << endl;
        string command;
        getline(cin, command);
        if (command.empty()) continue;

        vector<string> commands = splitString(command);

        //test();
        if (commands[0] == "rsa_encrypt") rsa_encrypt(commands);
        else if (commands[0] == "el-gamal_crypt") elGomal(commands);
        else if (commands[0] == "ident-protocol") test(commands);

        cout << "end" << endl;

    }

    return 0;
}