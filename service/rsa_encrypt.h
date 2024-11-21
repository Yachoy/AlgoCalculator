#include "general.h"

void rsa_encrypt(vector<string> args)
{

	int p = args[2] != "_" ? stoi(args[2]) : -1;
	int q = args[3] != "_" ? stoi(args[3]) : -1;
	int d = args[4] != "_" ? stoi(args[4]) : -1;

	vector<int> message =stringToIntegers(args[1]);


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
	int m = (p - 1) * (q - 1);

	int e = findModMulArg(d, m);


	vector<int> encrypted;

	cout << "\n#encryption...\n\"";
	for (auto el : message)
	{
		int encryptedSymbol = power(el, e, n);
		encrypted.push_back(encryptedSymbol);
		cout << format("{} ", encryptedSymbol);
	}
	cout << "\" " << format("{} {} {}", e, n, d) << endl;

	cout << "\n#decryption...\n";

	for (auto el : encrypted)
	{
		int encryptedSymbol = power(el, d, n);
		cout << format("#{} = {}\n", el, encryptedSymbol);
	}
}