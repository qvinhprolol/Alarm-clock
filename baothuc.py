# Nhạc chuông báo thức để ở cùng directory với file phần mềm, nhạc phải theo đuôi .wav
import time
import winsound

# Thời gian người dùng muốn báo thức kêu kèm tùy chọn file nhạc
print("Đây là chương trình đặt báo thức, định dạng 24h ")
hours = int(input("Nhập giờ: "))
minutes = int(input("Nhập phút: "))
seconds = int(input("Nhập giây: "))
message = input("Nhập lời nhắn cho báo thức: ")
music_name = input("Nhập tên file nhạc chuông rồi thêm .wav (không cách): ")

# Đây là công thức tính thời gian còn lại (thời gian tới khi rung chuông)
hours_left = hours - time.localtime().tm_hour
minutes_left = minutes - time.localtime().tm_min
seconds_left = seconds - time.localtime().tm_sec

if seconds_left < 0:
    minutes_left = minutes_left - 1
    seconds_left = 60 + seconds_left 
if minutes_left < 0:
    hours_left = hours_left - 1
    minutes_left = 60 + minutes_left
if hours_left < 0:
    hours_left = hours_left + 24

# In kết quả thời gian còn lại
print()
print("Báo thức sẽ kêu sau: ", end="")
print(hours_left, "giờ ",end="")
print(minutes_left, "phút ",end="")
print(seconds_left, "giây")

# Cách dòng (nhìn cho nó đỡ sát vào nhau)
print()
print()
print()

# Code liên quan tới hoạt động của báo thức
while True:
    if time.localtime().tm_hour == hours and time.localtime().tm_min == minutes and time.localtime().tm_sec == seconds :
        print(message)
        winsound.PlaySound(music_name, winsound.SND_FILENAME)
        # Đây là phần hỏi người dùng có muốn ngủ tiếp không để báo thức lại báo tiếp (tiếng Anh gọi là snooze)
        print("Muốn ngủ thêm bao lâu?")
        choice = int(input("Nhập 0-không ngủ thêm, 1-thêm mặc định, 2-thêm tùy biến: "))
        if choice == 0:
            break
        if choice == 2:
            hours_added = int(input("Số giờ: "))
            minutes_added = int(input("Số phút: "))
            seconds_added = int(input("Số giây: "))
            
            hours = time.localtime().tm_hour + hours_added
            minutes = time.localtime().tm_min + minutes_added
            seconds = time.localtime().tm_sec + seconds_added
            continue
        else:
            minutes = time.localtime().tm_min + 5   # mặc định là 5 phút nhưng hiệu chỉnh được
            continue
    else:
        continue
