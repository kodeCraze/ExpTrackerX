# ExpTrackerX

Budget Tracker App
The Budget Tracker App is a Python-based application that helps users manage their finances by tracking income, expenses, and budgets. It provides features for adding income and expenses, setting budgets, generating expense reports, visualizing spending, and optimizing budgets.
Features
Add Income: Users can add income amounts to their budget.
Add Expense: Users can add expenses by specifying the category and amount.
Set Budget: Users can set budgets for specific categories.
Generate Expense Report: Users can generate a report of their total expenses.
Visualize Spending: Users can visualize their spending breakdown by category using a bar chart.
Optimize Budget: The app automatically optimizes the budget by adjusting expenses to ensure that the total expenses do not exceed the remaining balance.
Requirements
Python 3.x
Seaborn library
Matplotlib library
Pandas library
Installation
Install Python: If you haven't already, download and install Python from the official website: https://www.python.org/downloads/
Install Required Libraries: Open a terminal or command prompt and run the following commands to install the required libraries:
bash
pip install seaborn
pip install matplotlib
pip install pandas

Download the Code: Download the Budget Tracker app code from the provided source.
Usage
Run the Code: Open a terminal or command prompt, navigate to the directory where you saved the Budget Tracker app code, and run the following command:
bash
python budget_tracker.py

Follow the Prompts: The app will display a menu with options to add income, add expenses, set budgets, generate expense reports, visualize spending, optimize budgets, and exit. Follow the prompts and enter the required information.
Visualize Spending: After adding income, expenses, and budgets, you can visualize your spending breakdown by selecting the "Visualize Spending" option from the menu. A bar chart will be displayed showing the expenses by category.
Optimize Budget: If your expenses exceed your remaining balance, you can optimize your budget by selecting the "Optimize Budget" option from the menu. The app will automatically adjust the expenses to ensure that the total expenses do not exceed the remaining balance.
Exit: To exit the app, select the "Exit" option from the menu.
Example Usage
1. Add income
2. Add expense
3. Set budget
4. Generate expense report
5. Visualize spending
6. Optimize budget
7. Exit
Enter your choice: 1
Enter income amount: 1000

1. Add income
2. Add expense
3. Set budget
4. Generate expense report
5. Visualize spending
6. Optimize budget
7. Exit
Enter your choice: 2
Enter category: Rent
Enter expense amount: 500

1. Add income
2. Add expense
3. Set budget
4. Generate expense report
5. Visualize spending
6. Optimize budget
7. Exit
Enter your choice: 3
Enter category: Entertainment
Enter budget amount: 100

1. Add income
2. Add expense
3. Set budget
4. Generate expense report
5. Visualize spending
6. Optimize budget
7. Exit
Enter your choice: 5

[A bar chart is displayed showing the spending breakdown by category]

1. Add income
2. Add expense
3. Set budget
4. Generate expense report
5. Visualize spending
6. Optimize budget
7. Exit
Enter your choice: 6

Optimized Expenses: {'Rent': 500, 'Entertainment': 100}

Final Balance: 400.0
Final Expenses: {'Rent': 500, 'Entertainment': 100}
Final Income: 1000

Contributing
If you find any issues or have suggestions for improvements, feel free to create a new issue or submit a pull request on the project's GitHub repository.
License
This project is licensed under the MIT License.
