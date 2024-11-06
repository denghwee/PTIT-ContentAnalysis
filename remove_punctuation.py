import pandas as pd
import string

# Đọc file CSV
df = pd.read_csv('C:/Users/ntrgi/Desktop/PTIT-ContentAnalysis-master/data/comments.csv')

# Tạo bộ dịch để loại bỏ các ký tự không phải chữ và một số ký tự trắng
translator = str.maketrans('', '', string.punctuation + '\t\n')

# Loại bỏ dấu nháy kép từ các bình luận
df['comment'] = df['comment'].str.replace('"', '', regex=False)

# Loại bỏ các ký tự không phải chữ và giữ lại khoảng trắng
df['comment'] = df['comment'].apply(lambda x: ''.join(e for e in x if e.isalnum() or e.isspace()))

# Chuyển đổi tất cả các bình luận thành chữ thường
df['comment'] = df['comment'].apply(lambda x: x.lower())

# Áp dụng bộ dịch để loại bỏ các ký tự không mong muốn
df['comment'] = df['comment'].apply(lambda x: x.translate(translator))

# Loại bỏ các hàng có cột 'comments' rỗng hoặc NaN
df = df[df['comment'].str.strip().astype(bool)]

# Lưu các bình luận đã xử lý vào một file CSV mới
df[['comment']].to_csv('./data/new_cmt.csv', index=False)