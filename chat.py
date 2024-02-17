from openai import OpenAI

import webbrowser
import markdown

client = OpenAI(
    api_key='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',
)

dataset_description = """
CustomerID,Name,Email,ProductPurchased,PurchaseAmount,Date
1,John Doe,johndoe@email.com,Product A,150.50,2023-02-01
2,Jane Smith,janesmith@email.com,Product B,99.99,2023-02-03
3,Bob Johnson,bobjohnson@email.com,Product C,200.00,2023-02-05
4,Alice Brown,alicebrown@email.com,Product A,120.75,2023-02-07
5,Chris Lee,chrislee@email.com,Product B,80.00,2023-02-10
6,Emma White,emmawhite@email.com,Product C,180.25,2023-02-12
7,David Miller,davidmiller@email.com,Product A,90.99,2023-02-15
8,Grace Turner,graceturner@email.com,Product B,110.50,2023-02-18
9,Sam Taylor,samtaylor@email.com,Product C,250.00,2023-02-20
10,Olivia Wilson,oliviawilson@email.com,Product A,130.20,2023-02-23
"""

# Prompt for ChatGPT
prompt = f"Write a detailed report on marketing campaign performance: \n'{dataset_description}'\n Use markdown."


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
)



file_path = 'index.html'

content = chat_completion.choices[0].message.content
html = markdown.markdown(content)

with open(file_path, 'w', encoding='utf-8') as html_file:
    html_file.write(html)

webbrowser.open_new_tab(file_path)
