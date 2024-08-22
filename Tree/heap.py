class Heap:
    def __init__(self):
        self._data = []  # Initialize an empty list for the heap

    def isempty(self):
        return len(self._data) == 0

    def insert(self, e):
        self._data.append(e)  # Add the new element to the end
        self._heapify_up(len(self._data) - 1)  # Maintain heap property

    def max(self):
        if self.isempty():
            print('Heap is Empty')
            return None
        return self._data[0]  # The maximum element is at the root

    def deletemax(self):
        if self.isempty():
            print('Heap is Empty')
            return None
        
        max_element = self._data[0]
        # Move the last element to the root and remove the last element
        self._data[0] = self._data[-1]
        self._data.pop()
        
        if not self.isempty():
            self._heapify_down(0)  # Maintain heap property
        
        return max_element

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        # Bubble up the element if it's greater than its parent
        if index > 0 and self._data[index] > self._data[parent_index]:
            self._data[index], self._data[parent_index] = self._data[parent_index], self._data[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        if left_child < len(self._data) and self._data[left_child] > self._data[largest]:
            largest = left_child
        
        if right_child < len(self._data) and self._data[right_child] > self._data[largest]:
            largest = right_child
        
        if largest != index:
            self._data[index], self._data[largest] = self._data[largest], self._data[index]
            self._heapify_down(largest)

# Example usage
S = Heap()
S.insert(25)
S.insert(14)
S.insert(2)
S.insert(20)
S.insert(10)
S.insert(40)

print(S._data)           # Output: [40, 20, 25, 14, 10, 2]
print(S.deletemax())     # Output: 40
print(S._data)           # Output: [25, 20, 2, 14, 10]
print(S.deletemax())     # Output: 25
print(S._data)           # Output: [20, 14, 2, 10]
