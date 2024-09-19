#include <stdio.h>
#include <bits/stdc++.h>
int search(int arr[], int n, int num)
{
    int i;
    for(int i=0; i<n; i++)
    {
        if(arr[i] == num)
        return i;
    }
    return -1;
}
vector<int> rotateArray(vector<int>& arr, int n)
{
    int first = arr[0];
    for(int i=0; i<n; i++)
    {
        arr[i] = arr[i+1];

    }
    arr[n-1] = first;
    return arr;
}
int main()
{
    int arr[] = {1, 2, 3, 4, 5};
    int num = 4;
    int n = sizeof(arr) / sizeof(arr[0]);
    int val = search(arr, n, num);
    printf("%d", val);
}
vector<int> moveZeros(int n, vector<int> a)
{
    vector<int> temp;
    for(int i=0; i<n; i++)
    {
        if(a[i] != 0)
        temp.push_back(a[i]);
    }
    int nz = temp.size();
    for(int i=0; i<nz; i++)
    {
        a[i] = temp[i];
    }
    for(int i=nz; i<n; i++)
    {
        a[i] = 0;
    }
    return a;
}

