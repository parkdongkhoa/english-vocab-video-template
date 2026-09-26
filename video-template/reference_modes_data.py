from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent


MODE_A_ITEMS = [
    {"vi": "Bạn có thể nói lại không?", "en": "Could you say that again?", "clue": "Khi bạn chưa nghe rõ", "pron": "/kʊd juː seɪ ðæt əˈɡen/", "example": "Could you say that again?", "icon": "repeat"},
    {"vi": "Tôi chưa nghe kịp.", "en": "I didn't catch that.", "clue": "Khi bỏ lỡ một ý", "pron": "/aɪ ˈdɪd.ənt kætʃ ðæt/", "example": "I didn't catch that.", "icon": "ear"},
    {"vi": "Cho tôi một giây.", "en": "Give me a second.", "clue": "Khi cần thêm chút thời gian", "pron": "/ɡɪv miː ə ˈsek.ənd/", "example": "Give me a second.", "icon": "hourglass"},
    {"vi": "Để tôi kiểm tra.", "en": "Let me check.", "clue": "Khi cần xác nhận thông tin", "pron": "/let miː tʃek/", "example": "Let me check.", "icon": "check"},
    {"vi": "Điều đó hợp lý.", "en": "That makes sense.", "clue": "Khi bạn đồng ý với ý giải thích", "pron": "/ðæt meɪks sens/", "example": "That makes sense.", "icon": "bulb"},
    {"vi": "Tôi vẫn chưa chắc.", "en": "I'm not sure yet.", "clue": "Khi bạn chưa có quyết định", "pron": "/aɪm nɒt ʃɔː jet/", "example": "I'm not sure yet.", "icon": "question"},
    {"vi": "Còn tùy.", "en": "It depends.", "clue": "Khi câu trả lời phụ thuộc tình huống", "pron": "/ɪt dɪˈpendz/", "example": "It depends.", "icon": "branch"},
    {"vi": "Tôi đang trên đường.", "en": "I'm on my way.", "clue": "Khi bạn đang di chuyển tới nơi hẹn", "pron": "/aɪm ɒn maɪ weɪ/", "example": "I'm on my way.", "icon": "way"},
    {"vi": "Ý bạn là gì?", "en": "What do you mean?", "clue": "Khi cần hỏi lại ý người khác", "pron": "/wɒt duː juː miːn/", "example": "What do you mean?", "icon": "meaning"},
    {"vi": "Giữ liên lạc nhé.", "en": "Let's stay in touch.", "clue": "Khi kết thúc một cuộc trò chuyện", "pron": "/lets steɪ ɪn tʌtʃ/", "example": "Let's stay in touch.", "icon": "connect"},
]


MODE_B_INTRO_TEXT = "Nghe từ tiếng Anh và chọn từ đúng."
MODE_B_CTA_TEXT = "Lưu video này, luyện lại các cặp từ và theo dõi kênh để học tiếng Anh mỗi ngày nhé."


MODE_B_CARDS = [
        {"left": "banana", "right": "bandana", "target": "banana", "audio": "", "meaning": "banana /bəˈnænə/ · bandana /bænˈdænə/", "explanation": "Banana là quả chuối; bandana là khăn hoặc băng đô đội đầu.", "left_asset": "banana.png", "right_asset": "bandana.png"},
        {"left": "quantity", "right": "quality", "target": "quality", "audio": "", "meaning": "quantity /ˈkwɒntəti/ · quality /ˈkwɒləti/", "explanation": "Quantity là số lượng; quality là chất lượng.", "left_asset": "quantity.png", "right_asset": "quality.png"},
        {"left": "finally", "right": "family", "target": "family", "audio": "", "meaning": "finally /ˈfaɪnəli/ · family /ˈfæməli/", "explanation": "Finally là cuối cùng; family là gia đình.", "left_asset": "finally.png", "right_asset": "family.png"},
        {"left": "document", "right": "monument", "target": "document", "audio": "", "meaning": "document /ˈdɒkjʊmənt/ · monument /ˈmɒnjʊmənt/", "explanation": "Document là tài liệu; monument là tượng đài hoặc công trình kỷ niệm.", "left_asset": "document.png", "right_asset": "monument.png"},
]
