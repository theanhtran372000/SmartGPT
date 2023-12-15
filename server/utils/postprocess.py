import re
import random

def replace_multiple_linebreaks(text):
    processed_text = re.sub(r'\n+', '\n', text)
    return processed_text

def replace_multiple_spaces(text):
    processed_text = re.sub(r'\s+', ' ', text)
    return processed_text

def remove_spaces_between_linebreaks(text):
    processed_text = re.sub(r'\n\s*\n', '\n\n', text)
    return processed_text

def replace_rn_with_n(text):
    processed_text = text.replace('\r\n', '\n')
    return processed_text

def postprocess_web_content(content):
    text = content.page_content
    text = replace_rn_with_n(text)
    text = replace_multiple_spaces(text)
    text = remove_spaces_between_linebreaks(text)
    text = replace_multiple_linebreaks(text)
    content.page_content = text
    return content

def random_crop_paragraph(long_paragraph, target_len=400):
    words = long_paragraph.split()
    
    if len(words) <= target_len:
        return long_paragraph

    start_index = random.randint(0, len(words) - target_len)
    cropped_words = words[start_index: start_index + target_len]
    cropped_paragraph = ' '.join(cropped_words)
    
    return cropped_paragraph