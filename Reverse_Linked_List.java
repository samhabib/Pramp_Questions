  public static LinkedListNode reverse(LinkedListNode headOfList) {
    LinkedListNode currentNode = headOfList;
    LinkedListNode previousNode = null;
    LinkedListNode nextNode = null;

    while (currentNode != null) {

        nextNode = currentNode.next;

        currentNode.next = previousNode;
        
        previousNode = currentNode;
        currentNode = nextNode;
    }

    return previousNode;
}
