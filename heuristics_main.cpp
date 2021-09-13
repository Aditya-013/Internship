#include<iostream>
#include<fstream>  //for files 
#include<cstring>  //for memset
#include<string>   //for strings
#include<time.h>   //for rand()

std::string count;
std::string piles;

//Getting rid of the extra space 
void removeDupWord(std::string str){
    int i = 0;
    for (auto x : str){
        if(x == ' ')
            i++;
        else if (i == 0)
            count = count + x;
        else
            piles = piles + x;
    }
    return;
}

//Calculating the sum of the entire pile
int sum_cal(int arr[], int n){
    int sum = 0;
    for(int i=0; i<n; i++){
        sum += arr[i];
    }
    return sum;
}

//Main
int main(){
    std::string myText;
    std::ifstream MyReadFile("non_uni/non_uni/alm1_10_5_13");

    //m = number of values 
    //n = total number of piles 
    std::getline (MyReadFile, myText); //Gets the first line with "m n"
    removeDupWord(myText); //Removes Space between m and n and stores values into the string count and piles (declared in line 5 & 6)

    int const m = stoi(count);  //string to integer
    int const n = stoi(piles);

    int arr[m], i=0;
    while (std::getline (MyReadFile, myText)) {
        arr[i] = stoi(myText);
        i++;
    }
    MyReadFile.close(); //Close file

    int sum = sum_cal(arr, m); //Calculates sum
    std::cout<<"The sum is:: "<<sum<<"\n";

    //Getting the values into the piles in a random order
    int pile[n][m];
    memset(piles, -1, sizeof(piles));   //Stores all the values as a '-1'
    srand(time(0));

}