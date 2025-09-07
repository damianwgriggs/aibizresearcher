# This file acts as our local, static database of articles.
# In a real-world scenario, this data might come from a dedicated database
# or a more robust data pipeline.

ARTICLES = [
    {
        "source": "TechCrunch - 'What is generative AI?'",
        "content": """
        Generative AI is a type of artificial intelligence that can create new content, like text, images, audio, and video. It works by learning patterns from massive amounts of data and then using that knowledge to generate new, original outputs.
        Unlike traditional AI that might classify data or make predictions, generative AI focuses on creation. This has led to the development of powerful tools like large language models (LLMs) such as OpenAI's GPT series and Google's Gemini, which can write essays, generate code, and hold conversations.
        The technology is rapidly evolving, with new models and applications appearing constantly. While it holds immense potential for industries like marketing, entertainment, and software development, it also raises important questions about ethics, copyright, and the potential for misuse.
        """
    },
    {
        "source": "Forbes - 'The State Of Generative AI In The Enterprise'",
        "content": """
        Enterprises are rapidly adopting generative AI to improve efficiency and create new business opportunities. A 2023 survey showed that over 60% of large companies are already experimenting with generative AI in some form.
        Key use cases include customer service chatbots that can handle complex queries, automated content creation for marketing campaigns, and sophisticated data analysis to identify market trends. Companies are also using it to accelerate software development by generating and debugging code.
        However, adoption is not without its challenges. Data security and privacy are major concerns, as is the cost of developing and deploying these large models. Furthermore, there is a significant skills gap, with a high demand for engineers and data scientists who can work with this new technology. Integrating generative AI with existing legacy systems also poses a significant technical hurdle for many organizations.
        """
    },
    {
        "source": "McKinsey - 'The Economic Potential of Generative AI'",
        "content": """
        The economic impact of generative AI is projected to be substantial, potentially adding trillions of dollars to the global economy annually. The biggest gains are expected to come from increased productivity across a wide range of business functions.
        Customer operations, marketing and sales, software engineering, and R&D are among the areas expected to see the most significant productivity boosts. For example, generative AI could automate up to 70% of tasks related to customer service and technical support.
        The technology also has the potential to create new products and services, driving innovation and economic growth. However, realizing this potential will require significant investment in technology, talent, and new business processes. There is also a risk of job displacement for roles that are highly susceptible to automation, which will require proactive measures from both businesses and governments to manage.
        """
    }
]