class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max_area = 0;

        while(left < right){
            int area = (right - left) * min(height[left], height[right]);
            if(area > max_area){
                max_area = area;
            }
            if(height[left] > height[right]){
                right -= 1;
            }else{
                left += 1;
            }
        }
        return max_area;
    }
};
