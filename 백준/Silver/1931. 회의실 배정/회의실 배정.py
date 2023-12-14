from collections import deque


def main():
    num_of_meetings = int(input())
    meetings = []
    for i in range(num_of_meetings):
        meeting = map(int, input().split())
        meetings.append(list(meeting))

    # print(meetings)

    meetings = deque(sorted(meetings, key=lambda x: (x[1], x[0])))

    prev_meeting = meetings.popleft()
    count = 1
    while meetings:
        meeting = meetings.popleft()

        if meeting[0] >= prev_meeting[1]:
            prev_meeting = meeting
            count += 1

    print(count)


if __name__ == "__main__":
    main()
