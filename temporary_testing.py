import pandas as pd
import numpy as np
from datetime import datetime, timedelta

file_path = 'data/comments.csv'
df = pd.read_csv(file_path)

# Thời gian bắt đầu và kết thúc
start_date = datetime(2024, 7, 1)
end_date = datetime(2024, 11, 6)

# Hàm tạo thời điểm thời gian trong khoảng start_date và end_date
def input_date(start, end):
    delta = end - start
    random_days = np.random.randint(0, delta.days + 1)
    return start + timedelta(days=random_days)

df['timestamp'] = [input_date(start_date, end_date) for _ in range(len(df))]

df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce').dt.strftime('%d/%m/%Y')

# Output csv
output_file_path = 'data/comments_new.csv'
df.to_csv(output_file_path)