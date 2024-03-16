# How to run this code

## Prerequisite

- A google drive account
- (optional, but recommened) A colabotary Pro account
- (optional, but recommened) A huggingface account

## Procedure

- Download the github repository
- Unzip the file
- If you are using colab. Upload the file to the google drive , directly under the *My Drive* directory
- Run the file code/RAG.ipynb, remember to change to path if you are using device other than colab.
- In RAG.ipynb, for customized single query, run until Test code block. To continue with test QA set, run through the end of the code.
- To evaluate test result, run metrics.ipynb
- For Significant testing, run sigtest.ipynb

# Repository
- Code: This directory contains all the runnable code.
- data: This directory contains questions-answering pair for training and testing.
- raw_data: This directory contains all raw data, including .txt, .pdf, html. As well as the code that processes the file.
- database: This directory contains all processed and runnable data
- system_outputs: This directory contains output generated from testing questions from Graham Neubig
- contributions.md: This file documents the range of 
- github_url.txt: This file contains the url to github that contains this directory
- README.md: This file.


