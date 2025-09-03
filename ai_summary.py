from openai import OpenAI

def summarise_text(text):
    client = OpenAI(
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        api_key= "sk-4933347d468145089fbb21aa2e1e5d3f",
    )
    response = client.chat.completions.create(
        model="qwen-max",
        
        messages=[
            {'role':'system',"content":
             '''
            You are a doctoral student with an academic background in Economics, Sociology, and Political Science. I will provide you with an academic journal article, and your task is to produce a systematic and in-depth summary of the article. The summary must comprehensively cover the following sections:
                1.	Research Question:
                •	Clearly identify the central research question the article seeks to answer.
                •	Explain why this question is significant within the broader academic discourse or real-world political and social contexts.
                •	Discuss the author’s motivation for addressing this question.
                2.	Literature Review:
                •	Provide an overview of how the study situates itself within the existing body of literature.
                •	Highlight the theories, concepts, or empirical studies that the author builds upon, critiques, or extends.
                •	Identify the gaps or limitations in the prior literature and explain how this article attempts to address or fill them.
                3.	Research Design and Methodology (with special emphasis):
                •	Describe in detail the data sources used in the study (e.g., survey data, experimental data, administrative records, geographic datasets, social media data, etc.).
                •	Explain the overall research design (e.g., natural experiment, quasi-experiment, regression discontinuity design, difference-in-differences, case study, mixed-methods).
                •	Discuss how the author addresses issues of endogeneity, causal identification, and potential biases, including the statistical models or analytical strategies applied.
                •	If the article incorporates qualitative methods, outline how qualitative evidence was gathered (e.g., interviews, discourse or textual analysis) and how it complements the quantitative analysis.
                4.	Conclusions and Contributions:
                •	Summarize the key findings and explain how they respond to the initial research question.
                •	Discuss the theoretical, methodological, and empirical contributions of the article to the academic literature.
                •	Reflect on the potential implications of these findings for public policy, social practice, or broader political debates.

            Writing Requirements:
                •	The summary must be well-structured, logically coherent, and no fewer than 500 words in length.
                •	The tone and style should be academic, avoiding colloquial expressions.
                •	Only output the content of the summary itself; do not include task instructions, additional explanations, or personal commentary.

            *** Generate the summary in English with a podcast style. ***

            '''
            },
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

