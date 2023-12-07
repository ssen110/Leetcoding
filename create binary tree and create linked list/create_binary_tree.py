class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def create_tree(self, arr):
        root = TreeNode(int(arr[0]))
        i = 1
        node_arr = []
        temp_root = root
        while i < len(arr):
            left_val = arr[i]
            right_val = arr[i+1]
            temp_root.left = TreeNode(left_val)
            temp_root.right = TreeNode(right_val)
            if left_val:
                node_arr.append( temp_root.left)
            if right_val:
                node_arr.append(temp_root.right)

            temp_root = node_arr.pop(0)
            i += 2
        return root


if __name__ == "__main__":
    arr = [50,  None, 54, 98, 6,  None, None,  None, 34]
    root = BinaryTree().create_tree(arr)
    temp = 0