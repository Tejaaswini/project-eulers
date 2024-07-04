def sum_of_multiples(limit, multiples):
    return sum(number for number in range(limit) if any(number % multiple == 0 for multiple in multiples))

if __name__ == "__main__":
    limit = 1000
    multiples = [3, 5]
    result = sum_of_multiples(limit, multiples)
    print(f"The sum of all the multiples of {multiples} below {limit} is: {result}")
