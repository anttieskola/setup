#!/usr/bin/env python3
from transformers import AutoTokenizer

# Load Qwen2 tokenizer (proxy for DeepSeek-R1-Distill-Qwen)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-7B")

# Read the prompt
with open("test_prompt.txt", "r") as f:
    prompt = f.read()

# Tokenize and count
tokens = tokenizer.encode(prompt)
print(f"Token count: {len(tokens)}")
print(f"First 10 tokens: {tokens[:10]}")
print(f"Last 10 tokens: {tokens[-10:]}")

