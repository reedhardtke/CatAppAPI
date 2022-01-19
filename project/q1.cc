#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

class ArrayFunction {
public:
    ArrayFunction() {

    }

    virtual float calculate(float array[], int size);

};

class Acc : public ArrayFunction{
    public:
    float calculate(float array[], int size) override{
        float sum = accumulate(array, array + size, 0.0);
        return sum / size;
    }
};

class Min : public ArrayFunction{
    public:
    float calculate(float array[], int size) override{
        return *min_element(array, array+size);
    }
};
class Max : public ArrayFunction{
    public:
    float calculate(float array[], int size) override {
        return *max_element(array, array+size);
    }
};

class First : public ArrayFunction{
    public:
    float calculate(float array[], int size) override {
        return array[0];
    }
};

int main() {
    float array[] {1,2,3,7};
    vector<ArrayFunction*> functions;
    functions.push_back(new Acc());
    functions.push_back(new Min());
    functions.push_back(new Max());
    functions.push_back(new First());

    for (int i = 0; i < functions.size(); i++) {
        cout << functions[i]->calculate(array, 4) << endl;
        delete functions[i];
    }

    return 0;
}