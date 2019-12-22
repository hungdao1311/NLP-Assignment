##Tổng quát về bài giải
Chương trình thực hiện các bước: 
###Dependency parser -> Grammatical relation -> Logical form -> Procedural semantic -> Database query

Ở mỗi bước, kết quả được lưu vào 1 cấu trúc dữ liệu trung gian (định nghĩa trong Models/data_type) sau đó được truyền sang xử lí ở bước tiếp theo
Chi tiết về việc sử dụng và truyền tiếp output có thể thấy ở file main.py

Database được định nghĩa trong file Database.py, dưới dạng list của các object

##Hướng dẫn khởi chạy
Câu hỏi input nằm trong file Input/questions.txt, có thể input nhiều câu hỏi cùng mẫu, cách biệt bởi kí tự xuống dòng '\\n'
Gõ lệnh `python3 main.py` ở cửa sổ command line, chương trình sẽ chạy và ghi output ra folder Ouput/output_*.txt 
Mỗi kết quả của mỗi câu hỏi được ngăn cách bằng một đường '-----------------'

