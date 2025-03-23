import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Heiti TC'  # 顯示中文字型
plt.rcParams['axes.unicode_minus'] = False  # 避免負號顯示錯誤

def get_student_data():
    """ 取得學生成績資料 """
    students = []
    n = int(input("請輸入學生人數: "))  # 使用者輸入學生數量

    for i in range(n):
        print(f"\n請輸入第 {i+1} 位學生的資料:")
        name = input("姓名: ")
        math = float(input("數學成績: "))
        english = float(input("英文成績: "))
        programming = float(input("程式設計成績: "))

        total = math + english + programming
        average = total / 3

        # 根據平均分數給等級
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        students.append({"name": name, "math": math, "english": english, 
                         "programming": programming, "total": total, 
                         "average": average, "grade": grade})

    return students

def show_results(students):
    """ 顯示所有學生的成績 """
    print("\n📊 學生成績分析 📊")
    print("-----------------------------------------------------")
    print("姓名       數學    英文    程式設計   總分   平均   等級")
    print("-----------------------------------------------------")

    for s in students:
        print(f"{s['name']:8} {s['math']:6.1f} {s['english']:6.1f} {s['programming']:8.1f} {s['total']:6.1f} {s['average']:6.1f}  {s['grade']}")

    print("-----------------------------------------------------")

def find_top_student(students):
    """ 找出總分最高的學生 """
    top_student = max(students, key=lambda s: s["total"])
    print(f"\n🏆 最高分學生: {top_student['name']} (總分: {top_student['total']:.1f}, 平均: {top_student['average']:.1f}, 等級: {top_student['grade']})")

def plot_scores(students):
    """ 繪製成績條狀圖 """
    names = [s["name"] for s in students]
    math_scores = [s["math"] for s in students]
    english_scores = [s["english"] for s in students]
    programming_scores = [s["programming"] for s in students]

    bar_width = 0.25
    index = range(len(students))

    plt.figure(figsize=(10, 5))
    plt.bar(index, math_scores, bar_width, label="數學")
    plt.bar([i + bar_width for i in index], english_scores, bar_width, label="英文")
    plt.bar([i + bar_width*2 for i in index], programming_scores, bar_width, label="程式設計")

    plt.xlabel("學生")
    plt.ylabel("分數")
    plt.title("學生成績比較")
    plt.xticks([i + bar_width for i in index], names)
    plt.legend()
    plt.show()

# 主程式
students = get_student_data()
show_results(students)
find_top_student(students)
plot_scores(students)