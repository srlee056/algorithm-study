def solution(dirs):
    
    directions = {'U':(0, 1), 'D':(0,-1), 'R':(1, 0), 'L':(-1, 0)}
    
    x, y = 0, 0
    visited_paths = set()
    count = 0
    for dir in dirs:
        dx, dy = directions[dir]
        nx, ny = x + dx, y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path = ((x,y), (nx, ny))
            opposite_path = ((nx, ny), (x, y))

            if path not in visited_paths and opposite_path not in visited_paths:
                visited_paths.add(path)
                count += 1

            x, y = nx, ny

        
    return count