import math

class KnightSitting:
    def circular_case(self, N):
        lower_knight_count = math.ceil(N/3)
        upper_knight_count = math.floor(N/2)

        seat_combinations = [math.comb(k, N-2*k) * math.factorial(k-1) for k in range(lower_knight_count, upper_knight_count+1)]

        seat_combinations_sum = sum(seat_combinations)

        average_empty_seats = 0

        for knight in range(lower_knight_count, upper_knight_count+1):
            average_empty_seats += seat_combinations[knight-lower_knight_count] * (N-knight)/(N*seat_combinations_sum)

        return average_empty_seats


# for i in range(1, 10):
#     print(f"{i}: {KnightSitting().circular_case(i)}")

print(KnightSitting().circular_case(100000))

print(KnightSitting().circular_case(100001))

