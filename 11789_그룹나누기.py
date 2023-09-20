import sys; sys.stdin = open('11789_그룹나누기.txt')

def bfs(now):
    global cnt_member
    q = [now]
    members[now] = 1
    cnt_member += 1
    while q:        # 인큐 상황 : 인접 정점이 있고, 멤버상태가 1이 아니면
        now = q.pop()
        for next in range(1, N + 1):
            if adj_m[now][next] == 0:       # 연결 안되있으면
                continue
            if members[next] == 1:          # 이미 체크된상태이면
                continue
            q.append(next)          # 인큐하면 방첵
            members[next] = 1
            cnt_member += 1


T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    app_forms = list(map(int, input().split()))
    adj_m = [[0]*(N + 1) for _ in range(N + 1)]

    # 인접 행렬 만들기
    for i in range(M):
        adj_m[app_forms[2*i]][app_forms[2*i + 1]] = 1
        adj_m[app_forms[2 * i + 1]][app_forms[2 * i]] = 1

    cnt_group, cnt_member = 0, 0
    members = [0]*(N + 1)
    while cnt_member < N :        # 모든 학생이 다 고려될때 까지
        for i in range(1, N + 1):
            if members[i] == 1:     # 이미 체크 된건 거름
                continue
            bfs(i)
            break
        cnt_group += 1
    print(f'#{tc} {cnt_group}')