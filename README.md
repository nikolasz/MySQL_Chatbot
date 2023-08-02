# MySQL Chatbot

This is a personal learning project titled 'MySQL Chatbot'. It's a program that leverages the GPT-4 model from OpenAI to generate parameterized SQL queries from natural language inputs.

The Python script `generate_mysql_query` takes in a database schema and a natural language query as inputs, and outputs a parameterized SQL query that can be used to get the information requested in the natural language query.

The script uses OpenAI's GPT-4 model to generate the SQL queries, so you'll need to provide your own OpenAI API key to use the script.

## Usage

Here's an example of how you might use the `generate_mysql_query` function:

```python
import json

# Define the database schema
schema = {
    "tables": [
        {
            "name": "InvestmentAccounts",
            "columns": [
                {"name": "client_id", "type": "INTEGER", "is_primary_key": True},
                {"name": "balance", "type": "INTEGER"}
            ]
        },
        {
            "name": "Advisors",
            "columns": [
                {"name": "advisor_id", "type": "INTEGER", "is_primary_key": True},
                {"name": "first_name", "type": "TEXT"},
                {"name": "last_name", "type": "TEXT"}
            ]
        },
        {
            "name": "Client_Advisor",
            "columns": [
                {"name": "client_id", "type": "INTEGER", "is_primary_key": True},
                {"name": "advisor_id", "type": "INTEGER", "is_primary_key": True}
            ]
        }
    ]
}

# Define the natural language query
query = "Generate a parameterized SQL query to find the total asset value for a given advisor, where the advisor's first and last names are parameters. The advisor's name is Nikolas Zeigler."

# Generate the SQL query
sql_query = generate_mysql_query(schema, query)

print(sql_query)

# Adjust schema and query to fit your needs
```

Requirements
To run this project, you'll need:

Python 3
An OpenAI API key
The openai Python package
The dotenv Python package