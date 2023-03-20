#include <iostream>
#include <fstream>
#include <cstdint>

using namespace std;

string data_80_120_folder = "Lodz-02_80-120MHz";
string data_80_120_file = "DATA-2022.08.25.16.56.50.777";

string data_50_90_folder = "Lodz-03_50-90MHz";
string data_50_90_file = "DATA-2022.08.26.11.18.44.498";

string data_20_60_folder = "Lodz-07_20-60MHz";
string data_20_60_file = "DATA-2022.10.25.11.47.52.509";

string selected_folder = data_20_60_folder;
string selected_file = data_20_60_file;

int main() {
    ifstream source("../../../" + selected_folder + "/" + selected_file + ".r3a", ios::binary);
    ofstream output("../output-" + selected_folder + ".txt");

    int16_t x;
    int max = INT_MIN;
    int min = INT_MAX;
    int i = 0;
    bool head_only = false;
    while (source.read(reinterpret_cast<char *>(&x), sizeof(x))) {
        if (max < x) {
            max = x;
        }
        if (min > x) {
            min = x;
        }
        if (i == 10000 && head_only) {
            break;
        }
        i++;

        output << (x >> 2) << endl;
    }

    source.close();
    output.close();

    cout << "Samples count: " << i << endl;
    cout << "MAX: " << (max >> 2) << endl;
    cout << "MIN: " << (min >> 2) << endl;

    return 0;
}
