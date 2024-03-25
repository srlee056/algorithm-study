def solution(routes):
    
    routes = sorted(routes)
    
    #print(routes)
    
    camera_counts = 1
    section = routes[0]
    for i in range(1, len(routes)):
        cur_route = routes[i]
        
        if section[1] >= cur_route[0]:
            section = [cur_route[0], min(section[1], cur_route[1])]
        else :
            camera_counts +=1
            section = cur_route
    
    #answer = 0
    return camera_counts