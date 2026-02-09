#include <stdio.h>

int max(int len,int arr[])
{
    int max = arr[0];
    for (int i = 0; i < len; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }
    return max;
}

int min(int len, int arr[])
{
    int min = arr[0];
    for (int i = 0; i < len; i++)
    {
        if (arr[i] < min)
        {
            min = arr[i];
        }
    }
    return min;
}

float avg(int len, int arr[])
{
    int sum = 0;
    for (int i = 0; i < len; i++)
    {
        sum += arr[i];
    }
    return (float) sum / len;
}

int* reverse(int len, int arr[])
{
    
}

int main(int argc, char argv[])
{
    int n;
    printf("\nEnter number of elements (btw 1 & 10): ");
    scanf("%d", &n);
    while (!(n > 0 && n < 11))
    {
        printf("\nPlease enter the number IN the range!\n");
        printf("Enter number of elements (btw 1 & 10): ");
        scanf("%d", &n);
    }
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        printf("\nEnter element %d: ", i+1);
        scanf("%d", &arr[i]);
    }
    int maxVal = max(n, arr);
    int minVal = min(n, arr);
    float avgVal = avg(n, arr);
    int* reversed = reverse(n, arr);
    printf("\n");
    printf("Max = %d\n", maxVal);
    printf("Min = %d\n", minVal);
    printf("Average = %f\n", avgVal);
}