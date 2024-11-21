#pragma once
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include "general.h"

using namespace std;

void rsa(vector<string>& args)
{
	vector<int> sfdsfsa;
	int h = 1;

	int p = args[1] != "_" ? stoi(args[1]) : -1;
	int q = args[2] != "_" ? stoi(args[2]) : -1;
	

	if (p == -1 && q == -1)
	{
		cout << "!not enough arguments! enter p or q!" << endl;
		return;
	}

	if (p == -1)
	{
		p = findCoprimeNumberBigger(q);
	}
	else if (q == -1)
	{
		q = findCoprimeNumberBigger(p);
	}


	int n = p * q;
	int fi = (p - 1) * (q - 1);
	int e = args[3] != "_" ? stoi(args[3]) : -1;
	if (e == -1)
	{
		e = findCoprimeNumberSmaller(fi);
	}

	int d = findModMulArg(e, fi);
	int m = hashMessage(sfdsfsa, h, n);

	int S = power(m, d, n);

	

	int check = power(S, e, n);

	cout << format(" p = {} \n q = {} \n e = {} \n n = {} \n fi = {} \n d = {} \n h = {} \n hash = {} \n s = {} \n h\': {}", p, q, e, n, fi, d, h, m, S, check);

}