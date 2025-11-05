import numpy as np
from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu


def rouge_and_bleu(pred, ref):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
    scores = scorer.score(ref, pred)
    bleu = sentence_bleu([ref.split()], pred.split())
    return {
        "rouge1": scores['rouge1'].fmeasure,
        "rougeL": scores['rougeL'].fmeasure,
        "bleu": bleu
    }


def evaluate_embeddings(stored_message: str):
    """
    Dummy evaluation for now — later will compare real retrieved chunks.
    """
    return {
        "status": "ok",
        "message": stored_message,
        "avg_rouge1": 0.0,
        "avg_rougeL": 0.0,
        "avg_bleu": 0.0
    }
