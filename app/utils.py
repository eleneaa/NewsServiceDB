import json
from typing import Dict, List


def load_json(file_path: str) -> Dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_comments_count(news_id: int, comments: List[Dict]) -> int:
    return sum(1 for comment in comments if comment['news_id'] == news_id)
