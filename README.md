# expense-tracker-cli
<div align="center">
    <img src="https://socialify.git.ci/Trishan0/expense-tracker-cli/image?forks=1&issues=1&language=1&name=1&pulls=1&stargazers=1&theme=Auto" alt="expense Tracker CLI" width="640" height="320" />
</div>
<br><br>
<br>

<div align='center' style=" display: grid;">

  [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sanjanatrishan@gmail.com)
  [![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Trishan0)
  [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@trishan-fernando)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/trishan-fernando/)
</div>

---

# Expense Tracker CLI Project

This is a simple command-line-based Expense Tracker written in Python. It allows users to add, update, delete, and view expenses stored in a JSON file. The program also provides summary reports based on recorded expenses.

## Features

- Add new expenses with descriptions and amounts
- Update existing expenses
- Delete expenses
- List all recorded expenses
- Filter expenses by month
- Get a summary of total expenses
- View total expenses for a specific month


## Example Commands

Here are some example commands and their usage:

```bash
expenser add --description Lunch --amount 20
# Expense added with ID: 1

expenser list                               
# ID   Date         Description     Amount    
# ---------------------------------------------   
# 1    2025-02-23   Lucnh           $15.0      
# 2    2025-03-01   Dinner          $20.0     

expenser list --month 3
# Expenses for March
# ID   Date         Description     Amount    
# ---------------------------------------------
# 1    2025-03-01   Dinner          $20.0      

expenser summary 
# Total expenses: $35.0
    
expenser summary --month 2
# Total expenses for February: $15.0

expenser delete --id 1    
# Expense 1 deleted successfully

```


## Conclusion

This project offers an opportunity to improve your programming and CLI development skills. You can practice interacting with the filesystem, handling JSON data, and managing user input via the command line while building a useful expense-tracking tool.

Original Project Link: [Expense Tracker CLI](https://roadmap.sh/projects/expense-tracker)

---

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Trishan0/expense-tracker-cli.git
    cd expense-tracker-cli
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

### Usage

1. Run the Expense Tracker CLI:
    ```sh
    pip install -e .
    expense-tracker    
    ```

2. Follow the on-screen instructions to add, view, update, or delete expenses.

### Basic Commands

- **Add a expense**: 
    ```sh
    expenser add --description "expense description" --amount <amount>
    ```

- **View All expenses**: 
    ```sh
    expenser list
    ```
- **List Expenses for a Specific Month**;
    ```sh
    expenser list --month 2
    ```

- **View Summary all expenses**: 
    ```sh
    summary 
    ```
- **View Summary for a Specific Month**: 
    ```sh
    summary --month 2
    ```

- **Update a expense**: 
    ```sh
    expenser update --id 1 --description "New expense Description" --amount <new amount>
    ```

- **Delete a expense**: 
    ```sh
    expenser delete --id <expense_id>
    ```

- **Data Storage**: 

Expenses are stored in a JSON file named expense_list.json. The data structure follows this format:

```sh
{
  "expenses": [
    {
      "id": 1,
      "expense": "Lunch",
      "amount": 15.0,
      "date": "2025-02-23"
    }
  ]
}
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
