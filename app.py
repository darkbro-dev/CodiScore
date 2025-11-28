import streamlit as st
import google.generativeai as genai
from PIL import Image
import json
from streamlit_javascript import st_javascript
from ui_translations import UI_TEXT, SITUATIONS
import re

# Page Config
st.set_page_config(
    page_title="AI Fashion Stylist",
    page_icon="👗",
    layout="wide"
)

# Load Custom CSS
def load_css():
    with open("d:/_Works Web/251126_CodiScore/style.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# --- Constants ---
MODELS = {
    "analysis": {
        "flash": "gemini-2.5-flash",
        "pro": "gemini-2.5-pro"
    },
    "image": {
        "imagen": "gemini-2.5-flash-image",
        "pro": "nano-banana-pro-preview"
    }
}

LANGUAGES = {
    "한국어": "Korean",
    "English": "English",
    "日本語": "Japanese",
    "中文": "Chinese",
    "हिन्दी": "Hindi",
    "Español": "Spanish",
    "Français": "French",
    "العربية": "Arabic",
    "বাংলা": "Bengali",
    "Русский": "Russian",
    "Português": "Portuguese",
    "Bahasa Indonesia": "Indonesian"
}


# --- Session State Initialization ---
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0
if 'is_premium' not in st.session_state:
    st.session_state.is_premium = False
if 'platform' not in st.session_state:
    st.session_state.platform = "unknown"
if 'language' not in st.session_state:
    st.session_state.language = "한국어"

# --- Helper Functions ---
def t(key):
    """Get translated text for current language"""
    lang = st.session_state.get('language', '한국어')
    
    # Try to get translation for selected language
    if lang in UI_TEXT and key in UI_TEXT[lang]:
        return UI_TEXT[lang][key]
    
    # Fallback to English
    if key in UI_TEXT.get('English', {}):
        return UI_TEXT['English'][key]
    
    # Last resort: return Korean or key itself
    return UI_TEXT.get('한국어', {}).get(key, key)

def get_platform():
    # Simple check using screen width to guess platform
    # This is a heuristic: < 768px is likely mobile
    width = st_javascript("window.innerWidth")
    if width:
        return "mobile" if width < 768 else "pc"
    return "pc" # Default to PC if detection fails

def init_api():
    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
        return True
    except Exception:
        st.error(t("api_error"))
        return False

# --- Main App ---
def main():
    # Initialize API
    if not init_api():
        return

    # Platform Detection
    platform = get_platform()
    st.session_state.platform = platform

    # Sidebar
    with st.sidebar:
        st.title(t("settings"))
        
        # User Status
        status = t("premium_member") if st.session_state.is_premium else t("free_member")
        st.info(f"{t('user_status')}: **{status}**")
        
        if not st.session_state.is_premium:
            st.write(f"{t('remaining_uses')}: **{3 - st.session_state.usage_count} / 3**")
            
            # Premium Upgrade Button
            if st.button("👑 프리미엄 업그레이드 하러 가기", type="primary", use_container_width=True, key="sidebar_upgrade_btn"):
                # Mock payment success
                st.session_state.is_premium = True
                st.balloons()
                st.success("프리미엄 회원이 되신 것을 환영합니다!")
                st.rerun()
        
        st.divider()
        
        # Language Selection
        st.subheader(t("language_select"))
        
        # Get current language index
        current_lang = st.session_state.language
        lang_options = list(LANGUAGES.keys())
        current_index = lang_options.index(current_lang) if current_lang in lang_options else 0
        
        selected_language = st.selectbox(
            t("result_language"),
            options=lang_options,
            index=current_index,
            key="language_selector"
        )
        
        # Update language and trigger rerun if changed
        if selected_language != st.session_state.language:
            st.session_state.language = selected_language
            st.rerun()
        
        st.divider()
        
        # Model Selection
        st.subheader(t("model_select"))
        
        # Analysis Model
        analysis_options = [t("flash_cheap"), t("pro_expensive")]
        analysis_choice = st.selectbox(t("analysis_ai"), analysis_options, index=0)
        selected_analysis_model = MODELS["analysis"]["flash"] if "Flash" in analysis_choice else MODELS["analysis"]["pro"]
        
        if "Pro" in analysis_choice and not st.session_state.is_premium:
            st.warning(t("premium_only").format(model="Pro"))
            selected_analysis_model = MODELS["analysis"]["flash"]

        # Image Model
        image_options = [t("flash_image"), t("nano_banana")]
        image_choice = st.selectbox(t("image_gen_ai"), image_options, index=0)
        selected_image_model = MODELS["image"]["imagen"] if "Flash" in image_choice else MODELS["image"]["pro"]

        if "Nano" in image_choice and not st.session_state.is_premium:
            st.warning(t("premium_only").format(model="Nano Banana Pro"))
            selected_image_model = MODELS["image"]["imagen"]
            
        st.divider()
        
        # Why Ads? Expander
        with st.expander(t("why_ads")):
            st.markdown(t("ads_explanation"))

    # Main Content
    st.title(t("page_title"))
    st.markdown(t("page_description"))
    
    # TPO Explanation Button (Expander)
    with st.expander("💡 " + t("tpo_question"), expanded=False):
        st.markdown(t("tpo_explanation"))
    
    # Situation Selection
    st.markdown(f"### {t('situation_title')}")
    
    # Get situations for current language, fallback to Korean
    current_lang = st.session_state.language
    situations = SITUATIONS.get(current_lang, SITUATIONS["한국어"])
    
    # Build a flat list with category headers as visual separators
    situation_options = []
    
    for category, items in situations.items():
        # Add category header
        situation_options.append(f"━━━ {category} ━━━")
        # Add items under this category
        situation_options.extend(items)
    
    # Selectbox
    selected_situation = st.selectbox(
        t("select_situation"),
        options=situation_options,
        index=1,  # Skip the first header, select first actual item
        help=t("situation_help")
    )
    
    # If user selected a header (separator), default to first item in that category
    if selected_situation.startswith("━━━"):
        # Find the first non-header item after this
        idx = situation_options.index(selected_situation)
        if idx + 1 < len(situation_options):
            selected_situation = situation_options[idx + 1]
    
    # Direct Input Handling
    if selected_situation == "직접 입력" or selected_situation == "Direct Input" or selected_situation == "直接入力" or selected_situation == "直接输入":
        custom_situation = st.text_input(
            "상황을 직접 입력해주세요 / Enter your situation",
            placeholder="예: 친구 생일 파티, 회사 면접 등"
        )
        if custom_situation:
            selected_situation = custom_situation
    
    st.divider()
    
    uploaded_file = st.file_uploader(t("upload_photo"), type=["jpg", "jpeg", "png", "webp"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        
        # Optimize image size to prevent API errors
        max_size = 1024
        if image.width > max_size or image.height > max_size:
            # Resize while maintaining aspect ratio
            image.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
            st.info(t("image_optimized").format(width=image.width, height=image.height))
        
        st.image(image, caption=t("uploaded_photo"), use_container_width=True)
        
        # Check Usage Limit
        if not st.session_state.is_premium and st.session_state.usage_count >= 3:
            st.error(t("limit_reached"))
            st.info(t("watch_ads_prompt"))
            return

        # --- Analysis Button ---
        if st.button(t("analyze_button")):
            # Increment Usage
            if not st.session_state.is_premium:
                st.session_state.usage_count += 1
            
            with st.spinner(t("analyzing")):
                try:
                    # 1. Image Analysis
                    model = genai.GenerativeModel(selected_analysis_model)
                    
                    # Get selected language
                    output_language = LANGUAGES[st.session_state.language]
                    
                    # Simplified Prompt for analysis
                    prompt = f"""Analyze this fashion photo for: {selected_situation}

Output in {output_language} as JSON:
{{
    "score": 0-100,
    "tpo_score": 0-100,
    "items": ["item1", "item2"],
    "style": "style",
    "reason": "score reasoning in {output_language}",
    "tpo_analysis": "TPO for {selected_situation} in {output_language}",
    "improvements": "suggestions in {output_language}"
}}

Consider: TPO for {selected_situation}, fit, colors, formality.
Be critical but constructive. Use {output_language}."""
                    # Retry logic for 500 errors
                    max_retries = 3
                    retry_count = 0
                    response = None
                    
                    while retry_count < max_retries:
                        try:
                            response = model.generate_content([prompt, image])
                            break  # Success, exit retry loop
                        except Exception as api_error:
                            error_msg = str(api_error)
                            if "500" in error_msg or "internal error" in error_msg.lower():
                                retry_count += 1
                                if retry_count < max_retries:
                                    st.warning(t("api_retry_warning").format(count=retry_count, max=max_retries))
                                    import time
                                    time.sleep(2)  # Wait 2 seconds before retry
                                else:
                                    raise api_error  # Max retries reached
                            else:
                                raise api_error  # Different error, don't retry
                    
                    if response is None:
                        st.error(t("no_response"))
                        return
                    
                    # Parse JSON response
                    try:
                        # Clean up json string if needed
                        text = response.text.strip()
                        if text.startswith("```json"):
                            text = text[7:-3]
                        elif text.startswith("```"):
                            text = text[3:-3]
                        analysis_data = json.loads(text)
                        
                        # Store result in session state
                        st.session_state['analysis_result'] = analysis_data
                        
                    except Exception as e:
                        st.error(f"{t('analysis_failed')}: {e}")
                        analysis_data = {"score": 50, "reason": "...", "improvements": "..."}
                        st.session_state['analysis_result'] = analysis_data

                except Exception as e:
                    st.error(f"{t('analysis_error')}: {e}")

        # --- Display Analysis Result ---
        if 'analysis_result' in st.session_state:
            analysis_data = st.session_state['analysis_result']
            
            # Display Analysis
            st.markdown(f"### {t('analysis_result')}")
            
            st.divider()
            
            # Score Display - 3 columns
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="score-container">
                    <div class="score-value">{analysis_data.get('score', 0)}</div>
                    <div class="score-label">{t('fashion_score')}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="score-container">
                    <div class="score-value">{analysis_data.get('tpo_score', 0)}</div>
                    <div class="score-label">{t('tpo_suitability')}</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                style_text = analysis_data.get('style', '-')
                # Calculate font size based on text length
                text_len = len(str(style_text))
                if text_len > 15:
                    font_class = "score-value-small"
                elif text_len > 8:
                    font_class = "score-value-medium"
                else:
                    font_class = "score-value-large"
                    
                st.markdown(f"""
                <div class="score-container">
                    <div class="{font_class}">{style_text}</div>
                    <div class="score-label">{t('style_label')}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.divider()
            
            # 감지된 아이템 (Emphasized with Tags)
            if 'items' in analysis_data and analysis_data['items']:
                st.markdown(f"<div style='text-align: center; margin-bottom: 0.8rem; font-weight: 600; color: #718096;'>{t('detected_items')}</div>", unsafe_allow_html=True)
                
                # Ensure items are a list
                items_list = analysis_data['items']
                if isinstance(items_list, str):
                    items_list = [i.strip() for i in items_list.split(',')]
                    
                items_html = '<div class="item-tag-container">'
                for item in items_list:
                    items_html += f'<span class="item-tag">{item}</span>'
                items_html += '</div>'
                
                st.markdown(items_html, unsafe_allow_html=True)
                st.divider()

            # 총평
            st.markdown(f"#### 📝 {t('summary')}")
            st.write(analysis_data.get('reason', '-'))
            
            st.markdown("")  # Spacing
            
            # 상황 분석 (TPO)
            if 'tpo_analysis' in analysis_data:
                st.markdown(f"#### 🎯 {t('situation_analysis')}")
                st.write(analysis_data.get('tpo_analysis', '-'))
                st.markdown("")  # Spacing
            
            # 개선점 (Formatted with line breaks)
            st.markdown(f"#### 💡 {t('improvements')}")
            improvements_text = analysis_data.get('improvements', '-')
            if improvements_text:
                # Replace "1. " with "\n1. ", but avoid double newlines if they exist
                formatted_improvements = re.sub(r'(?<!\n)(\d+\.)', r'\n\1', improvements_text)
                st.write(formatted_improvements)
            
            st.markdown("") # Spacing

            # Conditional Button based on Premium Status
            if st.session_state.get('is_premium', False):
                # Premium: Direct image generation
                if st.button("✨ 내 사진에 개선사항 적용하기", type="primary", use_container_width=True, key="apply_improvements_premium"):
                    st.session_state['trigger_image_generation'] = True
                    st.rerun()
            else:
                # Free: Upgrade prompt
                if st.button("👑 프리미엄 업그레이드 하러 가기", type="primary", use_container_width=True, key="apply_improvements_upgrade"):
                    st.session_state.is_premium = True
                    st.balloons()
                    st.success("프리미엄 회원이 되신 것을 환영합니다! 이제 '내 사진에 개선사항 적용하기' 버튼을 눌러주세요.")
                    st.rerun()

            # --- Image Generation Logic ---
            if st.session_state.get('trigger_image_generation', False):
                # Reset trigger
                st.session_state['trigger_image_generation'] = False
                
                with st.spinner("AI가 개선된 코디를 생성하고 있습니다..."):
                    try:
                        # Image Generation Prompt
                        output_language = LANGUAGES[st.session_state.language]
                        gen_prompt = (
                            "Create a fashion photograph of a person wearing a stylish, modern outfit.\n"
                            f"Improvements needed: {analysis_data.get('improvements', 'Make it trendy and stylish')}\n"
                            "The outfit should be perfect, scoring 100 points.\n"
                            "High quality, photorealistic, professional fashion photography.\n"
                            "Style: contemporary, clean, editorial."
                        )
                        
                        # Both models use the same GenerativeModel interface
                        image_model = genai.GenerativeModel(selected_image_model)
                        response_gen = image_model.generate_content(gen_prompt)
                        
                        # Try to extract image from response
                        image_found = False
                        
                        if hasattr(response_gen, '_result') and hasattr(response_gen._result, 'candidates'):
                            for candidate in response_gen._result.candidates:
                                if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                                    for part in candidate.content.parts:
                                        # Check for inline image data
                                        if hasattr(part, 'inline_data') and part.inline_data:
                                            import base64
                                            from io import BytesIO
                                            image_data = base64.b64decode(part.inline_data.data)
                                            generated_image = Image.open(BytesIO(image_data))
                                            st.success("✨ AI가 개선된 코디 이미지를 생성했습니다!")
                                            st.image(generated_image, caption=f"AI 생성 이미지 (모델: {selected_image_model})", use_container_width=True)
                                            image_found = True
                                            break
                                if image_found:
                                    break
                        
                        # Fallback to text if no image was generated
                        if not image_found and hasattr(response_gen, 'text') and response_gen.text:
                            st.info("💡 AI가 제안하는 완벽한 스타일링:")
                            st.markdown(f"**{response_gen.text}**")

                    except Exception as e:
                        error_msg = str(e)
                        if "429" in error_msg or "quota" in error_msg.lower():
                            st.error("🚫 이미지 생성 API 할당량 제한")
                            st.warning("""
                            **Google의 이미지 생성 모델은 무료 사용이 제한되어 있습니다.**
                            
                            현재 상황:
                            - `gemini-2.5-flash-image`와 `nano-banana-pro-preview` 모델은 유료 API 키가 필요합니다
                            - 무료 티어에서는 사용량 한도가 0으로 설정되어 있습니다
                            
                            대안:
                            1. **유료 플랜**: Google AI Studio에서 유료 플랜으로 업그레이드
                            2. **다른 서비스**: DALL-E, Midjourney 등 다른 이미지 생성 서비스 통합 (추후 업데이트 예정)
                            
                            💡 위에 표시된 "개선점"을 참고하여 스타일을 개선해보세요!
                            """)
                        else:
                            st.error(f"⚠️ 오류 발생: {error_msg}")
                            st.caption("문제가 계속되면 다른 모델을 선택해주세요.")


if __name__ == "__main__":
    main()

