class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        tokens = sentence.split()
        for index, token in enumerate(tokens):
            if token.startswith("$") and token[1:].isdigit():
                cost = int(token[1:])
                final_cost = cost - (cost * discount/100)
                tokens[index] = f"{round(final_cost)}"
        print(tokens)
        return sentence 


