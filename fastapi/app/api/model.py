import torch
from transformers import BertTokenizerFast, BertForQuestionAnswering


class QAModel:
    def __init__(self):
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model_name = "nyust-eb210/braslab-bert-drcd-384"
        self.tokenizer = BertTokenizerFast.from_pretrained(self.model_name)
        self.model = BertForQuestionAnswering.from_pretrained(self.model_name).to(
            self.device
        )

    def predict(self, text, query):
        answer, confidence = "Not able to answer your question.", 0.0
        encoded_input = self.tokenize(text, query).to(self.device)
        qa_outputs = self.model(**encoded_input)
        start = torch.argmax(qa_outputs.start_logits).item()
        end = torch.argmax(qa_outputs.end_logits).item()
        if start > end:
            return answer, confidence

        answer = encoded_input.input_ids.tolist()[0][start : end + 1]
        answer = "".join(self.tokenizer.decode(answer).split())

        start_prob = torch.max(torch.nn.Softmax(dim=-1)(qa_outputs.start_logits)).item()
        end_prob = torch.max(torch.nn.Softmax(dim=-1)(qa_outputs.end_logits)).item()
        confidence = (start_prob + end_prob) / 2

        return answer, confidence

    def tokenize(self, text: str, query: str):
        encoded_input = self.tokenizer(
            text,
            query,
            max_length=512,
            truncation=True,
            return_tensors="pt",
        )
        return encoded_input


def get_model():
    qa_model = QAModel()
    return qa_model


# if __name__ == "__main__":
#     text = "馬雲是我爸爸。"
#     query = "我爸爸是誰？"
#     device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#     tokenizer = BertTokenizerFast.from_pretrained(r"nyust-eb210/braslab-bert-drcd-384")
#     model = BertForQuestionAnswering.from_pretrained(
#         r"nyust-eb210/braslab-bert-drcd-384"
#     ).to(device)
#     encoded_input = tokenizer(text, query, return_tensors="pt").to(device)
#     qa_outputs = model(**encoded_input)

#     start = torch.argmax(qa_outputs.start_logits).item()
#     end = torch.argmax(qa_outputs.end_logits).item()
#     answer = encoded_input.input_ids.tolist()[0][start : end + 1]
#     answer = "".join(tokenizer.decode(answer).split())

#     start_prob = torch.max(torch.nn.Softmax(dim=-1)(qa_outputs.start_logits)).item()
#     end_prob = torch.max(torch.nn.Softmax(dim=-1)(qa_outputs.end_logits)).item()
#     confidence = (start_prob + end_prob) / 2
#     print(answer, confidence)
