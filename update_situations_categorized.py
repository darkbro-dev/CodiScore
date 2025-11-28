import json

# Define the categorized list of situations with the user's requested order
# Added "Direct Input" to a "Etc" or just appended to the list logic in app.py
# For the translation file, I will structure it as categories.

SITUATIONS_CATEGORIZED = {
    "한국어": {
        "특별한 날": ["소개팅", "결혼식 하객", "면접/발표", "파티/클럽", "전시회/공연 관람", "격식 있는 모임", "장례식"],
        "일상": ["데이트", "카페", "출근(비즈니스 캐주얼)", "출근(정장)", "학교/캠퍼스", "여행", "산책/가벼운 외출", "운동/액티비티", "공항 패션"],
        "기타": ["직접 입력"]
    },
    "English": {
        "Special Day": ["Blind Date", "Wedding Guest", "Interview/Presentation", "Party/Club", "Exhibition/Performance", "Formal Gathering", "Funeral"],
        "Daily": ["Date", "Cafe", "Work (Business Casual)", "Work (Formal)", "School/Campus", "Travel", "Walk/Light Outing", "Exercise/Activity", "Airport Fashion"],
        "Etc": ["Direct Input"]
    },
    "日本語": {
        "特別な日": ["合コン", "結婚式ゲスト", "面接/発表", "パーティー/クラブ", "展示会/公演観覧", "格式ある集まり", "葬儀"],
        "日常": ["デート", "カフェ", "通勤（ビジネスカジュアル）", "通勤（スーツ）", "学校/キャンパス", "旅行", "散歩/軽い外出", "運動/アクティビティ", "空港ファッション"],
        "その他": ["直接入力"]
    },
    "中文": {
        "特殊场合": ["相亲", "婚礼宾客", "面试/演讲", "派对/夜店", "展览/演出观看", "正式聚会", "葬礼"],
        "日常": ["约会", "咖啡厅", "上班(商务休闲)", "上班(正装)", "学校/校园", "旅行", "散步/轻便外出", "运动/活动", "机场时尚"],
        "其他": ["直接输入"]
    }
}

# Read existing file
file_path = "d:/_Works Web/251126_CodiScore/ui_translations.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove old SITUATIONS definition
if "SITUATIONS =" in content:
    content = content.split("SITUATIONS =")[0]

# Append new SITUATIONS
situations_code = "\n\nSITUATIONS = " + json.dumps(SITUATIONS_CATEGORIZED, ensure_ascii=False, indent=4)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content + situations_code)

print("Successfully updated SITUATIONS list with categories.")
