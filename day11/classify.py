# Call an LLM from code.

import os
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

MODEL = "claude-haiku-5-5"


# ---- step 1: done. a plain call. ----

# msg = client.messages.create(
#     model=MODEL,
#     max_tokens=200,
#     messages=[{"role": "user", "content": "In one sentence: what is Bitcoin?"}],
# )
# print(msg.content[0].text)
# print("tokens in:", msg.usage.input_tokens, " out:", msg.usage.output_tokens)


# ---- step 2: a system prompt, and a constrained output ----

msg = client.messages.create(
    model=MODEL,
    max_tokens=10,
    system=(
        "You classify cryptocurrencies. "
        "Reply with exactly one word from this list and nothing else: "
        "stablecoin, layer1, meme, other."
    ),
    messages=[{"role": "user", "content": "Tether (usdt)"}],
)

print(repr(msg.content[0].text))


# ---- step 3: your turn ----
#
# write a function:
#
#   def classify(name, symbol):
#       ...call the API with the same system prompt...
#       ...return the answer, cleaned up...
#
# then loop over these and print each one:
#
#   coins = [("Bitcoin","btc"), ("Tether","usdt"), ("Ethereum","eth"),
#            ("USDC","usdc"), ("Solana","sol")]
#
# add up the tokens as you go and print the total at the end.
SYSTEM = (
    "You classify cryptocurrencies. "
    "Reply with exactly one word from this list and nothing else: "
    "stablecoin, layer1, meme, other."
)
def classify(name, symbol):
    msg = client.messages.create(
        model=MODEL,
        max_tokens=10,
        system=SYSTEM,
        messages=[{"role": "user", "content": f"{name} ({symbol})"}],
    )
    answer = msg.content[0].text.strip().lower()
    return answer, msg.usage.input_tokens, msg.usage.output_tokens


coins = [("Bitcoin", "btc"), ("Tether", "usdt"), ("Ethereum", "eth"),
         ("USDC", "usdc"), ("Solana", "sol")]

total_input_tokens = 0
total_output_tokens = 0

for name, symbol in coins:
    category, input_tokens, output_tokens = classify(name, symbol)
    total_input_tokens += input_tokens
    total_output_tokens += output_tokens
    print(f"{name} ({symbol}): {category}")

print("tokens in:", total_input_tokens, " out:", total_output_tokens)