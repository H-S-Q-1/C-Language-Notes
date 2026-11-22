import json
from pathlib import Path


TASKS_FILE = Path(__file__).with_name("tasks.json")


def show_menu():
    print("\n===== 学习任务管理器 =====")
    print("1. 批量添加任务")
    print("2. 查看任务")
    print("3. 批量完成任务")
    print("4. 批量删除任务")
    print("0. 退出")


def load_tasks():
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        print(f"读取任务文件失败：{error}")
        return []

    if not isinstance(data, list):
        print("任务文件格式错误：根数据必须是列表")
        return []

    tasks = []

    for item in data:
        if (
            isinstance(item, dict)
            and isinstance(item.get("title"), str)
            and isinstance(item.get("completed"), bool)
        ):
            tasks.append({
                "title": item["title"],
                "completed": item["completed"],
            })

    return tasks


def save_tasks(tasks):
    try:
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)
        return True
    except OSError as error:
        print(f"保存任务失败：{error}")
        return False


def parse_task_numbers(text):
    normalized = text.replace("，", " ").replace(",", " ")
    parts = normalized.split()
    numbers = []

    for part in parts:
        try:
            number = int(part)
        except ValueError:
            print(f"忽略无效编号：{part}")
            continue

        if number <= 0:
            print(f"忽略无效编号：{number}")
            continue

        if number not in numbers:
            numbers.append(number)

    return numbers


def add_task(tasks):
    print("请输入任务名称，每行一条，直接输入空行结束：")

    new_tasks = []

    while True:
        title = input("> ").strip()

        if title == "":
            break

        new_tasks.append({
            "title": title,
            "completed": False,
        })

    if len(new_tasks) == 0:
        print("没有添加任务")
        return

    tasks.extend(new_tasks)

    if save_tasks(tasks):
        print(f"成功添加 {len(new_tasks)} 条任务")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("当前还没有任务")
        return

    print("\n任务列表：")

    for index, task in enumerate(tasks, start=1):
        status = "已完成" if task["completed"] else "未完成"
        print(f"{index}. [{status}] {task['title']}")


def complete_task(tasks):
    if len(tasks) == 0:
        print("当前还没有任务")
        return

    show_tasks(tasks)

    text = input("请输入任务编号，用空格或逗号分隔：")
    numbers = parse_task_numbers(text)

    if len(numbers) == 0:
        print("没有有效的任务编号")
        return

    completed_count = 0
    already_completed = 0
    invalid_numbers = []

    for task_number in numbers:
        if task_number < 1 or task_number > len(tasks):
            invalid_numbers.append(task_number)
            continue

        task = tasks[task_number - 1]

        if task["completed"]:
            already_completed += 1
            continue

        task["completed"] = True
        completed_count += 1
        print(f"任务已完成：{task['title']}")

    if completed_count > 0 and save_tasks(tasks):
        print(f"本次完成 {completed_count} 条任务")

    if already_completed > 0:
        print(f"跳过 {already_completed} 条已完成任务")

    if len(invalid_numbers) > 0:
        print("不存在的任务编号：", end="")
        print(*invalid_numbers, sep=" ")


def delete_task(tasks):
    if len(tasks) == 0:
        print("当前还没有任务")
        return

    show_tasks(tasks)

    text = input("请输入任务编号，用空格或逗号分隔：")
    numbers = parse_task_numbers(text)

    if len(numbers) == 0:
        print("没有有效的任务编号")
        return

    valid_numbers = [
        number for number in numbers
        if 1 <= number <= len(tasks)
    ]
    invalid_numbers = [
        number for number in numbers
        if number < 1 or number > len(tasks)
    ]

    if len(valid_numbers) == 0:
        print("没有可以删除的任务")

        if len(invalid_numbers) > 0:
            print("不存在的任务编号：", end="")
            print(*invalid_numbers, sep=" ")
        return

    for task_number in sorted(valid_numbers, reverse=True):
        deleted_task = tasks.pop(task_number - 1)
        print(f"任务已删除：{deleted_task['title']}")

    if save_tasks(tasks):
        print(f"本次删除 {len(valid_numbers)} 条任务")

    if len(invalid_numbers) > 0:
        print("不存在的任务编号：", end="")
        print(*invalid_numbers, sep=" ")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("请选择：").strip()

        if choice == "0":
            print("程序已退出")
            break
        elif choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        else:
            print("输入无效，请输入菜单中的编号")


if __name__ == "__main__":
    main()