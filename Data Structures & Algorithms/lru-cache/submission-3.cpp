class LRUCache {
private:
    struct ListNode{
        ListNode * next;
        ListNode * prev;
        int key;
        int value;
        ListNode(){
            next=nullptr;
            prev=nullptr;
            key=-1;
            value=-1;
        }
        ListNode(int key_,int value_){
            next=nullptr;
            prev=nullptr;
            key=key_;
            value=value_;
        }
    };
    int capacity_;

    ListNode * head;
    ListNode * tail;
    unordered_map<int,ListNode *> m;
public:
    LRUCache(int capacity) {
        head=new ListNode();
        tail=new ListNode();
        head->next=tail;
        tail->prev=head;
        capacity_=capacity;
    }
    
    int get(int key) {
        if (m.find(key)==m.end()){
            return -1;
        }
        ListNode * n=m[key];
        n->prev->next=n->next;
        n->next->prev=n->prev;

        n->next=head->next;
        n->next->prev=n;
        n->prev=head;
        head->next=n;

        return m[key]->value;
    }
    
    void put(int key, int value) {
        //find the key then update it and the value 
        if (m.find(key)!=m.end()){
            m[key]->value=value;
            ListNode * n=m[key];
            n->prev->next=n->next;
            n->next->prev=n->prev;

            n->next=head->next;
            n->next->prev=n;
            n->prev=head;
            head->next=n;
            return ;
        }
        if (m.size()==capacity_){
            ListNode * n=tail->prev;
            n->prev->next=tail;
            tail->prev=n->prev;
            int k=n->key;
            delete n;
            m.erase(k);
        }
        ListNode* n=new ListNode(key,value);

        m[key]=n;
        n->next=head->next;
        n->next->prev=n;
        n->prev=head;
        head->next=n;

        return ;
    }
};
