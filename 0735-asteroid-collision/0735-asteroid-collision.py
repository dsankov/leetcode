class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        orbit = deque()
        for asteroid in asteroids:
            if asteroid >= 0: 
                orbit.append(asteroid)
            else:
                while orbit:
                    last_seen = orbit[-1]
                    if last_seen < 0:
                        orbit.append(asteroid)
                        break
                    else:
                        if abs(last_seen) < abs(asteroid):
                            orbit.pop()
                        elif abs(last_seen) > abs(asteroid):
                            break
                        else:
                            orbit.pop()
                            break
                else:
                    orbit.append(asteroid)
                

        return orbit