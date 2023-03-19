#include <iostream>
#include <fstream>
#include <cstdint>

using namespace std;

int main() {
    ifstream source("../../../Lodz-02_80-120MHz/DATA-2022.08.25.16.56.50.777.r3a", ios::binary);
    ofstream output("../output.txt");

    int16_t x;
    int max = 60 * 1000 * 1000;
    while (source.read(reinterpret_cast<char *>(&x), sizeof(x))) {
        if (x & 0x8000) {
            x = -((~x + 1) & 0xFFFF);
        }

        output << x << endl;
        cout << x << endl;
        if (max < 0) {
            source.close();
            output.close();
            return 0;
        }
        max--;
    }

    source.close();
    output.close();

    return 0;
}
