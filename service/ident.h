#pragma once
#include <iostream>
#include <random>
#include <cmath>
#include <numeric>
#include "general.h"

// Функция для проверки, является ли число квадратичным вычетом
bool isQuadraticResidue(long long n, long long mod) {
    for (long long x = 0; x < mod; ++x) {
        if ((x * x) % mod == n) {
            return true;
        }
    }
    return false;
}


long long smallestQuadraticResidue(long long n, long long residue) {
    long long smallest = -1; // -1 означает, что решение не найдено

    for (long long x = 0; x < n; ++x) {
        if ((x * x) % n == residue) {
            smallest = x;
            break; // Нашли наименьшее, выходим из цикла
        }
    }

    return smallest;
}

int test(vector<string>& args) {
    // 1. Настройка
    long long p, q;
    p = stol(args[1]);
    q = stol(args[2]);
    vector<int> rand_bits = stringToIntegers(args[3]);
    vector<int> xs = stringToIntegers(args[4]);
    int r = stoi(args[5]);

    long long n = p * q;




    int k = xs.size();



    std::vector<long long> X(k);
    std::vector<long long> V_values(k);
    vector<long long> V1_values(k);
    std::vector<long long> S_values(k);
    

    // Generating the table
    std::cout << "#X \t V \t V-1 \t S" << std::endl;
    for (int i = 0; i < k; ++i) {
        X[i] = xs[i];                        //distrib(gen);
        V_values[i] = power(X[i], 2, n);
        V1_values[i] = findModMulArg(V_values[i], n, true);
        S_values[i] = smallestQuadraticResidue(n, V1_values[i]);


        std::cout << "#" << X[i] << " \t " << V_values[i] << " \t " << V1_values[i] << " \t " << S_values[i] << std::endl;
    }

    int x1 = (r * r) % n;
    cout << "#x\' = " << x1 << endl;
    long long y = r;
    string butifulFormatY = format("#y = {} * (", r);
    for (int i = 0; i < rand_bits.size(); ++i)
    {
        y *= pow(S_values[i], rand_bits[i]);
        butifulFormatY += (i == 0 ? "" : " * ") + to_string(S_values[i]) + "^" + to_string(rand_bits[i]);
    }
    y %= n;
    cout << "" << butifulFormatY + ")mod" << n << " = " << y << endl;



    long long x = y * y;
    string butifulFormatX = format("#x = {} * (", r);
    for (int i = 0; i < rand_bits.size(); ++i)
    {
        x *= pow(V_values[i], rand_bits[i]);
        butifulFormatX += (i == 0 ? "" : " * ") + to_string(V_values[i]) + "^" + to_string(rand_bits[i]);
    }
    x %= n;
    cout << butifulFormatX + ")mod" << n << " = " << x << endl;

    return 0;
}
