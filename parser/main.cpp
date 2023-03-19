#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream source("../DATA-2022.10.25.11.47.52.509.r3a", ios::binary);
    ofstream output("../output.txt");

    uint16_t x;
    int max = 60 * 1000 * 1000;
    while (source.read(reinterpret_cast<char *>(&x), 2)) {
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
