import requests
from bs4 import BeautifulSoup

# 학교 홈페이지에서 급식 메뉴 페이지의 URL
url = "http://school.gyo6.net/phds/135976/food"

# 웹 페이지에 요청을 보내고 HTML 응답을 받습니다.
response = requests.get(url)
html = response.text

# BeautifulSoup을 사용하여 HTML을 파싱합니다.
soup = BeautifulSoup(html, "html.parser")

# 필요한 급식 정보를 추출합니다.
# 예시: 테이블에서 아침, 점심, 저녁 메뉴를 추출하는 코드
table = soup.find("table")
rows = table.find_all("tr")[1:]  # 첫 번째 행은 헤더이므로 제외합니다.

menu_data = []
for row in rows:
    columns = row.find_all("td")
    menu = [column.get_text().strip() for column in columns]
    menu_data.append(menu)

# 업데이트할 HTML 코드 생성
updated_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Document</title>
<style>
body {

background-color: #f8eaf2; /* 핑크색 배경 */

font-family: Arial, sans-serif; /* 폰트 설정 */

margin: 0; /* 바깥 여백 제거 */

padding: 20px; /* 안쪽 여백 설정 */

}

h1 {

color: #e91e63; /* 핑크색 글자 */

text-align: center; /* 가운데 정렬 */

margin-bottom: 20px; /* 아래 여백 추가 */

}

h3 {

color: #e91e63; /* 핑크색 글자 */

text-align: center; /* 가운데 정렬 */

}

img {

display: block; /* 이미지를 블록 요소로 설정하여 가운데 정렬 */

margin: 0 auto; /* 가운데 정렬 */

max-width: 100%; /* 이미지의 최대 너비 설정 */

height: auto; /* 이미지의 높이 자동 조정 */

border-radius: 10px; /* 이미지에 둥근 테두리 추가 */

box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 그림자 효과 추가 */

margin-top: 20px; /* 위쪽 여백 추가 */

}

table {

border-collapse: collapse; /* 테이블 테두리 겹치게 하기 */

width: 80%; /* 테이블 너비 설정 */

margin: 0 auto; /* 테이블 가운데 정렬 */

}

th, td {

border: 1px solid #e91e63; /* 셀 테두리 설정 */

padding: 10px; /* 셀 안쪽 여백 설정 */

text-align: center; /* 셀 내용 가운데 정렬 */

}

th {

background-color: #f8eaf2; /* 헤더 셀 배경색 설정 */

color: #e91e63; /* 헤더 셀 글자색 설정 */

}
</style>
</head>
<body>
<h1>기숙사 이슈</h1>
<h3>야간집회 폼 미쳤다</h3>
<img src="https://www.kyongbuk.co.kr/news/photo/202001/2028511_438827_4357.jpg" alt="박원필" width="500">
<h3>오늘의 급식</h3>
<table>
<tr>
<th>아침</th>
<th>점심</th>
<th>저녁</th>
</tr>
<tr>
<td>{}</td>
<td>{}</td>
<td>{}</td>
</tr>
</table>
</body>
</html>
""".format(menu_data[0][0], menu_data[0][1], menu_data[0][2])

# 업데이트된 HTML 파일 저장 혹은 웹 페이지에 삽입하여 화면에 표시합니다.
# 자세한 구현 방법은 사용하는 프레임워크나 환경에 따라 다를 수 있습니다.
