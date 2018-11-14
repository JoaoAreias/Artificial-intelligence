#include <map>
#include <algorithm>
#include <vector>
#include <cstdio>


int main(){
    int size, mode;
    double mean;

    std::vector<int> input;
    std::map<int, int> frequency;
    
    scanf("%d", &size);
    input.resize(size);
    for(int i=0; i<size; i++){
        scanf("%ld", &input[i]);
        frequency[input[i]]++;
        mean += input[i];
    }
    // Mean
    mean /= (double)size;
    printf("%.1lf\n", mean);
    // Median
    std::sort(input.begin(), input.end());
    if(size % 2 == 0)
        printf("%.1lf\n", (double)(input[size/2] + input[size/2 - 1])/2);
    else
        printf("%.1lf\n", input[size/2]);
    // Mode
    int max_freq = 0;
    for(std::pair<int, int> p: frequency){
        if(p.second > max_freq){
            mode = p.first;
            max_freq = p.second;
        }
    }
    printf("%d\n", mode);
    return 0;
}