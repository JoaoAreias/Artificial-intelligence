#include <vector>
#include <cstdio>
#include <cmath>

int main(){
    std::vector<int> input;
    double std_deviation=0, mean=0;
    int size;
    
    scanf("%d", &size);
    input.resize(size);
    // Compute mean
    for(int  i=0; i<size; i++){
        scanf("%d", &input[i]);
        mean += input[i];
    }
    mean /= size;
    // Cmpute Standard deviation
    for(int x: input)
        std_deviation += (x-mean)*(x-mean);
    std_deviation = sqrt(std_deviation/size);

    printf("%.1lf", std_deviation);
    return 0;
}