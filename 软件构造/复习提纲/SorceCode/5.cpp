#include<bits/stdc++.h>
using namespace std;
const int maxn = 1e4+100;
const int maxm = 1e5+100;
int first[maxn],des[maxm],nxt[maxm],d[maxm],tot=0;
int ans[maxn],now=0;
int m,n;
inline void addEdge(int x,int y){
	des[++tot] = y;
	nxt[tot] = first[x];
	first[x] = tot;
	d[y]++;
}
int main(){
	//n个点，m条单向边，无环。 
	scanf("%d%d",&n,&m);
	for (int i=0;i<m;i++){
		int u,v;
		scanf("%d%d",&u,&v);
		addEdge(v,u);
	}
	queue<int> Q;
	for (int i=1;i<=n;i++){
		if (!d[i])Q.push(i);
	}
	while (!Q.empty()){
		int q = Q.front();Q.pop();
		ans[now++] = q;
		for (int t = first[q];t;t=nxt[t]){
			int v = des[t];
			d[v]--;
			if (!d[v])Q.push(v);
		}
	}
	for (int i=0;i<now;i++){
		printf("%d ",ans[i]);
	}
	return 0;
}
