class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort_car = []
        for i in range(len(position)):
            sort_car.append((position[i], speed[i]))
        sort_car.sort()
        fleets = len(position)

        fleet_pos = sort_car[-1][0]
        fleet_speed = sort_car[-1][1]

        for i in range(len(sort_car) - 2, -1, -1):
            pos = sort_car[i][0]
            speed = sort_car[i][1]


            if (target - pos) / speed <= (target - fleet_pos) / fleet_speed:
                fleets -= 1
            else:
                fleet_pos = pos
                fleet_speed = speed

            

        return fleets