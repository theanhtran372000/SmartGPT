import os

from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

API_KEY = open('/home/asus/SmartGPT/server/save/keys/openai.txt', 'r').read().strip()
os.environ['OPENAI_API_KEY'] = API_KEY

template = open('/home/asus/SmartGPT/server/save/prompt_templates/extract_keyword.txt', 'r').read()
prompt = PromptTemplate(input_variables=["input", "default"], template=template)

chatgpt_chain = LLMChain(
    llm=ChatOpenAI(temperature=0),
    prompt=prompt
)

output = chatgpt_chain.predict(
    input="1. Bối cảnh thế giới và trong nước Năm 2021, kinh tế thế giới có sự phục hồi nhanh (tăng 6,1%). Quy mô thị trường tài chính Việt Nam tính theo thông lệ quốc tế đến hết tháng 9/2022 tương đương khoảng 295% GDP năm 2022; trong đó, hệ thống ngân hàng (tính bằng tổng tài sản các TCTD ngân hàng và phi ngân hàng) giữ vai trò chủ đạo, chiếm khoảng 64,7% quy mô tài sản hệ thống tài chính. Vốn hóa thị trường cổ phiếu, sau thời gian điều chỉnh, đã giảm xuống 22,1% so với mức 28,5% của năm 2021; dư nợ thị trường trái phiếu chiếm 12,5% và doanh thu phí bảo hiểm chiếm 0,7% quy mô hệ thống tài chính Việt Nam. Chính sách tiền tệ tiếp tục được NHNN điều hành linh hoạt, thận trọng trong xu hướng thắt chặt tiền tệ chung của thế giới. Trái ngược với giai đoạn 2020-2021, khi NHNN hạ lãi suất điều hành 3 đợt, mỗi đợt từ 0,5-1% nhằm giảm chi phí vốn, hỗ trợ doanh nghiệp và người dân trong bối cảnh dịch Covid-19. Sang năm 2022, trước xu hướng tăng lãi suất cơ bản của ngân hàng trung ương (NHTW) các nước như FED, ECB, Úc, Canada… có tỷ giá tăng mạnh (đồng USD tăng 12% so với đầu năm). Để ổn định tỷ giá USD/VND và kiểm soát lạm phát, NHNN đã thực hiện: (i) tăng lãi suất điều hành 2 đợt vào ngày ngày 22/9 và 24/10 (tương ứng với 2 đợt tăng lãi suất 75 điểm % của FED vào ngày 21/9 và 2/11), mỗi lần khoảng 1%, đưa dải lãi suất điều hành ngang với thời điểm trước đại dịch Covid-19; (ii) bán ngoại tệ để ổn định tỷ giá (từ đầu năm đến hết tháng 9/2022, NHNN đã bán khoảng 21 tỷ USD từ dự trữ ngoại hối để bình ổn thị trường ngoại hối; theo đó, dự trữ ngoại hối giảm xuống còn khoảng 89 tỷ USD); (iii) điều chỉnh biên độ tỷ giá giao ngay USD/VND vào ngày 17/10 từ mức +-3% lên +-5% trong bối cảnh USD tăng giá mạnh, tỷ giá giao dịch tại các NHTM ở trạng thái kịch trần biên độ; (iv) sử dụng lại công cụ tín phiếu lần đầu sau 2 năm để chủ động hút tiền về khi cần, đảm bảo chênh lệch lãi suất dương giữa VND và USD trên thị trường liên ngân hàng, tần suất bơm/hút mạnh dần bắt đầu từ quý 3/2022). Một vấn đề rất lớn của thị trường tài chính.",
    default="Không rõ"
)
print(output)