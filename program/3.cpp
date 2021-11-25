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

int findNumberIn2DArray(const vector<vector<int>> &mat, int target) {
    int n = mat.size();
    int m = mat[0].size();

    int x = 0, y = m-1;
    // solution 1
    // while (true) {
    //     if (x >= n || y < 0) {
    //         return 0;
    //     }
    //     if (mat[x][y] == target) {
    //         return 1;
    //     }
    //     if (mat[x][y] > target) {
    //         y--;
    //     }
    //     if (mat[x][y] < target) {
    //         x++;
    //     }
    // }

    // solution 2
    int mark = 0;
    while (true) {
        if (mark == 0) {
            int pos = lower_bound(mat[x].begin(), mat[x].begin() + y + 1, target) - mat[x].begin();
            if (pos < m && mat[x][pos] == target) return 1;
            if (pos == 0) return 0;
            y = pos - 1;
        }else {
            int l = x, r = n-1;
            while (l <= r) {
                int _m = mid;
                if (mat[_m][y] == target) return 1;
                else if (mat[_m][y] < target) {
                    l = _m + 1;
                }else {
                    r = _m - 1;
                }
            }
            if (l >= n) return 0;
            x = l;
        }
        mark = 1 - mark;
    }
}


int main() {
    ios::sync_with_stdio(false);
    int tcase;

    // ifstream file;
    // file.open("../test/data/3.txt");
    // file >> tcase;
    cin >> tcase;
    // cout << tcase << endl;

    for (int _i = 0 ; _i < tcase; _i++) {
        int n, m, target;
        cin >> n >> m >> target;
        // file >> n >> m >> target;
        vector<vector<int>> mat(n, vector<int>(m, 0)); 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> mat[i][j];
                // file >> mat[i][j];
            }
        }

        cout << findNumberIn2DArray(mat, target) << endl;
    }
    // file.close();
    return 0;
}