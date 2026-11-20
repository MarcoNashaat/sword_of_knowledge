"""Rebuild index.html after editing questions.json.
Usage: python3 build.py
Each category in questions.json: {"c": name, "m": [[question, correct, wrong1, wrong2, wrong3], ...],
"n": [[question, answer, unit, typical_error, isYear(0/1)], ...]}"""
import json
bank = json.load(open("questions.json", encoding="utf-8"))
tpl = open("index.template.html", encoding="utf-8").read()
data = json.dumps(bank, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
open("index.html", "w", encoding="utf-8").write(tpl.replace("/*BANK*/", data))
print("built:", sum(len(c["m"]) for c in bank), "MCQ,", sum(len(c["n"]) for c in bank), "numeric")
