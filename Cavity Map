#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    string grid[n];
    for(int i = 0; i < n;i++)
       cin >> grid[i];
    for(int i=1;i<n-1;i++)
    {
        for(int j=1;j<n-1;j++)
        {
         
            if(grid[i][j-1]<grid[i][j] && grid[i][j+1]<grid[i][j] && grid[i-1][j]<grid[i][j] && grid[i+1][j]<grid[i][j])
                  grid[i][j]='X';
        }
        
        
           
    }
    for(int i = 0; i < n;i++)
       cout<<grid[i]<<endl;
    
    return 0;
}
