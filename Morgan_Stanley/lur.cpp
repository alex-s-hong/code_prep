#include <iostream>
#include <map>

int size;
list<int> lru;                              // MRU ... LRU
unordered_map<int, list<int>::iterator> mp; // key -> iterator
unordered_map<int, int> kv;                 // key -> value

LRUCache(int capacity) : size(capacity) {}
int get(int key) {
    if (kv.count(key) == 0) return -1;
    updateLRU(key);
    return kv[key];
}
void put(int key, int value) {
    if (kv.size() == size && kv.count(key) == 0)    //매칭되는 값이 없으면 한 개를 map에서 빼버려라
        evict();
    updateLRU(key);
    kv[key] = value;
}
void updateLRU(int key) {
    if (kv.count(key))  //그 key 가 있다면
        lru.erase(mp[key]); // 그 위치에 가서 지워라
    lru.push_front(key);    //맨 앞이 가장 나중
    mp[key] = lru.begin();  //iteration map 에 위치 저장
}
void evict() {
    mp.erase(lru.back());
    kv.erase(lru.back());
    lru.pop_back();
}