#pragma warning(disable:4786)//使命名长度不受限制  
#pragma comment(linker, "/STACK:102400000,102400000")//手工开栈 
#include <vector>  
#include <list>  
#include <map>  
#include <set>  
#include <deque>  
#include <queue>  
#include <stack>  
#include <bitset>   
#include <algorithm>  
#include <functional>  
#include <numeric>  
#include <utility>  
#include <complex>  
#include <sstream>  
#include <iostream>  
#include <iomanip>  
#include <cstdio>  
#include <cmath>  
#include <cstdlib>  
#include <cstring>  
#include <ctime>  
#include <cassert>  
using namespace std;  
#define lson 2*i    
#define rson 2*i+1    
#define LS l,mid,lson    
#define RS mid+1,r,rson    
#define UP(i,x,y) for(i=x;i<=y;i++)    
#define DOWN(i,x,y) for(i=x;i>=y;i--)    
#define MEM(a,x) memset(a,x,sizeof(a))    
#define W(a) while(a)    
#define gcd(a,b) __gcd(a,b)       
#define N 1000005    
#define MOD 1000000007    
#define INF 0x3f3f3f3f    
#define EXP 1e-8    
#define lowbit(x) (x&-x) 
typedef long long LL;
const int NNN=1000000009;  
const LL modd = 1e9 + 7;  
const double PI = acos(-1.0);  
const double E = exp(1);  
const double EPS=1e-8;   
inline int read(){
	char ch=getchar();int rre=0;
	while (ch<'0'||ch>'9')ch = getchar();
	while (ch>='0'&&ch<='9')rre = rre*10+ch-'0',ch = getchar();
	return rre;
} 
inline LL readLL(){
	char chLL = getchar();LL rreLL=0LL;
	while (chLL<'0'||chLL>'9')chLL = getchar();
	while (chLL>='0'&&chLL<='9')rreLL = 10*rreLL+chLL-'0',chLL = getchar();
	return rreLL;
}
