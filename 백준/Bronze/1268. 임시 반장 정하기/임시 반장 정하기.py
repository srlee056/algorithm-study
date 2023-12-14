def main():
    num_of_students = int(input())

    groups = []

    for i in range(num_of_students):
        group = map(int, input().split())

        groups.append(list(group))

    common_groups = {}
    for year_idx in range(5):
        temp_group_dict = {}
        for student_idx in range(num_of_students):
            group_num = groups[student_idx][year_idx]
            temp_group_dict[group_num] = temp_group_dict.get(group_num, [])
            temp_group_dict[group_num].append(student_idx)

        for group_num, students in temp_group_dict.items():
            for student in students:
                common_groups[student] = common_groups.get(student, set())
                common_groups[student].update(students)
    max_len = max(len(v) for v in common_groups.values())
    max_len_students = [k for k, v in common_groups.items() if len(v) == max_len]

    max_len_students.sort()

    print(max_len_students[0] + 1)


if __name__ == "__main__":
    main()
