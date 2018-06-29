#include<bits/stdc++.h>
using namespace std; 
const int maxn = 8+5;
bool row[maxn];
bool line2[maxn*2];
bool line3[maxn*2];
bool mp[maxn][maxn];
int tot=0;
void print(){
	printf("map %d:\n",++tot);
	for (int i=0;i<8;i++){
		for (int j=0;j<8;j++){
			printf("%d ",mp[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}
void solve(int depth){
	if (depth==8){
		print();
		return;
	}
	for (int i=0;i<8;i++){
		if (row[i]||line2[depth+i]||line3[8+i-depth])continue;
		row[i]=line2[depth+i]=line3[8+i-depth]=1;
		mp[depth][i] =1;
		solve(depth+1);
		mp[depth][i] = 0;
		row[i]=line2[depth+i]=line3[8+i-depth]=0;
	}
}
int main(){
	solve(0);
	return 0;
}
