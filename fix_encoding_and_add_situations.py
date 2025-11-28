import json

# 1. Read the base content from ui_translations_complete.py
with open("d:/_Works Web/251126_CodiScore/ui_translations_complete.py", "r", encoding="utf-8") as f:
    content = f.read()

# 2. Apply the page_description change
old_desc = '"page_description": "당신의 사진을 올려주세요. **냉철한 평가**와 **완벽한 코디**를 제안해 드립니다.",'
new_desc = '"page_description": "당신의 사진을 올려주세요.  \\n**냉철한 평가**와 **완벽한 코디**를 제안해 드립니다.  \\n  \\nAI가 선택된 상황에 맞는 **TPO(상황) 분석**을 하고  \\n놀라울 정도로 정확하게 판단합니다.",'
content = content.replace(old_desc, new_desc)

# 3. Define SITUATIONS
situations_code = """

SITUATIONS = {
    "한국어": {
        "일상": ["데이트", "카페", "출근(비즈니스 캐주얼)", "출근(정장)", "학교/캠퍼스", "여행", "산책/가벼운 외출", "운동/액티비티", "공항 패션"],
        "특별한 날": ["결혼식 하객", "소개팅", "면접/발표", "파티/클럽", "전시회/공연 관람", "격식 있는 모임", "장례식"]
    },
    "English": {
        "Daily": ["Date", "Cafe", "Work (Business Casual)", "Work (Formal)", "School/Campus", "Travel", "Walk/Light Outing", "Exercise/Activity", "Airport Fashion"],
        "Special": ["Wedding Guest", "Blind Date", "Interview/Presentation", "Party/Club", "Exhibition/Performance", "Formal Gathering", "Funeral"]
    },
    "日本語": {
        "日常": ["デート", "カフェ", "通勤（ビジネスカジュアル）", "通勤（スーツ）", "学校/キャンパス", "旅行", "散歩/軽い外出", "運動/アクティビティ", "空港ファッション"],
        "特別な日": ["結婚式ゲスト", "合コン", "面接/発表", "パーティー/クラブ", "展示会/公演観覧", "格式ある集まり", "葬儀"]
    },
    "中文": {
        "日常": ["约会", "咖啡厅", "上班(商务休闲)", "上班(正装)", "学校/校园", "旅行", "散步/轻便外出", "运动/活动", "机场时尚"],
        "特殊场合": ["婚礼宾客", "相亲", "面试/演讲", "派对/夜店", "展览/演出观看", "正式聚会", "葬礼"]
    }
}
"""

# 4. Write to ui_translations.py
with open("d:/_Works Web/251126_CodiScore/ui_translations.py", "w", encoding="utf-8") as f:
    f.write(content + situations_code)

print("Successfully rewrote ui_translations.py with correct encoding and content.")
