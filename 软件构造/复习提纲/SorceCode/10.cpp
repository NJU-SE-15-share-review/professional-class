#include<bits/stdc++.h>
using namespace std;
const int maxn = 1e5+10;
int n,N;
int a[maxn];
bool can[maxn];
int x,y;
int main(){
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		scanf("%d",a+i);
	}
	scanf("%d%d",&x,&y);
	sort(a,a+n);
	can[0] =0;
	N = max(x,y);
	for (int i=0;i<N;i++){
		if (can[i]){
			for (int j = 0;j<n&&i+a[j]<=N;j++){
				can[i+a[j]]=1;
			}
		}
	}
	printf("%d\n",!(can[x]&&can[y]));
	return 0; 
} 
