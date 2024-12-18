# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:36:13 2024

@author: Mirhotam
"""

import random

def generate_students():
    """30명의 학생 데이터를 무작위로 생성합니다."""
    students = []
    for _ in range(30):
        name = chr(random.randint(65, 90)) + chr(random.randint(65, 90))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"name": name, "age": age, "score": score})
    return students

def selection_sort(students, key, reverse=False):
    """선택 정렬 구현."""
    n = len(students)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if (students[j][key] < students[idx][key]) != reverse:
                idx = j
        students[i], students[idx] = students[idx], students[i]

def insertion_sort(students, key, reverse=False):
    """삽입 정렬 구현."""
    for i in range(1, len(students)):
        current = students[i]
        j = i - 1
        while j >= 0 and (students[j][key] > current[key]) != reverse:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = current

def quick_sort(students, key, reverse=False):
    """퀵 정렬 구현."""
    if len(students) <= 1:
        return students

    pivot = students[0]
    less = [x for x in students[1:] if (x[key] < pivot[key]) != reverse]
    greater = [x for x in students[1:] if (x[key] >= pivot[key]) != reverse]

    return quick_sort(less, key, reverse) + [pivot] + quick_sort(greater, key, reverse)

def counting_sort_for_radix(arr, key, exp):
    """기수 정렬에서 사용하는 계수 정렬."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for student in arr:
        index = (student[key] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i][key] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(students, key):
    """숫자 키를 기반으로 기수 정렬 구현."""
    max_value = max(students, key=lambda x: x[key])[key]
    exp = 1
    while max_value // exp > 0:
        counting_sort_for_radix(students, key, exp)
        exp *= 10

def display_students(students):
    """학생 정보를 출력."""
    print("\n이름\t나이\t성적")
    print("-" * 20)
    for student in students:
        print(f"{student['name']}\t{student['age']}\t{student['score']}")

def main():
    students = generate_students()
    print("초기 학생 데이터:")
    display_students(students)

    while True:
        print("\n메뉴:")
        print("1. 이름 기준 정렬")
        print("2. 나이 기준 정렬")
        print("3. 성적 기준 정렬")
        print("4. 종료")
        choice = input("메뉴를 선택하세요: ")

        if choice == "4":
            print("프로그램을 종료합니다.")
            break

        key_map = {"1": "name", "2": "age", "3": "score"}
        algo_map = {"1": selection_sort, "2": insertion_sort, "3": quick_sort, "4": radix_sort}

        key = key_map.get(choice)
        if not key:
            print("잘못된 선택입니다. 다시 시도하세요.")
            continue

        print("\n정렬 알고리즘:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        if key == "score":
            print("4. 기수 정렬")

        algo_choice = input("정렬 알고리즘을 선택하세요: ")
        algo = algo_map.get(algo_choice)

        if algo_choice == "4" and key != "score":
            print("기수 정렬은 성적 기준 정렬에서만 사용할 수 있습니다.")
            continue

        if algo is None:
            print("잘못된 정렬 알고리즘 선택입니다. 다시 시도하세요.")
            continue

        order = input("오름차순으로 정렬하시겠습니까? (yes/no): ").lower() == "no"

        if algo_choice == "4":
            algo(students, key)
        else:
            algo(students, key, reverse=order)

        print("\n정렬된 학생 데이터:")
        display_students(students)

if __name__ == "__main__":
    main()
