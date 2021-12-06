class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def countListNodes(self, head):
        count = 0

        temp = head

        while temp:
            temp = temp.next
            count +=1

        return count        


    def sortedListToBST(self, head):

        n = self.countListNodes(head)

        def helper(n):
            nonlocal head

            if n <= 0:
                return None
            
            # in order traversal
            left = helper(n//2)
            root = TreeNode(head.val)
            root.left = left

            head = head.next

            root.right = helper( n- n//2 -1) #  n//2 for left, -1 for root

            return root

        return helper(n)

# push reversly
def push(head, new_val):
    node = ListNode(new_val)

    node.next = head

    head = node

    return head

def print_list(head):
    while head:
        print(head.val, end= " ")
        head = head.next
    print()

def preorder_bst(root):
    if not root:
        return
    print(root.val)
    preorder_bst(root.left)
    preorder_bst(root.right)


if __name__ == "__main__":
    head = None

    head = push(head, 7)
    head = push(head, 6)
    head = push(head, 5)
    head = push(head, 4)
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)

    print_list(head)
    s = Solution()
    preorder_bst(s.sortedListToBST(head))


