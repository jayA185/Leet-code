# Problem 1710: Maximum Units on a Truck

class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        # Sort by units per box in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        
        for boxes, units in boxTypes:
            if truckSize == 0:
                break
            
            take = min(boxes, truckSize)
            total_units += take * units
            truckSize -= take
        
        return total_units