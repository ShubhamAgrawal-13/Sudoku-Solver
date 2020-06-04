#include<bits/stdc++.h>
#include <unistd.h>
using namespace std;

#define N 9

// int dx[]={-1,-1,-1,0,0,1,1,1};
// int dy[]={-1,0,1,-1,1,-1,0,1};

bool is_thik(char a[][N], int n,int r,int c,char choice)
{
	for(int i=0;i<n;i++)
	{
		if(a[i][c]==choice)
			return false;
	}
	for(int i=0;i<n;i++)
	{
		if(a[r][i]==choice)
			return false;
	}

	int block_r=r%3;
	int block_c=c%3;
	int pr=0;
	int qr=0;

	if(block_r==0 && block_c==0)
	{
		pr=r;
		qr=c;
	}
	

	else if(block_r==0 && block_c==1)
	{
		pr=r;
		qr=c-1;
	}

	else if(block_r==0 && block_c==2)
	{
		pr=r;
		qr=c-2;
	}

	else if(block_r==1 && block_c==0)
	{
		pr=r-1;
		qr=c;
	}

	else if(block_r==1 && block_c==1)
	{
		pr=r-1;
		qr=c-1;
	}

	else if(block_r==1 && block_c==2)
	{
		pr=r-1;
		qr=c-2;
	}

	else if(block_r==2 && block_c==0)
	{
		pr=r-2;
		qr=c;
	}

	else if(block_r==2 && block_c==1)
	{
		pr=r-2;
		qr=c-1;
	}

	else if(block_r==2 && block_c==2)
	{
		pr=r-2;
		qr=c-2;
	}

	for(int p=pr;p<pr+3;p++)
	{
		for(int q=qr;q<qr+3;q++)
		{
			if(a[p][q]==choice)
			{
				return false;
			}
		}
	}

	return true;
}

bool isSafe(int x,int y,int n)
{
	if(x>=0 && x<n && y>=0 && y<n)
	{
		return true;
	}
	return false;
}

void print(char a[][N],int n)
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			cout<<a[i][j]<<" ";
		}
		cout<<endl;
	}
	cout<<"--------------------------------------------\n";
}

bool check(char a[][N],int n,int& x,int& y)
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(a[i][j]=='.')
			{
				x=i;
				y=j;
				return true;
			}
		}
	}
	x=-1;
	y=-1;
	return false;
}


void solve(char a[][N], int n)
{
	//int flag=0;
	//print(a,n);
	int i,j;
	if(check(a,n,i,j))
	{
		for(char choice='1';choice<='9';choice++)
		{
			if(is_thik(a,n,i,j,choice))
			{
				a[i][j]=choice;
				solve(a,n);
				a[i][j]='.';	
			}
		}
	}
	else
	{
		print(a,n);
	}
}
// int i = pos / 9;
// int j = pos % 9;
int main()
{
	int n=N;
	char a[][N]={{'5','3','.','.','7','.','.','.','.'}, {'6','.','.','1','9','5','.','.','.'}, {'.','9','8','.','.','.','.','6','.'}, {'8','.','.','.','6','.','.','.','3'}, {'4','.','.','8','.','3','.','.','1'}, {'7','.','.','.','2','.','.','.','6'}, {'.','6','.','.','.','.','2','8','.'}, {'.','.','.','4','1','9','.','.','5'}, {'.','.','.','.','8','.','.','7','9'}};
	solve(a,n);
	print(a,n);
	return 0;
}