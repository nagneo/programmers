def solution(id_list, report, k):
    reportedMap = {id : set() for id in id_list}
    
    for rep in report:
        splits = rep.split()
        reporter = splits[0]
        reported = splits[1]
        reportedMap[reported].add(reporter)
    
    answerMap = {id : 0 for id in id_list}
    for reporteds in reportedMap.values():
        if len(reporteds) < k:
            continue
        
        for reported in reporteds:
            if reported in answerMap:
                answerMap[reported] += 1
        
    return list(answerMap.values())


#print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))