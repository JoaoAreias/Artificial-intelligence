#include <vector>
#include <cstdio>


int main(){
    std::vector<int> x;
    std::vector<int> w;
    int size;

    scanf("%d", &size);
    x.resize(size);
    w.resize(size);

    for(int i=0; i<size; i++)
        scanf("%d", &x[i]);
    for(int i=0; i<size; i++)
        scanf("%d", &w[i]);

    double cum_sum = 0, weigh_sum;
    for(int i=0; i<size; i++){
        cum_sum += x[i]*w[i];
        weigh_sum += w[i];
    }
    
    printf("%.1lf", cum_sum/weigh_sum);
}