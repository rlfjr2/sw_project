import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('college_calcul.db')
cursor = conn.cursor()

# 지필고사 등급 테이블 생성
cursor.execute('''CREATE TABLE IF NOT EXISTS 지필고사_등급 (
                    id TEXT PRIMARY KEY,
                    중간고사1 REAL,
                    기말고사1 REAL,
                    중간고사2 REAL,
                    기말고사2 REAL,
                    중간고사3 REAL,
                    기말고사3 REAL,
                    중간고사4 REAL,
                    기말고사4 REAL,
                    중간고사5 REAL,
                    기말고사5 REAL,
                    중간고사6 REAL,
                    기말고사6 REAL
                )''')

# 사용자 정보 확인 함수
def check_user_id(id):
    cursor.execute("SELECT id FROM 사용자_정보 WHERE id=?", (id,))
    existing_id = cursor.fetchone()
    if existing_id:
        return True
    else:
        print("존재하지 않는 ID입니다. 다시 입력해주세요.")
        return False

# 사용자 정보 입력 받기 (존재하는 ID 확인)
while True:
    id = input("사용자 ID를 입력하세요: ")
    if check_user_id(id):
        break

# 중간 및 기말고사 성적 입력 받기
중간고사1 = float(input("1학년 1학기 중간고사 평균점수를 입력하세요: "))
기말고사1 = float(input("1학년 1학기 기말고사 평균점수를 입력하세요: "))
중간고사2 = float(input("1학년 2학기 중간고사 평균점수를 입력하세요: "))
기말고사2 = float(input("1학년 2학기 기말고사 평균점수를 입력하세요: "))
중간고사3 = float(input("2학년 1학기 중간고사 평균점수를 입력하세요: "))
기말고사3 = float(input("2학년 1학기 기말고사 평균점수를 입력하세요: "))
중간고사4 = float(input("2학년 2학기 중간고사 평균점수를 입력하세요: "))
기말고사4 = float(input("2학년 2학기 기말고사 평균점수를 입력하세요: "))
중간고사5 = float(input("3학년 1학기 중간고사 평균점수를 입력하세요: "))
기말고사5 = float(input("3학년 1학기 기말고사 평균점수를 입력하세요: "))
중간고사6 = float(input("3학년 2학기 중간고사 평균점수를 입력하세요: "))
기말고사6 = float(input("3학년 2학기 기말고사 평균점수를 입력하세요: "))

# 점수 테이블에 입력된 점수 업데이트
cursor.execute('''INSERT OR REPLACE INTO 지필고사_등급 (id, 중간고사1, 기말고사1, 중간고사2, 기말고사2, 중간고사3, 기말고사3,
                                                     중간고사4, 기말고사4, 중간고사5, 기말고사5, 중간고사6, 기말고사6)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
               (id, 중간고사1, 기말고사1, 중간고사2, 기말고사2, 중간고사3, 기말고사3, 중간고사4, 기말고사4,
                중간고사5, 기말고사5, 중간고사6, 기말고사6))

conn.commit()  # 변경사항 커밋

# 데이터베이스 연결 종료
conn.close()
