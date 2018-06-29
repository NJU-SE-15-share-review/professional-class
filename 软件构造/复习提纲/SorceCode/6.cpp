#include<bits/stdc++.h>
using namespace std;
struct Matrix{
	int a[2][2];
	Matrix operator * (Matrix m2){
		Matrix ans;
		memset(ans.a,0,sizeof ans.a);
		for (int i=0;i<2;i++){
			for (int j=0;j<2;j++){
				for (int k=0;k<2;k++){
					ans.a[i][j]+=a[i][k]*m2.a[k][j];
				}
			}
		}
		return ans;
	}
}x;
Matrix quick(Matrix ans,int y){
	if (y==1)return ans;
	if (y&1){
		return ans*quick(ans*ans,y/2);
	}else{
		return quick(ans*ans,y/2);
	}
}
int n;
int main(){
	scanf("%d",&n);
	if (n==1||n==2){
		cout<<1<<endl;
		return 0;
	} 
	x.a[0][0]=x.a[0][1]=x.a[1][0]=1;
	x.a[1][1]=0;
	x=quick(x,n-2);
	cout<<(x.a[0][0]+x.a[0][1])<<endl;
	return 0;
} 
