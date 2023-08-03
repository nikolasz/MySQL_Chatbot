#deprecated
import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_mysql_query(schema, query):
    schema_str = json.dumps(schema, indent=4)
    system_message = '''
    You are an SQL query generator. You only respond with SQL queries written in Python, and never as an assistant, and never using sentences or conversational English. Don't ever break character or provide explanations or excuses. Return only 'error' if there is any issue generating an SQL query from the prompt, elif valid prompt return valid script. Parameterize variables to be mindful of SQL security. Your task is to generate a parameterized SQL query based on the user's input and the provided database schema. The query should use placeholders for any variable parts, such as the names in a WHERE clause.''' + schema_str

    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": query}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.1,
        max_tokens=200
    )

    generate_mysql_query = response['choices'][0]['message']['content'].strip()

    return generate_mysql_query

schema = {
    "tables": [
        {
            "name": "InvestmentAccounts",
            "columns": [
                {
                    "name": "client_id",
                    "type": "INTEGER",
                    "is_primary_key": True
                },
                {
                    "name": "balance",
                    "type": "INTEGER"
                }
            ]
        },
        {
            "name": "Advisors",
            "columns": [
                {
                    "name": "advisor_id",
                    "type": "INTEGER",
                    "is_primary_key": True
                },
                {
                    "name": "first_name",
                    "type": "TEXT"
                },
                {
                    "name": "last_name",
                    "type": "TEXT"
                }
            ]
        },
        {
            "name": "Client_Advisor",
            "columns": [
                {
                    "name": "client_id",
                    "type": "INTEGER",
                    "is_primary_key": True
                },
                {
                    "name": "advisor_id",
                    "type": "INTEGER",
                    "is_primary_key": True
                }
            ]
        }
    ]
}

query = "Generate a parameterized SQL query to find the total asset value for a given advisor, where the advisor's first and last names are parameters. The advisors name is Nikolas Zeigler"
print(generate_mysql_query(schema, query))

# Output:
'''
advisor_first_name = "Nikolas"
advisor_last_name = "Zeigler"

sql_query = """
SELECT SUM(InvestmentAccounts.balance) as total_asset_value
FROM Advisors
JOIN Client_Advisor ON Advisors.advisor_id = Client_Advisor.advisor_id
JOIN InvestmentAccounts ON Client_Advisor.client_id = InvestmentAccounts.client_id
WHERE Advisors.first_name = ? AND Advisors.last_name = ?
"""

parameters = (advisor_first_name, advisor_last_name)
'''
