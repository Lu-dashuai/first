class Node:
    """每一个节点对象"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList:
    """单链表"""

    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断是否为空"""
        return self.__head is None

    def length(self):
        """判断长度"""
        count = 0
        bo = True
        while bo:
            if self.__head is None:
                bo = False
            else:
                count = count + 1
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = Node(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self.__head
        # 将链表的头_head指向新节点
        self.__head = node


if __name__ == '__main__':
    sll = SingleLinkList()
    sll.add(100)
    sll.add(200)
    sll.add(300)

    sll.travel()
