#include<cstdio>
#include<algorithm>
using namespace std;
const int maxn = 1e5+40;
int a[maxn];
int n;
void Qsort(int* a,int l,int r){
	int i =l,j=r,mid = a[l+r >>1];
	while (i<j){
		while (a[i]<mid)i++;
		while (a[j]>mid)j--;
		if (i<=j)swap(a[i++],a[j--]);
	}
	if (l<j)Qsort(a,l,j);
	if (i<r)Qsort(a,i,r);
}
int main(){
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		scanf("%d",a+i);
	}
	Qsort(a,0,n-1);
	for (int i=0;i<n;i++){
		printf("%d ",a[i]);
	}
}
