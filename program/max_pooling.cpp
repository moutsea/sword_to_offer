#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include "time.h"
#include <functional>
#include <fstream>
#include <codecvt>
#define rep(i,a,b) for (int i=a; i<b; i++)
#define Rep(i,a,b) for (int i=a; i>b; i--)
#define foreach(e,x) for (__typeof(x.begin()) e=x.begin();e!=x.end();e++)
#define mid ((l+r)>>1)
#define lson (k<<1)
#define rson (k<<1|1)
#define MEM(a,x) memset(a,x,sizeof a)
#define L ch[r][0]
#define R ch[r][1]
#define pii pair<int, int>
#define LL long long 
using namespace std;
const int N=500005;
const long long Mod=99997867;

void get_max_pooling(int n, int k, vector<int> &nums, vector<int>& ans) {
    deque<int> dque;
    for (int i = 0; i < k-1; i++) {
        int u = nums[i];
        while (!dque.empty() && u > nums[dque.back()]) {
            dque.pop_back();
        }
        dque.push_back(i);
    }
    for (int i = k-1; i < n; i++) {
        int u = nums[i];
        while (!dque.empty() && i - dque.front() >= k) {
            dque.pop_front();
        }
        while (!dque.empty() && (u > nums[dque.back()] || i - dque.back() >= k)) {
            dque.pop_back();
        }
        dque.push_back(i);
        ans.push_back(nums[dque.front()]);
    }
}

int main() {
    ios::sync_with_stdio(false);
    int tcases;
    cin >> tcases;
    for (int _i = 0; _i < tcases; _i++) {
        int n, k;
        cin >> n >> k;
        vector<int> arr;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            arr.push_back(x);
        }
        vector<int> res;
        get_max_pooling(n, k, arr, res);
        for (auto x: res) {
            cout << x << " ";
        }
        cout << endl;
    }
}