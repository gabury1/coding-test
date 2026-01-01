
def true_telling(idx) :
        global true_person
        true_candidate = party[idx] - true_person
        true_person.update(true_candidate)
        true_res = bt(idx-1)
        true_person = true_person - true_candidate
        return true_res

def lie_telling(idx) :
        global lie_person
        lie_candidate = party[idx] - lie_person
        lie_person.update(lie_candidate)
        lie_res = bt(idx-1)
        lie_person = lie_person - lie_candidate 
        return lie_res

def bt(idx) :
    """
    그룹에 거짓과 진실로 아는 사람이 섞여 있음. << 0으로 리턴
    그룹에 진실로 아는 사람이 있음 << 진실로 확정
    그룹에 거짓으로 아는 사람이 있음 << 거짓으로 확정
    아직은 선택할 여지가 있는, 무고한 사람만 있음 << true / false 선택
    """

    if idx < 0 : return 0
    global true_person, lie_person

    party_people = party[idx]
    lie_knower = party_people & lie_person
    true_knower = party_people & true_person

    if 0 < len(lie_knower) and 0 < len(true_knower) :
           return -9999
    elif 0 < len(lie_knower) :
           return lie_telling(idx) + 1
    elif 0 < len(true_knower) :
            return true_telling(idx)
    else :
           return max(true_telling(idx), lie_telling(idx)+1)


N, M = map(int, input().split()) 
true_person = set(list(map(int, input().split()))[1:]) # 진실 아는 사람들
lie_person = set() # 구라로 아는 사람들
party = [set(list(map(int, input().split()))[1:]) for _ in range(M)]

print(bt(M-1))

"""
    그룹에 진실로 아는 사람이 있음 << 진실로 확정
    그룹에 거짓으로 아는 사람이 있음 << 거짓으로 확정
    그룹에 거짓과 진실로 아는 사람이 섞여 있음. << 0으로 리턴
    아직은 선택할 여지가 있는, 무고한 사람만 있음 << true / false 선택
"""

"""
10 9
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9
1 10
2 3 10
1 4

4 3
0
2 1 2
1 3
3 2 3 4
"""