class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        tree_counts = {}
        max_fruits = 0
        left = 0

        for right in range(len(fruits)):
            cur_tree = fruits[right]
            tree_counts[cur_tree] = tree_counts.get(cur_tree, 0) + 1

            if len(tree_counts) > 2:
                left_tree = fruits[left]
                tree_counts[left_tree] -= 1
                if tree_counts[left_tree] == 0:
                    tree_counts.pop(left_tree)
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits