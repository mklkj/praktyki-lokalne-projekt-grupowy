#include <iostream>
#include <fstream>
#include <cstdint>

using namespace std;

int main() {
    ifstream source("../../../Lodz-07_20-60MHz/DATA-2022.10.25.11.47.52.509.r3a", ios::binary);
    ofstream output("../output-Lodz-07_20-60MHz-signed.txt");

    int16_t x;
    int max = INT_MIN;
    int min = INT_MAX;
    while (source.read(reinterpret_cast<char *>(&x), sizeof(x))) {
        if (max < x) {
            max = x;
        }
        if (min > x) {
            min = x;
        }

        output << (x >> 2) << endl;
    }

    source.close();
    output.close();

    cout << "MAX: " << max << endl;
    cout << "MIN: " << min << endl;

    return 0;
}
