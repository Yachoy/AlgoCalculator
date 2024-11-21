#pragma once
#include "general.h"

void elGomal(vector<string> args)
{
	int g = args[2] != "_" ? stoi(args[2]) : -1;
	int p = args[3] != "_" ? stoi(args[3]) : -1;
	int x = args[4] != "_" ? stoi(args[4]) : -1;
	int k = args[5] != "_" ? stoi(args[5]) : -1;

	vector<int> message = stringToIntegers(args[1]);


	if (p == -1 && g == -1)
	{
		cout << "!not enough arguments! enter p or q!" << endl;
		return;
	}

	if (g == -1)
	{
		g = findCoprimeNumberBigger(p);
	}
	else if (p == -1)
	{
		p = findCoprimeNumberBigger(g);
	}

	int y = power(g, x, p);
	int a = power(g, k, p);
	cout << format("p = {}\ng = {}\ny = {}\na = {}\n", p, g, y, a);

	cout << "#encryption...\n\"";
	vector<int> encrypted;

	for (auto el : message)
	{
		int b = (power(y, k, p) * el) % p;
		encrypted.push_back(b);
		cout << format("{} ", b);
	}
	cout << "\"\n";

	cout << "#decryption...\n";
	for (auto coded : encrypted)
	{
		if (coded < 0) coded += p; // Обработка отрицательных значений

		// Вычисляем a^(p-1-x) mod p
		long long a_pow = power(a, p - 1 - x, p);

		// Дешифруем: decrypted = (coded * a^(p-1-x)) mod p
		long long decrypted = (coded * a_pow) % p;

		if (decrypted < 0) decrypted += p; // Обработка отрицательных результатов (маловероятно)

		std::cout << std::format("#{} = {}\n", coded, decrypted);
	}

}