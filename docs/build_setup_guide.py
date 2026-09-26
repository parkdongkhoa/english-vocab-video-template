from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Flowable, PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(__file__).with_name("HUONG_DAN_CAI_DAT.pdf")
FONT_DIR = Path("C:/Windows/Fonts")

NAVY = colors.HexColor("#102B3F")
BLUE = colors.HexColor("#1F668A")
GREEN = colors.HexColor("#1B9B68")
PALE = colors.HexColor("#EEF6F3")
PALE_BLUE = colors.HexColor("#EEF4F8")
INK = colors.HexColor("#1C2C37")
MUTED = colors.HexColor("#586B77")
GOLD = colors.HexColor("#E6B44A")
RED = colors.HexColor("#A63A43")
WHITE = colors.white

pdfmetrics.registerFont(TTFont("GuideSans", str(FONT_DIR / "arial.ttf")))
pdfmetrics.registerFont(TTFont("GuideSans-Bold", str(FONT_DIR / "arialbd.ttf")))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="GuideTitle", fontName="GuideSans-Bold", fontSize=27, leading=33, textColor=NAVY, spaceAfter=8))
styles.add(ParagraphStyle(name="GuideSubtitle", fontName="GuideSans", fontSize=11, leading=16, textColor=MUTED, spaceAfter=13))
styles.add(ParagraphStyle(name="GuideH1", fontName="GuideSans-Bold", fontSize=19, leading=24, textColor=NAVY, spaceAfter=7))
styles.add(ParagraphStyle(name="GuideH2", fontName="GuideSans-Bold", fontSize=12, leading=16, textColor=BLUE, spaceBefore=4, spaceAfter=5))
styles.add(ParagraphStyle(name="GuideBody", fontName="GuideSans", fontSize=9.3, leading=14, textColor=INK, spaceAfter=6))
styles.add(ParagraphStyle(name="GuideSmall", fontName="GuideSans", fontSize=8, leading=11, textColor=MUTED, spaceAfter=3))
styles.add(ParagraphStyle(name="GuideCallout", fontName="GuideSans-Bold", fontSize=9.1, leading=13, textColor=NAVY))
styles.add(ParagraphStyle(name="GuideCode", fontName="Courier", fontSize=8.2, leading=11, textColor=WHITE))
styles.add(ParagraphStyle(name="GuideCenter", fontName="GuideSans-Bold", fontSize=10, leading=14, textColor=NAVY, alignment=TA_CENTER))


def p(text: str, style: str = "GuideBody") -> Paragraph:
    return Paragraph(text, styles[style])


def numbered_rows(rows: list[tuple[str, str]]) -> Table:
    data = []
    for index, (title, detail) in enumerate(rows, 1):
        badge = Table([[str(index)]], colWidths=[23], rowHeights=[23])
        badge.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), GREEN),
            ("TEXTCOLOR", (0, 0), (-1, -1), WHITE),
            ("FONTNAME", (0, 0), (-1, -1), "GuideSans-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOX", (0, 0), (-1, -1), 0, WHITE),
        ]))
        data.append([badge, [p(f"<b>{title}</b><br/>{detail}")]])
    table = Table(data, colWidths=[31, 470], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


class GitHubDownloadDiagram(Flowable):
    def __init__(self, width: float = 510, height: float = 226):
        super().__init__()
        self.width, self.height = width, height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        c.setFillColor(colors.HexColor("#F5F7F8"))
        c.roundRect(0, 0, w, h, 12, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.roundRect(0, h - 37, w, 37, 12, fill=1, stroke=0)
        c.rect(0, h - 37, w, 12, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("GuideSans-Bold", 10)
        c.drawString(16, h - 23, "GITHUB  /  ENGLISH-VOCAB-VIDEO-TEMPLATE")
        c.setFillColor(BLUE)
        c.setFont("GuideSans-Bold", 14)
        c.drawString(18, h - 68, "english-vocab-video-template")
        c.setFillColor(MUTED)
        c.setFont("GuideSans", 8.5)
        c.drawString(18, h - 86, "Bộ mẫu video tiếng Anh - Readme, skill, template và hướng dẫn")
        c.setFillColor(colors.HexColor("#E4E9EC"))
        c.roundRect(w - 132, h - 83, 112, 28, 7, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont("GuideSans-Bold", 9)
        c.drawCentredString(w - 76, h - 66, "Code  v")
        c.setStrokeColor(colors.HexColor("#D7E0E4"))
        c.line(16, h - 101, w - 16, h - 101)
        c.setFillColor(WHITE)
        c.roundRect(w - 227, 15, 205, 119, 8, fill=1, stroke=1)
        c.setStrokeColor(colors.HexColor("#D7E0E4"))
        c.setFillColor(INK)
        c.setFont("GuideSans", 9)
        c.drawString(w - 209, 111, "Open with GitHub Desktop")
        c.drawString(w - 209, 90, "Download ZIP")
        c.setFillColor(PALE)
        c.roundRect(w - 222, 76, 195, 28, 5, fill=1, stroke=0)
        c.setFillColor(GREEN)
        c.setFont("GuideSans-Bold", 9)
        c.drawString(w - 209, 87, "Download ZIP")
        c.setStrokeColor(GOLD)
        c.setLineWidth(2)
        c.line(w - 142, h - 78, w - 142, 145)
        c.line(w - 142, 145, w - 85, 137)
        c.setFillColor(NAVY)
        c.setFont("GuideSans-Bold", 8)
        c.drawString(18, 80, "1  Mở repo được chia sẻ")
        c.drawString(18, 60, "2  Bấm Code")
        c.drawString(18, 40, "3  Chọn Download ZIP")
        c.setFillColor(MUTED)
        c.setFont("GuideSans", 7.5)
        c.drawString(18, 20, "Minh họa giao diện; tên repo thực tế sẽ theo link phát hành.")


class PrerequisiteDiagram(Flowable):
    def __init__(self, width: float = 510, height: float = 125):
        super().__init__()
        self.width, self.height = width, height

    def draw(self):
        c = self.canv
        labels = [("01", "Codex Desktop", "Mở project và gọi skill"), ("02", "Python 3.12 x64", "Chạy script tạo video"), ("03", "FFmpeg", "Ghép hình và âm thanh")]
        gap = 10
        card_w = (self.width - gap * 2) / 3
        for i, (num, title, detail) in enumerate(labels):
            x = i * (card_w + gap)
            c.setFillColor(PALE_BLUE if i != 1 else PALE)
            c.roundRect(x, 7, card_w, self.height - 15, 10, fill=1, stroke=0)
            c.setFillColor(GREEN if i == 2 else BLUE)
            c.circle(x + 25, self.height - 34, 14, fill=1, stroke=0)
            c.setFillColor(WHITE)
            c.setFont("GuideSans-Bold", 8)
            c.drawCentredString(x + 25, self.height - 37, num)
            c.setFillColor(NAVY)
            c.setFont("GuideSans-Bold", 10)
            c.drawString(x + 17, self.height - 65, title)
            c.setFillColor(MUTED)
            c.setFont("GuideSans", 8)
            c.drawString(x + 17, self.height - 83, detail)
            c.setFillColor(GREEN)
            c.setFont("GuideSans-Bold", 7.5)
            c.drawString(x + 17, 23, "CÀI TRƯỚC KHI SETUP")


class FolderDiagram(Flowable):
    def __init__(self, width: float = 510, height: float = 190):
        super().__init__()
        self.width, self.height = width, height

    def draw(self):
        c = self.canv
        half = self.width / 2 - 7
        boxes = [
            (0, "TỪ FILE ZIP", ["english-vocab-video-template", "  codex-skill\\", "    english-vocab-10-keywords\\", "  video-template\\setup_windows.bat"]),
            (half + 14, "SAU KHI CÀI SKILL", ["%USERPROFILE%\\.codex\\skills\\", "  english-vocab-10-keywords\\", "    SKILL.md", "    agents\\openai.yaml"]),
        ]
        for x, title, lines in boxes:
            c.setFillColor(colors.HexColor("#F5F7F8"))
            c.roundRect(x, 5, half, self.height - 10, 9, fill=1, stroke=0)
            c.setFillColor(BLUE)
            c.setFont("GuideSans-Bold", 8.5)
            c.drawString(x + 13, self.height - 27, title)
            c.setFillColor(INK)
            c.setFont("Courier", 7.4)
            y = self.height - 52
            for line in lines:
                c.drawString(x + 13, y, line)
                y -= 23


class EnvDiagram(Flowable):
    def __init__(self, width: float = 510, height: float = 171):
        super().__init__()
        self.width, self.height = width, height

    def draw(self):
        c = self.canv
        c.setFillColor(NAVY)
        c.roundRect(0, 0, self.width, self.height, 10, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#9DE0BC"))
        c.setFont("GuideSans-Bold", 9)
        c.drawString(17, self.height - 23, "video-template\\.env  (chỉ lưu trên máy của bạn)")
        lines = [
            "ELEVENLABS_API_KEY=...key-cua-ban...",
            "ELEVENLABS_VOICE_ID=...voice-duoc-phep...",
            "ELEVENLABS_MODEL_ID=eleven_v3",
            "CIT_BASE_URL=http://127.0.0.1:8001",
            "CIT_VOICE_ID=...voice-id-duoc-cap...",
            "CIT_API_KEY=...neu-dich-vu-yeu-cau...",
        ]
        c.setFillColor(WHITE)
        c.setFont("Courier", 8.2)
        y = self.height - 46
        for line in lines:
            c.drawString(18, y, line)
            y -= 18
        c.setFillColor(colors.HexColor("#FFDA86"))
        c.setFont("GuideSans-Bold", 8)
        c.drawString(17, 13, "Không gửi file này lên GitHub hoặc cho người khác.")


class WorkflowDiagram(Flowable):
    def __init__(self, width: float = 510, height: float = 105):
        super().__init__()
        self.width, self.height = width, height

    def draw(self):
        c = self.canv
        labels = ["Kịch bản", "Voice", "Hình + render", "Xem MP4"]
        gap = 9
        box_w = (self.width - gap * 3) / 4
        for i, label in enumerate(labels):
            x = i * (box_w + gap)
            c.setFillColor([PALE_BLUE, PALE, colors.HexColor("#FFF5DF"), colors.HexColor("#FCEFF0")][i])
            c.roundRect(x, 21, box_w, 56, 9, fill=1, stroke=0)
            c.setFillColor([BLUE, GREEN, colors.HexColor("#B98520"), RED][i])
            c.setFont("GuideSans-Bold", 9)
            c.drawCentredString(x + box_w / 2, 45, label)
            if i < len(labels) - 1:
                c.setStrokeColor(MUTED)
                c.setLineWidth(1.6)
                c.line(x + box_w + 1, 49, x + box_w + gap - 2, 49)
                c.line(x + box_w + gap - 6, 53, x + box_w + gap - 2, 49)
                c.line(x + box_w + gap - 6, 45, x + box_w + gap - 2, 49)


def page_chrome(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setFillColor(NAVY)
    canvas.rect(0, height - 8, width, 8, fill=1, stroke=0)
    if doc.page > 1:
        canvas.setFillColor(MUTED)
        canvas.setFont("GuideSans-Bold", 7.5)
        canvas.drawString(40, height - 27, "ENGLISH VOCAB VIDEO STARTER  /  HƯỚNG DẪN CÀI ĐẶT")
    canvas.setStrokeColor(colors.HexColor("#D8E0E3"))
    canvas.line(40, 31, width - 40, 31)
    canvas.setFillColor(MUTED)
    canvas.setFont("GuideSans", 7.5)
    canvas.drawString(40, 19, "Bản hướng dẫn cho Windows 10/11 - Không chia sẻ khóa API")
    canvas.drawRightString(width - 40, 19, f"{doc.page}")
    canvas.restoreState()


def note_box(text: str, background=PALE) -> Table:
    table = Table([[p(text, "GuideCallout")]], colWidths=[500])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), background),
        ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#C8DCD2")),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return table


def code_box(text: str) -> Table:
    table = Table([[Preformatted(text, styles["GuideCode"])]], colWidths=[500])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("BOX", (0, 0), (-1, -1), 0.5, NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return table


def build() -> None:
    doc = SimpleDocTemplate(
        str(OUTPUT), pagesize=A4,
        rightMargin=42, leftMargin=42, topMargin=47, bottomMargin=43,
        title="Hướng dẫn cài đặt English Vocab Video Starter",
        author="English Vocab Video Starter",
    )
    story = []

    story += [Spacer(1, 10 * mm), p("ENGLISH VOCAB<br/>VIDEO STARTER", "GuideTitle"),
              p("Bộ khởi tạo video học tiếng Anh - cài một lần, tạo nhiều tập bằng Codex", "GuideSubtitle"),
              note_box("Dành cho người mới: tải ZIP, cài Python và FFmpeg, thêm skill vào Codex, cấu hình giọng đọc riêng rồi tạo video đầu tiên."),
              Spacer(1, 8 * mm), p("Bộ này có gì?", "GuideH2")]
    features = [
        [p("<b>Skill Codex</b><br/>Hướng dẫn viết nội dung và giữ nhịp video đã chốt.", "GuideBody"), p("<b>Project video</b><br/>Renderer Mode B, timing, trộn voice và nhạc.", "GuideBody")],
        [p("<b>Giọng song ngữ</b><br/>ElevenLabs v3 cho tiếng Anh, CIT Voice Studio cho tiếng Việt.", "GuideBody"), p("<b>PDF + bản chữ</b><br/>Làm theo hình hoặc mở hướng dẫn Markdown chi tiết.", "GuideBody")],
    ]
    table = Table(features, colWidths=[250, 250])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE_BLUE),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D6E1E5")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D6E1E5")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 11),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    story += [table, Spacer(1, 8 * mm), p("Luồng tổng quát", "GuideH2"), WorkflowDiagram(),
              Spacer(1, 5 * mm), p("Video mẫu đi kèm: samples/mode-b-silent-preview.mp4. Đây là bản render Mode B không có voice, dùng để kiểm tra bố cục, timer, cặp lựa chọn và icon trước khi cấu hình dịch vụ giọng đọc.", "GuideSmall"),
              p("Thời gian cài phụ thuộc vào máy tính và việc bạn đã có quyền truy cập dịch vụ giọng đọc hay chưa.", "GuideSmall"), PageBreak()]

    story += [p("1. Tải bộ mẫu từ GitHub", "GuideH1"),
              p("Bạn không cần cài Git để tải và sử dụng. Mở link repo do người chia sẻ cung cấp, sau đó tải ZIP.", "GuideBody"),
              GitHubDownloadDiagram(), Spacer(1, 4 * mm),
              numbered_rows([
                  ("Mở trang repo", "Dùng link GitHub của bộ mẫu mà người chia sẻ gửi cho bạn."),
                  ("Mở menu Code", "Nút Code nằm phía trên danh sách file."),
                  ("Tải ZIP và giải nén", "Chọn Download ZIP, rồi giải nén vào một thư mục dễ tìm như Documents."),
              ]), Spacer(1, 4 * mm),
              note_box("Nếu repo có mục Releases, tải file ZIP ở phiên bản mới nhất. Giữ thư mục đã giải nén ở vị trí cố định để Codex dễ mở.", PALE_BLUE), PageBreak()]

    story += [p("2. Cài ứng dụng cần thiết", "GuideH1"),
              p("Cài các ứng dụng nền trước khi chạy file setup trong project. Chỉ tải bộ cài từ trang chính thức.", "GuideBody"),
              PrerequisiteDiagram(), Spacer(1, 2 * mm),
              numbered_rows([
                  ("Codex Desktop", "Cài và đăng nhập ứng dụng Codex để mở skill và project video."),
                  ("Python 3.12 x64", "Trong phần cài đặt, bật tùy chọn thêm Python vào PATH."),
                  ("FFmpeg cho Windows", "Cài đầy đủ ffmpeg và ffprobe; thêm thư mục bin vào PATH."),
              ]), Spacer(1, 3 * mm), p("Kiểm tra trong cửa sổ PowerShell mới", "GuideH2"),
              code_box("py -3.12 --version\nffmpeg -version\nffprobe -version"),
              Spacer(1, 3 * mm), note_box("Nếu Windows không tìm thấy py, ffmpeg hoặc ffprobe, cài lại PATH rồi mở PowerShell mới trước khi tiếp tục."), PageBreak()]

    story += [p("3. Cài project và skill", "GuideH1"),
              numbered_rows([
                  ("Chạy setup", "Vào thư mục video-template và nhấp đúp setup_windows.bat. Script tạo môi trường Python riêng, cài thư viện, tạo .env mẫu và âm thanh tổng hợp ban đầu."),
                  ("Mở thư mục skills", "Trong File Explorer, dán %USERPROFILE%\\.codex\\skills vào thanh địa chỉ. Tạo thư mục skills nếu chưa có."),
                  ("Sao chép skill", "Copy thư mục codex-skill\\english-vocab-10-keywords vào .codex\\skills."),
                  ("Mở project", "Khởi động lại Codex Desktop, chọn Open Folder và mở thư mục video-template."),
              ]), Spacer(1, 5 * mm), FolderDiagram(), Spacer(1, 4 * mm),
              note_box("Không mở project trực tiếp bên trong file ZIP. Hãy giải nén trước rồi mới chạy setup_windows.bat.", PALE_BLUE), PageBreak()]

    story += [p("4. Cấu hình giọng đọc", "GuideH1"),
              p("Mỗi người dùng nhập tài khoản và endpoint của chính mình. Setup tạo file .env mẫu trong video-template.", "GuideBody"),
              EnvDiagram(), Spacer(1, 4 * mm),
              numbered_rows([
                  ("ElevenLabs", "Nhập API key và voice ID bạn được phép sử dụng. Mẫu đặt model là eleven_v3."),
                  ("CIT Voice Studio", "Nhập địa chỉ dịch vụ đang chạy và voice ID được cấp. Nếu CIT chạy trên máy này, có thể dùng 127.0.0.1; nếu ở máy khác, cần địa chỉ truy cập được từ mạng của bạn."),
                  ("Bảo vệ khóa", "Không gửi file .env qua chat, email hoặc GitHub. Chỉ commit .env.example đã để trống thông tin bí mật."),
              ]), Spacer(1, 3 * mm),
              note_box("API tạo giọng có thể tiêu thụ hạn mức hoặc phát sinh phí theo gói tài khoản. Kiểm tra mức sử dụng trước khi tạo nhiều tập.", colors.HexColor("#FFF5DF")), PageBreak()]

    story += [p("5. Tạo video đầu tiên", "GuideH1"),
              p("Trong Codex, yêu cầu tạo một tập mới bằng skill English Vocab - Listen & Choose. Ví dụ:", "GuideBody"),
              note_box("Dùng skill english-vocab-10-keywords. Tạo 5 cặp từ thông dụng về giao tiếp công sở; mỗi cặp có nghĩa tiếng Việt, phát âm, giải thích ngắn và hình minh họa có quyền sử dụng. Giữ thanh xanh co vào tâm, giải thích sau đáp án và CTA cuối video."),
              Spacer(1, 5 * mm), p("Luồng tạo tập", "GuideH2"), WorkflowDiagram(), Spacer(1, 4 * mm),
              p("Trước khi render, kiểm tra file ảnh có trong source_research\\reference_b_cutouts và tên file khớp reference_modes_data.py. Nếu chưa có ảnh, renderer sẽ hiển thị placeholder để bạn biết cần bổ sung.", "GuideBody"),
              p("Lệnh render thủ công", "GuideH2"),
              code_box(".\\.venv\\Scripts\\python.exe generate_reference_mode_b_hybrid_voice.py\n.\\.venv\\Scripts\\python.exe render_reference_mode_b_source_template.py --out preview_silent.mp4\n.\\.venv\\Scripts\\python.exe mix_reference_modes.py --mode b"),
              Spacer(1, 3 * mm), p("Video cuối nằm trong thư mục video-template. Mẫu đi kèm có 4 cặp; thêm cặp thứ 5 để có 10 lựa chọn và kiểm tra lại tổng thời lượng dưới 60 giây.", "GuideSmall"), PageBreak()]

    story += [p("6. Cập nhật và xử lý lỗi", "GuideH1"),
              p("Khi có phiên bản mới, mở mục Releases của repo và tải ZIP mới nhất. Nếu đã chỉnh sửa dữ liệu riêng, sao lưu trước khi thay file. Repo tạo từ template là bản riêng, không tự nhận cập nhật từ repo gốc.", "GuideBody"),
              p("Một số lỗi hay gặp", "GuideH2")]
    issues = [
        [p("Lỗi", "GuideCallout"), p("Cách xử lý", "GuideCallout")],
        [p("Không nhận Python/FFmpeg"), p("Kiểm tra PATH, mở PowerShell mới và chạy lại lệnh kiểm tra phiên bản.")],
        [p("CIT connection refused"), p("Khởi động CIT Voice Studio, kiểm tra URL/port và quyền truy cập mạng.")],
        [p("ElevenLabs 401/403"), p("Kiểm tra API key và voice ID trong .env. Không chụp hoặc gửi lộ khóa.")],
        [p("Thiếu hình minh họa"), p("Đặt ảnh được phép sử dụng vào đúng thư mục và đồng bộ filename trong dữ liệu.")],
        [p("Bản mới không tự cập nhật"), p("Tải Release mới, sao lưu nội dung riêng rồi cập nhật project.")],
    ]
    issue_table = Table(issues, colWidths=[155, 345])
    issue_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PALE),
        ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F8FAFB")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D7E0E4")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story += [issue_table, Spacer(1, 5 * mm),
              note_box("Khi nhờ hỗ trợ, chỉ gửi log đã xóa API key, token, email cá nhân và thông tin truy cập nội bộ.", colors.HexColor("#FFF5DF")),
              Spacer(1, 5 * mm), p("Tham khảo", "GuideH2"),
              p("<link href='https://www.python.org/downloads/windows/' color='#1F668A'>Python for Windows</link>  |  <link href='https://www.ffmpeg.org/download.html' color='#1F668A'>FFmpeg</link>  |  <link href='https://elevenlabs.io/docs/eleven-api/quickstart' color='#1F668A'>ElevenLabs API quickstart</link>", "GuideSmall"),
              Spacer(1, 3 * mm),
              p("Bản quyền phần mềm: đọc THIRD_PARTY_NOTICES.md. CIT Voice Studio là phần mềm bên ngoài do <link href='https://github.com/Cuongyd196/cit-voice-studio' color='#1F668A'>Cường IT phát triển</link>, dùng theo license và NOTICE của repo chính thức; template này chỉ kết nối tới endpoint của bạn và không phân phối CIT.", "GuideSmall")]

    doc.build(story, onFirstPage=page_chrome, onLaterPages=page_chrome)
    print(OUTPUT)


if __name__ == "__main__":
    build()
