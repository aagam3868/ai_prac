# # class MonkeyBananaProblem:
# #     def __init__(self):
# #         self.monkey_position = 'ground'
# #         self.banana_position = 'ceiling'
# #         self.has_banana = False
# #         self.box_position = 'ground'

# #     def climb_box(self):
# #         if self.monkey_position == 'on box':
# #             print("Monkey is already on the box.")
# #         elif self.box_position == 'under banana':
# #             self.monkey_position = 'on box'
# #             print("Monkey climbs onto the box.")
# #         else:
# #             print("Monkey can't climb until the box is under the bananas.")

# #     def move_box_under_banana(self):
# #         if self.box_position == 'under banana':
# #             print("Box is already under the bananas.")
# #         else:
# #             self.box_position = 'under banana'
# #             print("Monkey moves the box under the bananas.")

# #     def grab_banana(self):
# #         if self.monkey_position == 'on box' and self.box_position == 'under banana':
# #             self.has_banana = True
# #             print("Monkey grabs the bananas!")
# #         else:
# #             print("Monkey can't reach the bananas yet.")

# #     def solve(self):
# #         print("Starting Monkey Banana Problem solution...")
# #         self.move_box_under_banana()
# #         self.climb_box()
# #         self.grab_banana()
# #         if self.has_banana:
# #             print("Success! The monkey got the bananas.")
# #         else:
# #             print("Failed. The monkey couldn't get the bananas.")


# # # Run the hard-coded solution
# # problem = MonkeyBananaProblem()
# # problem.solve()






# class MonkeyBananaProblemUser:
#     def __init__(self):
#         self.monkey_position = 'ground'
#         self.banana_position = 'ceiling'
#         self.has_banana = False
#         self.box_position = 'ground'

#     def climb_box(self):
#         if self.monkey_position == 'on box':
#             print("Monkey is already on the box.")
#         elif self.box_position == 'under banana':
#             self.monkey_position = 'on box'
#             print("Monkey climbs onto the box.")
#         else:
#             print("Monkey can't climb until the box is under the bananas.")

#     def move_box_under_banana(self):
#         if self.box_position == 'under banana':
#             print("Box is already under the bananas.")
#         else:
#             self.box_position = 'under banana'
#             print("Monkey moves the box under the bananas.")

#     def grab_banana(self):
#         if self.monkey_position == 'on box' and self.box_position == 'under banana':
#             self.has_banana = True
#             print("Monkey grabs the bananas!")
#         else:
#             print("Monkey can't reach the bananas yet.")

#     def solve(self):
#         print("Monkey Banana Problem: Interactive Solution")
#         print("Actions: 'move_box', 'climb_box', 'grab_banana'")
        
#         while not self.has_banana:
#             action = input("Enter action (move_box, climb_box, grab_banana): ").strip().lower()
#             if action == 'move_box':
#                 self.move_box_under_banana()
#             elif action == 'climb_box':
#                 self.climb_box()
#             elif action == 'grab_banana':
#                 self.grab_banana()
#             else:
#                 print("Invalid action. Please try again.")

#             if self.has_banana:
#                 print("Success! The monkey got the bananas.")
#                 break


# # Run the user-input solution
# problem_user = MonkeyBananaProblemUser()
# problem_user.solve()







class MonkeyBananaProblem:
    def __init__(self, monkey_position, box_position, banana_position):
        self.monkey_position = monkey_position
        self.box_position = box_position
        self.banana_position = banana_position
        self.has_bananas = False
        self.monkey_on_box = False

    def move_monkey(self, new_position):
        self.monkey_position = new_position
        print(f"Monkey moved to {self.monkey_position}")

    def push_box(self, new_position):
        if self.monkey_position == self.box_position:
            self.box_position = new_position
            self.monkey_position = new_position
            print(f"Monkey pushed box to {self.box_position}")
        else:
            print("Monkey needs to be at the box's position to push it.")

    def climb_box(self):
        if self.monkey_position == self.box_position:
            self.monkey_on_box = True
            print("Monkey climbed on the box.")
        else:
            print("Monkey needs to be at the box's position to climb.")

    def grab_bananas(self):
        if self.monkey_on_box and self.box_position == self.banana_position:
            self.has_bananas = True
            print("Monkey grabbed the bananas!")
        else:
            print("Monkey needs to be on the box under the bananas to grab them.")

    def check_goal(self):
        return self.has_bananas

def solve_monkey_banana():
    # Initial positions of the monkey, box, and bananas
    monkey_position = (0, 0)
    box_position = (1, 0)
    banana_position = (2, 1)
    
    problem = MonkeyBananaProblem(monkey_position, box_position, banana_position)

    # Solving steps
    problem.move_monkey((1, 0))   # Move to the box
    problem.push_box((2, 1))      # Push the box under the bananas
    problem.climb_box()           # Climb on the box
    problem.grab_bananas()        # Grab the bananas
    
    if problem.check_goal():
        print("Success: The monkey has the bananas!")
    else:
        print("The monkey doesn't have the bananas.")

if __name__ == "__main__":
    solve_monkey_banana()
