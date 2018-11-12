#include <vector>
#include <stdexcept>
#include <algorithm>
#include <cstdio>

int split_quartile(int begin, int end, const std::vector<int> &data){
    if(end < begin)
        throw std::invalid_argument("Invalid range");
    
    if((end - begin)%2 == 0)
        return (data[begin + (end-begin)/2 - 1] + data[begin + (end-begin)/2])/2;
    else
        return data[begin + (end-begin)/2];
}

int main(){
    std::vector<int> input;
    int Q1, Q2, Q3;
    int size;
    // Input
    scanf("%d", &size);
    input.resize(size);
    for(int  i=0; i<size; i++)
        scanf("%d", &input[i]);
    std::sort(input.begin(), input.end());

    Q1 = split_quartile(0, size/2, input);
    Q2 = split_quartile(0, size, input);
    if(size%2 == 0)
        Q3 = split_quartile(size/2, size, input);
    else
        Q3 = split_quartile(size/2 + 1, size, input);
    printf("%d\n%d\n%d\n", Q1, Q2, Q3);
    return 0;
}
