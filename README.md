# RRR-GenAI-Competition-Submission

# Project Overview

## AI Evaluator using Generative AI Principles

Our project focuses on leveraging Generative AI principles to create an AI evaluator capable of providing thorough text evaluations for solutions. The system incorporates several layers of complex large language models (LLMs) and utilizes innovative techniques for idea evaluation.

## Key Components

### 1. Synthetic Data Generation

To train our models, we employed a process known as **Synthetic Agent Tuning**. This involved simulating discussions between two AI agents, generating JSON data containing AI evaluations for given ideas. This synthetic data serves as a foundation for training the language models.

### 2. Retrieval Augmented Generation (RAG)

We integrated the open-source model **Tinyllama** from Hugging Face, enhancing it with **RAG capabilities**. RAG allows our system to draw on external information during evaluations, providing grounded assessments and improving the overall quality of responses.

(future direction):
### 3. Discriminator Function with GANs

Originally, our goal was to implement **Generative Adversarial Networks (GANs)**, specifically focusing on the discriminator part. This component was intended to filter out nonsensical inputs by training the model to recognize good problem and solution pairs. Due to computational constraints, we adjusted our approach to a fine-tuned LLM that collaborates with RAG to deliver effective answers.
