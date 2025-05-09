class NumberAscOrder:
    def sort(self, stack):
        if stack.is_empty():
            return []

        numbers = []
        while not stack.is_empty():
            numbers.append(stack.pop())

        return sorted(numbers)
