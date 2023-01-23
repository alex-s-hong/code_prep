'''
There are N patients (numbered from 0 to n-1) who want to visit the doctor. 
The doctor has S possible appointment slots, numbered from 1 to S. 
Each of the patients has two preferences. 
Patient K would like to visit the doctor during either slot A[k] or B[k]. 
The doctor can treat only one patient during each slot.
Is it possible to assign every patient to one of their preferred slots 
so that there will be at most one patient assigned to each slot?

No patent has two preferences for the same slot. i.e. A[i] != B[i]

n = number of patients, len(A) and len(B)
S = slots
'''

from collections import defaultdict

def find_slots(n:int, s:int, A:list, B:list):
    patient2slot = defaultdict(list)
    slot2patient = defaultdict(list)

    for patient, slots in enumerate(zip(A, B)):
        patient2slot[patient].append(slots[0])
        patient2slot[patient].append(slots[1])

        slot2patient[slots[0]].append(patient)
        slot2patient[slots[1]].append(patient)

    
    visited = set()

    def dfs (p, patient_set, slot_set):
        if p in visited:
            return
        visited.add(p)
        patient_set.add(p)
        for s in patient2slot[p]:
            slot_set.add(s)
            for pchild in slot2patient[s]:
                dfs(pchild, patient_set, slot_set)
        
    for p in range(n):
        if p not in visited:
            patient_set = set()
            slot_set = set()
            dfs(p, patient_set, slot_set)
            if len(patient_set) > len(slot_set):
                return False
    return True
