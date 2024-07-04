def solution(S):
    N = len(S)
    patches = 0
    i = 0
    
    while i < N:
        if S[i] == 'X':
            # We encounter a pothole, so we need to apply a patch
            patches += 1
            # Skip the next two segments after applying the patch
            i += 3
        else:
            # Move to the next segment
            i += 1
            
    return patches

# Examples
print(solution(".X..X"))          
print(solution("X.XXXXX.X."))     
print(solution("XX.XXX.."))       
print(solution("XXXX"))