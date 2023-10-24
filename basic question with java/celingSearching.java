public class celingSearching {
    public static void main(String[] args)
    {
    int[] arr ={1,2,3,4,6,7,8};
    int target=5;
    int ans = Search1(arr,target);
    System.out.println(ans);
    }
    static int Search1(int[] arr,int target)
    {
      int start = 0; 
      int end =arr.length-1;
      while(start<=end)
      {
        int mid = start+(end-start)/2;

        if(target>arr[mid])
        {
            start=mid+1;

        }
        else if(target==arr[mid])
        {
            return arr[mid];
        }
        else{
            end = mid-1;
        }
      }
    return arr[start];
    }
}
