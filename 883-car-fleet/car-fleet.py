class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(map(list,zip(position,speed)))
        cars.sort(reverse=True)
        times=[]
        fleets=0
        last_time=0
        for i in range(len(cars)):
            time=(target-cars[i][0])/cars[i][1]
            if time>last_time:
                fleets+=1
                last_time=time
            else:
                continue
        return fleets
