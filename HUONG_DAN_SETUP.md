# Hướng dẫn cài đặt English Vocab Video Starter

> Tài liệu này dành cho người chưa quen Git, Python hoặc dựng video bằng code. Bắt đầu bằng file PDF có hình ở `docs/HUONG_DAN_CAI_DAT.pdf`; bản này cung cấp chi tiết lệnh và xử lý lỗi.

## Bộ này làm gì?

- Skill giúp Codex tạo kịch bản tiếng Anh theo format Listen & Choose đã chốt.
- Project `video-template` dựng video dọc Mode B: hai lựa chọn, thanh xanh co vào tâm, đáp án, giải thích tiếng Việt và CTA cuối.
- Mẫu dữ liệu đi kèm có 4 cặp từ để minh họa. Muốn hiển thị 10 lựa chọn, dùng 5 cặp.
- Bản public không kèm ảnh trích từ video tham khảo, nhạc mẫu hoặc âm thanh chưa rõ quyền. Người dùng cần dùng ảnh do mình tạo hoặc có quyền sử dụng.

## Cần chuẩn bị

- Windows 10/11 và Codex Desktop đã cài/đăng nhập.
- Python 3.12 x64 và FFmpeg cho Windows.
- Tài khoản ElevenLabs và API key do chính bạn quản lý.
- CIT Voice Studio đang chạy ở địa chỉ bạn truy cập được, cùng voice ID được cấp. Nếu dịch vụ yêu cầu API key, bạn cần có key riêng.
- Internet khi cài thư viện và tạo giọng đọc.

Tải phần mềm từ trang chính thức: [Codex](https://openai.com/codex/), [Python for Windows](https://www.python.org/downloads/windows/), [FFmpeg downloads](https://www.ffmpeg.org/download.html), [ElevenLabs API keys](https://elevenlabs.io/app/settings/api-keys).

## 1. Tải và giải nén

Trên trang GitHub, bấm **Code → Download ZIP**. Giải nén vào một thư mục cố định, ví dụ `Documents\english-vocab-video-template`. Không chạy file bên trong ZIP.

Trong GitHub có thể có thêm mục **Releases**; nếu chủ repo phát hành một gói cài đặt ở đó, hãy tải file ZIP ở bản mới nhất.

## 2. Cài Python và FFmpeg

1. Cài Python 3.12 x64. Trong trình cài đặt, bật tùy chọn thêm Python vào PATH.
2. Cài một bản FFmpeg cho Windows và thêm thư mục `bin` của FFmpeg vào PATH.
3. Mở PowerShell mới và kiểm tra:

```powershell
py -3.12 --version
ffmpeg -version
ffprobe -version
```

Mỗi lệnh cần hiện phiên bản. Nếu không tìm thấy `ffmpeg`, mở lại PowerShell sau khi cập nhật PATH.

## 3. Cài project

Mở thư mục đã giải nén, vào `video-template`, rồi nhấp đúp `setup_windows.bat`. Script sẽ kiểm tra Python/FFmpeg, tạo `.venv`, cài thư viện, tạo `.env` mẫu và sinh nhạc nền/cue âm thanh tổng hợp ban đầu.

Nếu Windows hỏi có muốn chạy file hay không, kiểm tra file nằm trong thư mục project vừa tải rồi mới xác nhận.

## 4. Cài skill vào Codex

1. Mở File Explorer, dán `%USERPROFILE%\.codex\skills` vào thanh địa chỉ. Nếu thư mục `skills` chưa có, hãy tạo.
2. Sao chép nguyên thư mục `codex-skill\english-vocab-10-keywords` vào đó.
3. Kiểm tra có đường dẫn `%USERPROFILE%\.codex\skills\english-vocab-10-keywords\SKILL.md`.
4. Đóng và mở lại Codex Desktop.

## 5. Cấu hình giọng đọc riêng

1. Mở `video-template\.env` bằng Notepad. File được tạo từ `.env.example` khi chạy setup.
2. Dán API key ElevenLabs của bạn vào `ELEVENLABS_API_KEY`. Model mặc định trong mẫu là `eleven_v3`; hãy chọn voice ID bạn được phép sử dụng.
3. Điền `CIT_BASE_URL` và `CIT_VOICE_ID` theo dịch vụ được cấp. `http://127.0.0.1:8001` chỉ dùng khi CIT Voice Studio chạy trên chính máy này.
4. Nếu CIT yêu cầu xác thực, điền key vào `CIT_API_KEY`.
5. Lưu file `.env`.

Không gửi file `.env` cho người khác, không chụp màn hình lộ key và không đưa key vào GitHub. Người nhận ở ngoài mạng nội bộ không thể dùng địa chỉ riêng như `192.168.x.x` của máy anh; mỗi người cần một CIT endpoint mà máy họ truy cập được.

## 6. Chuẩn bị hình và nội dung

Mở project bằng Codex Desktop: **Open Folder → chọn `video-template`**. Dùng skill `english-vocab-10-keywords` và yêu cầu tạo chủ đề mới.

Trước khi render:

- Kiểm tra danh sách từ, nghĩa tiếng Việt, phát âm và đáp án trong `reference_modes_data.py`.
- Đặt một ảnh phù hợp cho mỗi lựa chọn vào `source_research\reference_b_cutouts\`, rồi giữ đúng tên file đã khai báo trong dữ liệu.
- Chỉ dùng ảnh tự tạo hoặc ảnh có quyền dùng phù hợp. Khi thiếu file, renderer sẽ hiện ô nhắc thêm hình; đó là placeholder, không phải hình cuối.
- Mẫu 4 cặp hiện tại tạo 8 lựa chọn. Thêm cặp thứ 5 để có 10 lựa chọn; đọc lại timing và CTA để đảm bảo video vẫn dưới 60 giây.

## 7. Tạo giọng, xem thử và xuất video

Tại thư mục `video-template`, chạy trong PowerShell:

```powershell
.\.venv\Scripts\python.exe generate_reference_mode_b_hybrid_voice.py
.\.venv\Scripts\python.exe render_reference_mode_b_source_template.py --out reference_mode_b_source_template_silent.mp4
.\.venv\Scripts\python.exe mix_reference_modes.py --mode b
```

File cuối là `reference_mode_b_source_template_hybrid.mp4`. Nếu đổi nội dung/độ dài CTA, tạo lại voice và kiểm tra thời lượng toàn video. Voice API có thể tiêu thụ hạn mức tài khoản.

## Xử lý lỗi thường gặp

- **Không tìm thấy `py`**: cài Python 3.12 x64, bật PATH và mở PowerShell mới.
- **Không tìm thấy `ffmpeg`/`ffprobe`**: thêm thư mục `bin` của FFmpeg vào PATH rồi mở PowerShell mới.
- **Connection refused với CIT**: kiểm tra dịch vụ đang chạy, đúng host/port và máy hiện tại truy cập được URL đó.
- **401/403**: kiểm tra API key/voice ID trong `.env`; không gửi key qua chat hỗ trợ.
- **Thiếu hình**: kiểm tra tên ảnh trong `reference_modes_data.py` khớp file trong `source_research\reference_b_cutouts\`.
- **Hết hạn mức**: kiểm tra gói ElevenLabs/CIT; tạo giọng có thể sử dụng hạn mức hoặc phát sinh chi phí theo tài khoản.

## Cập nhật template

Tải ZIP ở **Releases → bản mới nhất** rồi đọc ghi chú thay đổi. Nếu anh đã sửa project riêng, sao lưu nội dung của mình trước khi thay file từ phiên bản mới. Repo tạo từ template không tự nhận các cập nhật của repo gốc.

## Quyền sử dụng

Điều khoản cộng đồng nằm trong `LICENSE.md`: mọi người được miễn phí tải, cài và tự dùng bộ mã nguồn để tạo video; không được bán lại, đóng gói lại hoặc phân phối bộ mã nguồn như một sản phẩm riêng. Đây là điều khoản riêng, không phải giấy phép mã nguồn mở chuẩn. Ảnh, nhạc, giọng đọc, API và các tài nguyên bên thứ ba vẫn tuân theo giấy phép/điều khoản riêng của chúng.
