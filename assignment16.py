# Given list of employee names
employees = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ian", "Jack"]

# Step 1: Split the list into two sublists
subList1 = employees[:5]  # First 5 names
subList2 = employees[5:]  # Last 5 names

# Step 2: Adding a new employee "Kriti Brown" to subList2
subList2.append("Kriti Brown")  

# Step 3: Remove the second employee from subList1
# List index starts from 0, so index 1 corresponds to the second employee
subList1.pop(1)  # Removes "Bob" from subList1

# Step 4: Merge both lists
mergedList = subList1 + subList2  # Concatenation of two lists

# Step 5: Salary List (Assuming 10 salaries, one for each original employee)
salaryList = [50000, 60000, 55000, 62000, 48000, 53000, 75000, 72000, 58000, 65000]

# Updating salaries with a 4% increase
salaryList = [int(salary * 1.04) for salary in salaryList]  # Apply 4% increase to each salary

# Step 6: Sorting salaries in descending order and getting the top 3 salaries
salaryList.sort(reverse=True)  # Sorting in descending order
top_3_salaries = salaryList[:3]  # Extracting the top 3 salaries

# Output results
print("Merged Employee List:", mergedList)
print("Updated Salary List:", salaryList)
print("Top 3 Salaries:", top_3_salaries)
