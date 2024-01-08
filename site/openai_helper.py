from openai import OpenAI

def get_openai_response(problem_text, solution_text):
    client = OpenAI(
        # This is the default and can be omitted
        api_key="API_KEY",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": '''
                    You will act as a venture capitalist agent. This agent will analyze solution's to given problems.
                    Both the problem and solution are related to environmental circular economy practices, meaning upcycling and being sustainable.

                    Provide an evaluation for the solution and rank it from 1 to 5 in these 4 categories:
                    economically stability, technologically advanced, feasiblity, and circular economy principals

                    You will respond to in the following format:
                    Economically Stability: {'number'}
                    Technologically Advanced: {'number'}
                    Feasiblity: {'number'}
                    Circular Economy Principles: {'number'}

                    Feedback: {solutions's positives and negatives}

                    Make sure your output as an agent follows the format listed above and replaces the numbers with values from 1-10
                    as well as feedback about the solution
                '''
            },
            {
                "role": "user",
                "content": f"Problem: {problem_text}. Solution: {solution_text}",
            }
        ],
        model="gpt-3.5-turbo",
    )

    response_content = chat_completion.choices[0].message.content
    return response_content
