#include<iostream>
#include<cstdio> 
using namespace std;
const int maxn = 1e5+100;
char s1[maxn],s2[maxn];
bool strcpy(const char* s1,const char* s2){
	//s1>=s2:true else:false 
	for (int i=0;s1[i];i++){
		if (s1[i]==s2[i])continue;
		return s1[i]<s2[i];
	}
	return true;
}
int main(){
	scanf("%s%s",s1,s2);
	cout<<strcpy(s1,s2)<<endl;
	return 0;
} 
