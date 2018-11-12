#include <vector>
#include <stdexcept>
#include <algorithm>
#include <cstdio>
#include <map>


class Array{
    /*
        Class to interpret a frequency table as an array
    */
    private:
        std::map<int, int> m_elements; // Stores the cummulative frequency of each element
        int m_size;
    public:
        int size(){ return m_size; };
        int operator[](int x){
            // Get an element of the array in O(log n)
            if(m_elements.find(x) != m_elements.end())
                return m_elements[x];
            
            auto pos = m_elements.lower_bound(x);
            pos--;
            return pos->second;
        }
        Array(std::map<int, int> freq_table){
            m_size = 0;
            for(std::pair<int, int> entry: freq_table){
                m_elements[m_size] = entry.first;
                m_size += entry.second;
            }
        }
};

double split_quartile(int begin, int end, Array &data){
    if(end < begin)
        throw std::invalid_argument("Invalid range");
    
    if((end - begin)%2 == 0)
        return (double)(data[begin + (end-begin)/2 - 1] + data[begin + (end-begin)/2])/2;
    else
        return (double)data[begin + (end-begin)/2];
}

int main(){
    std::vector<int> input;
    std::map<int, int> frequency;

    double Q1, Q3;
    int size;
    // Input
    scanf("%d", &size); // Get input size
    input.resize(size);
    for(int  i=0; i<size; i++)
        scanf("%d", &input[i]);
    for(int  i=0; i<size; i++){
        int aux;
        scanf("%d", &aux);
        frequency[input[i]] = aux;
    }
    Array array(frequency);
    size = array.size();
    
    Q1 = split_quartile(0, size/2, array);
    Q3 = split_quartile(size/2 + size%2, size, array);
    
    printf("%.1lf\n", Q3 - Q1);
    return 0;
}
