#include <stdio.h>
#include <stdlib.h>
#define Count_Vertice 6
#define Far_Distance 2000

int W[Count_Vertice][Count_Vertice] = {
// W[i][j]는 i에서 j까지의 직행거리, Far_distance란 큰 수는 바로 갈 수 없는 경우를 표시
        {0, Far_Distance, 2, 3, 3, 6},
        {Far_Distance, 0, Far_Distance, 4, 2, Far_Distance},
        {10, 2, 0, 5, 1, Far_Distance},
        {Far_Distance, Far_Distance, 4, 0, Far_Distance, 2},
        {5, 9, Far_Distance, 4, 0, 3},
        {Far_Distance, Far_Distance, Far_Distance, 4, Far_Distance, 0},
};

int D[Count_Vertice][Count_Vertice];	// D[i][j]는 i에서 j까지 가는 최소 거리를 저장
int P[Count_Vertice][Count_Vertice];	// P[i][j]는 i에서 j까지 가는 데 거치는 최고 차수 정점을 저장 

void Floyd(){
    int i, j, k;
    for(i=0; i < Count_Vertice; i++)	// 배열 초기화
        for(j=0; j < Count_Vertice; j++){
            P[i][j] = -1;
            D[i][j] = W[i][j];
        }

    for(k=0; k < Count_Vertice; k++)
        for(i=0; i < Count_Vertice; i++)
            for(j=0; j < Count_Vertice; j++)
                if(D[i][j] > D[i][k] + D[k][j]){
                    /* k를 거칠 시 D[i][j]가 더 짧아지는 경우 */
                    D[i][j] = D[i][k] + D[k][j];
                    P[i][j] = k;
                }
}

void Print_Path(int a, int b){		// Print_Path[i][j]에서 i와 j는 출력하지 않음을 주의
    if(P[a][b] != -1)	{	// P[a][b] = -1  "="  a에서 바로 b로 가는 것이 최단거리
        Print_Path(a, P[a][b]);
        printf("%d ", P[a][b]);
        Print_Path(P[a][b], b);
    }
}

int main(){
    Floyd();
    int a, b;
    printf("출발점과 도착점을 입력하시오. (0 ~ %d)\n", Count_Vertice - 1);
    scanf("%d %d", &a, &b);
    printf("최단거리 : %d\n", D[a][b]);
    printf("최단경로 : ");
    printf("%d ", a);	Print_Path(a, b);
    if(D[a][b] != 0)	printf("%d", b);	// D[a][b] = 0  "="  a = b
    return 0;

}