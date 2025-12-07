# Ghigliottina-LLM

Various python notebooks to train a LLM to play “La Ghigliottina”, the final game of an Italian TV show called “L’Eredità”. The game involves a single player who is given a set of five words unrelated to each other, but related with a sixth word that represents the solution to the game.

## Project Overview

The project is developed in two main stages:

### 1. Dataset Creation
Initially, I focused on building the dataset by combining computer vision and NLP techniques:
- **OCR (Optical Character Recognition):** I extracted the 5 clue words directly from frames of public YouTube videos of the game.
- **NLP & LLMs:** I analyzed the video transcripts provided by YouTube services using LLMs to extract the final solution word and the specific reasoning explaining why that word is the correct answer.

### 2. Fine-Tuning Experiments
After establishing the dataset, I conducted various fine-tuning experiments. I tested different models, ranging from smaller to larger architectures, to build a system capable of effectively playing the game.

---

### ⚠️ Project Status
**Please note: This is an ongoing research project.** The code, models, and datasets are subject to changes and improvements as I continue to refine the training process and evaluate results.

I took inspiration from the challenge organized for EVALITA 2020 (https://www.ai-lc.it/ghigliottin-ai-a-evalita-2020/)
