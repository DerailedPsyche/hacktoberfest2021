#include<iostream>
using namespace std;


int main(){


    int n,k;
    cin>>n>>k;

    int *arr = new int[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    int count=0;
    int page =1;
    int qus = 1;
    for(int i=0;i<n;i++){
        int page_pr = arr[i]/k;
        int mod = arr[i]%k;
        int j;
        if(mod==0){
            j=page_pr+page;
        }
        else{
            j=page+page_pr+1;
        }
        /*cout<<" Current Page :"<<page<<endl;
        cout<<"Next Page : "<<j<<endl;*/
        for(int d =0; d<arr[i];d++){
            if(qus==page){
                count++;


            }
            //int p = qus%k;
            if(qus%k==0){
                page+=1;

            }

            /*else if(qus>=k+1 && qus==j-1){
                    count++;
            }*/

            qus++;
        }
        //cout<<"Current Count : "<<count<<endl;
        qus=1;
        page = j;
    }

    cout<<count<<endl;
}
