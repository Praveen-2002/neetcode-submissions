class Solution {
    public Node copyRandomList(Node head) {
        if (head == null){
            return null;
        }
        var old_map = new HashMap<Node,Integer>();
        var temp = head;
        int ind = 0;
        while(temp != null){
            old_map.put(temp, ind);
            ind +=1;
            temp = temp.next;
        }

        var new_list = new Node(head.val);
        var res = new_list;
        var map = new HashMap<Integer, List<Node>>();
        var ind_map = new HashMap<Integer, Node>();
        var curr = 0;
        while(head != null){
            var new_node  = new Node(head.val);
            ind_map.put(curr,new_node);
            if(head.random != null && old_map.get(head.random) <= curr){
                new_node.random = ind_map.get(old_map.get(head.random));
            }
            else if(head.random != null && old_map.get(head.random) > curr){
                if(map.containsKey(old_map.get(head.random))){
                    map.get(old_map.get(head.random)).add(new_node);
                }
                else{
                    map.put(old_map.get(head.random), new ArrayList<Node>(List.of(new_node)));
                }
            }
            if(map.containsKey(curr)){
                for (Node n : map.get(curr)){
                    n.random = new_node;
                }
            }
            curr+=1;
            head = head.next;
            new_list.next = new_node;
            new_list = new_list.next;
        }
        return res.next;
    }
}
