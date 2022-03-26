/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* arr, int n, int target,int *size)
{
    int i,j;
    int *a;
    *size=2;
    a = (int*)malloc(2*sizeof(int));
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
              if((arr[i]+arr[j])==target)
              {
                a[0]=i;
                a[1]=j;
                 break;
              
        }
        
      }
    }
 return a;
    }