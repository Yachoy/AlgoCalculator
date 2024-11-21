#pragma once
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>
#include <map>
#include <cwctype>
#include <format>

using namespace std;

bool gcd(int a, int b)
{
	while (b != 0)
	{
		int temp = b;
		b = a % b;
		a = temp;
	}
	return a == 1;
}

int findCoprimeNumberBigger(int a)
{
	vector<int> ansers((int)sqrt(a));
	
	for (size_t i = a + 1; i < a * 2; i++)
	{
		if (gcd(a, i))
		{
			ansers.push_back(i);
		}
	}
	srand(static_cast<unsigned int>(time(0)));
	return ansers[rand() % ansers.size()];
}

int findCoprimeNumberSmaller(int a)
{
	vector<int> ansers((int)sqrt(a));

	for (size_t i = 2; i < a; i++)
	{
		if (gcd(a, i))
		{
			ansers.push_back(i);
		}
	}
	srand(static_cast<unsigned int>(time(0)));
	return ansers[rand() % ansers.size()];
}

int findModMulArg(int first, int limit, bool fromOne = false)
{
	for (size_t i = fromOne ? 1 : 2; i < limit * 10; i++)
	{
		if ((first * i) % limit == 1)
		{
			return i;
		}
	}
	cout << "didn\'t find comultiplier for \"mod expession\"!" << endl;
	return 0;
}

int hashMessage(vector<int> message, int h, int n) {
	

	for (auto c : message) {
		
		h = ((h + c) * (h + c)) % n;
		
	}

	return h; // Возвращаем вычисленное значение h
}

long long power(long long m, long long d, long long n) {
	long long res = 1;
	m %= n; // Оптимизация: сразу берем m по модулю n
	while (d > 0) {
		if (d % 2 == 1) {
			res = (res * m) % n;
		}
		m = (m * m) % n; // Возводим m в квадрат по модулю n
		d /= 2;
	}
	return res;
}

std::vector<std::string> splitString(const std::string& str) {
	std::vector<std::string> words;
	std::stringstream ss(str);
	std::string word;
	bool insideQuotes = false;

	while (ss >> std::ws) { // Eat up whitespace before each word
		if (ss.peek() == '"') {
			ss.ignore(); // Skip the opening quote
			insideQuotes = true;
			std::getline(ss, word, '"');  // Read until the closing quote
			insideQuotes = false;
			//If there are more double quotes, merge them into word
			while (ss.peek() == '"') {
				ss.ignore();
				std::string nextWord;
				if (ss.peek() == ' ') ss.ignore();
				std::getline(ss, nextWord, '"');
				word += "\"" + nextWord;
			}
		}
		else {
			ss >> word;
		}
		words.push_back(word);
	}
	return words;
}

std::vector<int> stringToIntegers(const std::string& str) {
    std::vector<int> result;
    std::stringstream ss(str);
    int num;

    while (ss >> num) {
        result.push_back(num);
    }

    return result;
}