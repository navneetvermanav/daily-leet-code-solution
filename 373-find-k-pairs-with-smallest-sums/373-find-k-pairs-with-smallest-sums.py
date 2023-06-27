class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(min(len(nums1), k)):
            # tuple of (sum of nums1[i] + nums2[0], nums1[i], nums2[0], index of nums2 start = 0)
            heappush(minHeap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))

        ans = []
        while k > 0 and minHeap:
            _, u, v, i = heappop(minHeap)
            ans.append([u, v])
            if i + 1 < len(nums2):
                newSum = u + nums2[i + 1]
                heappush(minHeap, (newSum, u, nums2[i + 1], i + 1))
            k -= 1
        return ans
