# Script to add remaining language translations
# This will append translations to ui_translations.py

translations_to_add = """
# Japanese
UI_TEXT["日本語"] = UI_TEXT["한국어"].copy()
UI_TEXT["日本語"].update({
    "page_title": "AIファッションスタイリスト",
    "page_description": "写真をアップロードしてください。**正直な評価**と**完璧なコーデ**を提案します。",
    "settings": "⚙️ 設定",
    "user_status": "会員ステータス",
    "free_member": "🌱 無料会員",
    "premium_member": "👑 プレミアム会員",
    "remaining_uses": "今日の残り無料回数",
    "watch_ads": "📺 広告2本で無制限",
    "select_situation": "状況を選択してください",
    "situation_title": "📍 どんな状況ですか？",
})

# Chinese
UI_TEXT["中文"] = UI_TEXT["English"].copy()
UI_TEXT["中文"].update({
    "page_title": "AI时尚造型师",
    "page_description": "上传您的照片。获得**诚实的评价**和**完美的穿搭建议**。",
    "settings": "⚙️ 设置",
    "select_situation": "选择场合",
    "situation_title": "📍 什么场合？",
})

# Spanish  
UI_TEXT["Español"] = UI_TEXT["English"].copy()
UI_TEXT["Español"].update({
    "page_title": "Estilista de Moda IA",
    "page_description": "Sube tu foto. Obtén **críticas honestas** y **recomendaciones de atuendos perfectos**.",
    "settings": "⚙️ Configuración",
    "select_situation": "Seleccionar situación",
    "situation_title": "📍 ¿Cuál es la ocasión?",
})

# French
UI_TEXT["Français"] = UI_TEXT["English"].copy()
UI_TEXT["Français"].update({
    "page_title": "Styliste de Mode IA",
    "page_description": "Téléchargez votre photo. Obtenez **des critiques honnêtes** et **des recommandations de tenues parfaites**.",
    "settings": "⚙️ Paramètres",
    "select_situation": "Sélectionner une situation",
    "situation_title": "📍 Quelle est l'occasion?",
})

# Russian
UI_TEXT["Русский"] = UI_TEXT["English"].copy()
UI_TEXT["Русский"].update({
    "page_title": "ИИ Модный Стилист",
    "page_description": "Загрузите фото. Получите **честную оценку** и **идеальные рекомендации по стилю**.",
    "settings": "⚙️ Настройки",
    "select_situation": "Выберите ситуацию",
    "situation_title": "📍 Какой повод?",
})

# Portuguese
UI_TEXT["Português"] = UI_TEXT["English"].copy()
UI_TEXT["Português"].update({
    "page_title": "Estilista de Moda IA",
    "page_description": "Envie sua foto. Obtenha **críticas honestas** e **recomendações de looks perfeitos**.",
    "settings": "⚙️ Configurações",
    "select_situation": "Selecionar situação",
    "situation_title": "📍 Qual é a ocasião?",
})

# Indonesian
UI_TEXT["Bahasa Indonesia"] = UI_TEXT["English"].copy()
UI_TEXT["Bahasa Indonesia"].update({
    "page_title": "Penata Gaya AI",
    "page_description": "Unggah foto Anda. Dapatkan **kritik jujur** dan **rekomendasi outfit sempurna**.",
    "settings": "⚙️ Pengaturan",
    "select_situation": "Pilih situasi",
    "situation_title": "📍 Apa kesempatannya?",
})

# Arabic
UI_TEXT["العربية"] = UI_TEXT["English"].copy()
UI_TEXT["العربية"].update({
    "page_title": "مصمم أزياء بالذكاء الاصطناعي",
    "page_description": "قم بتحميل صورتك. احصل على **تقييم صادق** و **توصيات ملابس مثالية**.",
    "settings": "⚙️ الإعدادات",
    "select_situation": "اختر الموقف",
    "situation_title": "📍 ما المناسبة؟",
})

# Hindi
UI_TEXT["हिन्दी"] = UI_TEXT["English"].copy()
UI_TEXT["हिन्दी"].update({
    "page_title": "एआई फैशन स्टाइलिस्ट",
    "page_description": "अपनी फोटो अपलोड करें। **ईमानदार समीक्षा** और **परफेक्ट आउटफिट सुझाव** प्राप्त करें।",
    "settings": "⚙️ सेटिंग्स",
    "select_situation": "स्थिति चुनें",
    "situation_title": "📍 अवसर क्या है?",
})

# Bengali  
UI_TEXT["বাংলা"] = UI_TEXT["English"].copy()
UI_TEXT["বাংলা"].update({
    "page_title": "এআই ফ্যাশন স্টাইলিস্ট",
    "page_description": "আপনার ছবি আপলোড করুন। **সৎ মূল্যায়ন** এবং **নিখুঁত পোশাক সুপারিশ** পান।",
    "settings": "⚙️ সেটিংস",
    "select_situation": "পরিস্থিতি নির্বাচন করুন",
    "situation_title": "📍 উপলক্ষ কি?",
})
"""

# Read current file
with open(r"d:\_Works Web\251126_CodiScore\ui_translations.py", "r", encoding="utf-8") as f:
    content = f.read()

# Append translations
with open(r"d:\_Works Web\251126_CodiScore\ui_translations.py", "a", encoding="utf-8") as f:
    f.write("\n" + translations_to_add)

print("All language translations added successfully!")
