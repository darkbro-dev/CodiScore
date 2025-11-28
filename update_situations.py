import json

# Define the comprehensive list of situations for 4 main languages
# 30 items including Direct Input

SITUATIONS_NEW = {
    "한국어": {
        "상황 선택": [
            "데이트", "카페/가벼운 만남", "출근 (비즈니스 캐주얼)", "출근 (정장/포멀)", 
            "결혼식 하객", "소개팅", "면접", "중요한 발표/미팅", 
            "파티/클럽", "전시회/공연 관람", "격식 있는 모임/디너", "장례식",
            "학교/캠퍼스룩", "여행/휴양지", "산책/가벼운 외출", "운동/피트니스", 
            "공항 패션", "친구들과의 모임", "쇼핑", "놀이공원/테마파크",
            "등산/아웃도어", "골프/라운딩", "테니스/배드민턴", "호캉스",
            "페스티벌/콘서트", "가족 모임", "종교 행사", "집들이", 
            "프로필 사진 촬영", "직접 입력"
        ]
    },
    "English": {
        "Select Situation": [
            "Date", "Cafe/Casual Meetup", "Work (Business Casual)", "Work (Formal)",
            "Wedding Guest", "Blind Date", "Interview", "Presentation/Meeting",
            "Party/Club", "Exhibition/Performance", "Formal Dinner", "Funeral",
            "School/Campus", "Travel/Resort", "Walk/Light Outing", "Exercise/Fitness",
            "Airport Fashion", "Gathering with Friends", "Shopping", "Amusement Park",
            "Hiking/Outdoor", "Golf", "Tennis/Badminton", "Hotel Vacation",
            "Festival/Concert", "Family Gathering", "Religious Event", "Housewarming Party",
            "Profile Photo Shoot", "Direct Input"
        ]
    },
    "日本語": {
        "シチュエーション選択": [
            "デート", "カフェ/軽い集まり", "通勤（ビジネスカジュアル）", "通勤（フォーマル）",
            "結婚式ゲスト", "合コン", "面接", "重要な発表/会議",
            "パーティー/クラブ", "展示会/公演観覧", "格式ある集まり/ディナー", "葬儀",
            "学校/キャンパス", "旅行/リゾート", "散歩/軽い外出", "運動/フィットネス",
            "空港ファッション", "友達との集まり", "ショッピング", "遊園地/テーマパーク",
            "登山/アウトドア", "ゴルフ", "テニス/バドミントン", "ホカンス",
            "フェスティバル/コンサート", "家族の集まり", "宗教行事", "引っ越し祝い",
            "プロフィール写真撮影", "直接入力"
        ]
    },
    "中文": {
        "选择场合": [
            "约会", "咖啡厅/轻松聚会", "上班 (商务休闲)", "上班 (正装)",
            "婚礼宾客", "相亲", "面试", "重要演讲/会议",
            "派对/夜店", "展览/演出观看", "正式聚会/晚餐", "葬礼",
            "学校/校园", "旅行/度假", "散步/轻便外出", "运动/健身",
            "机场时尚", "朋友聚会", "购物", "游乐园/主题公园",
            "登山/户外", "高尔夫", "网球/羽毛球", "酒店度假",
            "音乐节/演唱会", "家庭聚会", "宗教活动", "乔迁派对",
            "个人写真拍摄", "直接输入"
        ]
    }
}

# Read existing file
file_path = "d:/_Works Web/251126_CodiScore/ui_translations.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Remove old SITUATIONS definition if it exists (it's at the end)
if "SITUATIONS =" in content:
    content = content.split("SITUATIONS =")[0]

# Append new SITUATIONS
# We need to format it nicely as Python code
situations_code = "\n\nSITUATIONS = " + json.dumps(SITUATIONS_NEW, ensure_ascii=False, indent=4)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content + situations_code)

print("Successfully updated SITUATIONS list to 30 items.")
