import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('college_calcul.db')
cursor = conn.cursor()

# 사용자 정보 테이블 생성 (한글 테이블 이름 사용)
cursor.execute('''CREATE TABLE IF NOT EXISTS 사용자_정보 (
                    id TEXT PRIMARY KEY,
                    이름 TEXT,
                    과학탐구1 TEXT,
                    과학탐구2 TEXT,
                    사회탐구1 TEXT,
                    사회탐구2 TEXT
                )''')

# 사용자 정보 및 선택과목 입력
def insert_user_info(id, 이름, 과학탐구1, 과학탐구2, 사회탐구1, 사회탐구2):
    cursor.execute("SELECT id FROM 사용자_정보 WHERE id=?", (id,))
    existing_id = cursor.fetchone()
    if existing_id:
        print("이미 존재하는 ID입니다. 다른 ID를 입력하세요.")
        return False
    else:
        cursor.execute('''INSERT INTO 사용자_정보 (id, 이름, 과학탐구1, 과학탐구2, 사회탐구1, 사회탐구2)
                          VALUES (?, ?, ?, ?, ?, ?)''', (id, 이름, 과학탐구1, 과학탐구2, 사회탐구1, 사회탐구2))
        conn.commit()
        print("사용자 정보가 성공적으로 입력되었습니다.")
        return True

# 사용자 정보 입력 받기 (중복된 ID 방지)
while True:
    id = input("ID를 입력하세요: ")
    if insert_user_info(id, '', '', '', '', ''):  # 이름과 선택과목은 여기서 입력하지 않음
        break

# 사용자 정보 입력 받기
이름 = input("이름을 입력하세요: ")
과학탐구1 = input("과학탐구 과목 1을 입력하세요: ")
과학탐구2 = input("과학탐구 과목 2를 입력하세요: ")
사회탐구1 = input("사회탐구 과목 1을 입력하세요: ")
사회탐구2 = input("사회탐구 과목 2를 입력하세요: ")

# 사용자 정보 업데이트
cursor.execute('''UPDATE 사용자_정보
                  SET 이름=?, 과학탐구1=?, 과학탐구2=?, 사회탐구1=?, 사회탐구2=?
                  WHERE id=?''', (이름, 과학탐구1, 과학탐구2, 사회탐구1, 사회탐구2, id))
conn.commit()

# 데이터베이스 연결 종료
conn.close()
