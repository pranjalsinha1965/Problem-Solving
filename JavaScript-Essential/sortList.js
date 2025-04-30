var reverseKGroup = function(head, k) {
    let len=1;
    let count =0;
    let counter =0;
    let dummy = new ListNode(0, head);
    let before = dummy;
    let prev = dummy;
    let node = head;
    let current = head;
    let next;
    while(current.next!==null){
        len++;
        current = current.next;
    }
    let swap = Math.floor(len/k);
    while(count < swap){
        for(let i=0; i<k; i++){
            next = node.next;
            node.next = prev;
            prev = node;
            node = next;
        }
        let temp = before.next;
        before.next = prev;
        temp.next = node;
        prev = temp;
        before = temp;
        count++;
    }
    return dummy.next;
};