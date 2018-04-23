---
title: Algorithm - paintHouse(cost)
category: algorithm
tags: python algorithm codefight dynamic-programming

---

## Problem

- 순서대로 배치된 집을 색칠하려고 한다. 
    - 방법은 총 3가지
    - 집마다 색칠할 때의 가격은 다르며, i 번째 집을 j 색으로 칠할 때의 가격은 `cost[i][j]`
    - 연속된 집은 같은 색으로 칠하면 안된다. 
- 모든 집을 칠할 수 있는 가장 적은 가격을 구해봅시다앙. 

## solution

### recursive version

```python
def paintHouses(cost):
    def paintHouseWithoutK(remaining_cost, k):
        if len(remaining_cost)==1:
            top_row = remaining_cost[0]
            if k==0:
                return min(top_row[1], top_row[2])
            elif k==1:
                return min(top_row[2], top_row[0])
            else:
                return min(top_row[1], top_row[0])
        else:
            top_row = remaining_cost[0]
            if k==-1:
                return min([top_row[0]+paintHouseWithoutK(remaining_cost[1:], 0),
                            top_row[1]+paintHouseWithoutK(remaining_cost[1:], 1), 
                            top_row[2]+paintHouseWithoutK(remaining_cost[1:], 2)])
            elif k==0:
                return min(top_row[1]+paintHouseWithoutK(remaining_cost[1:], 1), 
                           top_row[2]+paintHouseWithoutK(remaining_cost[1:], 2))
            elif k==1:
                return min(top_row[2]+paintHouseWithoutK(remaining_cost[1:], 2), 
                           top_row[0]+paintHouseWithoutK(remaining_cost[1:], 0))
            else:
                return min(top_row[1]+paintHouseWithoutK(remaining_cost[1:], 1), 
                           top_row[0]+paintHouseWithoutK(remaining_cost[1:], 0))
    return paintHouseWithoutK(cost, -1)
```

### iterative version 

```python
def paintHouses(cost):
    if len(cost)==1:
        return min(cost[0])
    else:
        from0 =0 
        from1 =0
        from2 =0
        for i in range(0, len(cost)):
            new_from0 = from0
            new_from1 = from1
            new_from2 = from2
            cur_row = cost[i]
            if from1+cur_row[0]<=from2+cur_row[0]:
                new_from0 = from1+cur_row[0]
            else:
                new_from0 = from2+cur_row[0]
                
            if from0+cur_row[1]<=from2+cur_row[1]:
                new_from1 = from0+cur_row[1]
            else:
                new_from1 = from2+cur_row[1]
                
            if from0+cur_row[2]<=from1+cur_row[2]:
                new_from2 = from0+cur_row[2]
            else:
                new_from2 = from1+cur_row[2]
            from0, from1, from2 = new_from0, new_from1, new_from2
        return min([from0, from1, from2])
```
