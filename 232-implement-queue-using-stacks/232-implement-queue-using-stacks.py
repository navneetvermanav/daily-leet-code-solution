class MyQueue:

	def __init__(self): 
		self.queue_stack = list()

	def push(self, x: int) -> None:
		new_stack = [x]
		new_stack.extend(self.queue_stack)
		self.queue_stack = new_stack

	def pop(self) -> int:
		return self.queue_stack.pop(-1)  

	def peek(self) -> int:
		return self.queue_stack[-1]

	def empty(self) -> bool:
		return 0 == len(self.queue_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()