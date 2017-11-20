#include<bits/stdc++.h>
using namespace std;
const int maxn = 1e5+100;
string s[maxn];
int n;
int depth =0;
void solve(int &depth,int x){
//	cout<<endl<<depth<<" "<<x<<endl;
	if (s[depth]=="pair"){
		cout<<"pair<";
		solve(++depth,2);
	}else{
		cout<<s[depth];
	}
	if (x==2)cout<<",",solve(++depth,x-1);
	else cout<<">";
}
int main(){
	while (cin>>s[n++]);
	solve(depth,0);
	return 0;
}
