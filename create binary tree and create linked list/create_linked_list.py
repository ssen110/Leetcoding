class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Linkedlist:
    def create_linked_list(self, val_list):
        linkedlist = None
        for item in val_list[::-1]:
            node = ListNode(item)
            if linkedlist:
                node.next = linkedlist
                linkedlist = node
            else:
                linkedlist = node
        return linkedlist


if __name__ == "__main__":
    start = 0
    ll_test = Linkedlist().create_linked_list([1, 2, 3, 4, 5])
    end = 0