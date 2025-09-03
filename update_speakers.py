#!/usr/bin/env python3
import re

def update_speaker_previews():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到所有講師的data-speaker-experience內容
    speaker_data_pattern = r'data-speaker-name="([^"]+)"[^>]*?data-speaker-experience="([^"]+)"'
    speakers = re.findall(speaker_data_pattern, content, re.DOTALL)
    
    print(f"Found {len(speakers)} speakers")
    
    for name, experience in speakers:
        print(f"Processing: {name}")
        
        # 找到對應的preview區塊並替換中文內容
        preview_pattern = r'(<div class="speaker-experience-preview">[\s\S]*?<span class="lang-zh">)[^<]+(</span>)'
        
        # 在特定講師卡片區域中查找
        speaker_card_pattern = rf'(<div class="speaker-card[^>]*?data-speaker-name="{re.escape(name)}"[^>]*?>[\s\S]*?<div class="speaker-experience-preview">[\s\S]*?<span class="lang-zh">)[^<]+(</span>)'
        
        def replace_preview(match):
            return match.group(1) + experience + match.group(2)
        
        content = re.sub(speaker_card_pattern, replace_preview, content, count=1)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Updated all speaker previews")

if __name__ == "__main__":
    update_speaker_previews()
