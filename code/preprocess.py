from transformers import AutoTokenizer
from datasets import Dataset
import os 

# def read_questions_from_file(file_path):
#     questions_list = []
#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             # Strip newline and any trailing whitespace from each line
#             question = line.strip()
#             # Append the cleaned line to the list
#             questions_list.append(question)
#     return questions_list


# train_folder_path = "../data/train/"
# test_foler_path = "../data/test/"

# raw_train = train_folder_path + "questions.txt"
# raw_test = test_foler_path + "questions.txt"



# # model_name = "bert-base-cased"
# # tokenizer = AutoTokenizer.from_pretrained(model_name)
# # encoded_input = tokenizer(question_list, padding=True, truncation=True, return_tensors="pt")

# def preprocess(tokenizer,
#                raw_train = train_folder_path + "questions.txt", 
#                raw_test = test_foler_path + "questions.txt"):
    
#     train_question_list = read_questions_from_file(raw_train)
#     test_question_list = read_questions_from_file(raw_test)

#     encoded_train = tokenizer(train_question_list, padding=True, truncation=True, return_tensors="pt")
#     encoded_test = tokenizer(test_question_list, padding=True, truncation=True, return_tensors="pt")

#     return encoded_train, 

def read_linesfrom_file(file_path) -> list:
    result = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Append the cleaned line to the list
            result.append(line.strip())
    return result

raw_train_question_path = "../data/train/questions.txt"
raw_train_answer_path = "../data/train/reference_answers.txt"

train_question_list = read_linesfrom_file(raw_train_question_path)
train_answer_list = read_linesfrom_file(raw_train_answer_path)

train_question_dict = {"questions": train_question_list}
train_answer_dict = {"answers": train_answer_list}

train_dict = train_question_dict
train_dict.update(train_answer_dict)

train_set = Dataset.from_dict(train_dict)

ds = train_set
print(ds)
print(type(ds))
print(type(ds['questions']))
print(type(ds['questions'][0]))