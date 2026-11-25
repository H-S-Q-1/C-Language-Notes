import csv
import json
from datetime import datetime
from pathlib import Path


TASKS_FILE = Path(__file__).with_name("tasks.json")
EXPORT_FILE = Path(__file__).with_name("task_export.csv")
DUE_TIME_FORMAT = "%Y-%m-%d %H:%M"


def show_menu():
    print("\n===== 学习任务管理器 =====")
    print("1. 批量添加任务")
    print("2. 查看任务")
    print("3. 批量完成任务")
    print("4. 批量删除任务")
    print("5. 搜索任务")
    print("6. 按状态筛选")
    print("7. 修改任务名称")
    print("8. 清空已完成任务")
    print("9. 查看任务统计")
    print("10. 导出任务记录")
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
            created_at = item.get("created_at")

            if not isinstance(created_at, str) or created_at == "":
                created_at = "未知"

            due_at = item.get("due_at")

            if not isinstance(due_at, str):
                due_at = ""
            else:
                try:
                    datetime.strptime(due_at, DUE_TIME_FORMAT)
                except ValueError:
                    due_at = ""

            tasks.append({
                "title": item["title"],
                "completed": item["completed"],
                "created_at": created_at,
                "due_at": due_at,
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
    print("请输入任务，每行一条，直接输入空行结束。")
    print("格式：任务名称 | 截止时间（截止时间可省略）")
    print("截止时间格式：YYYY-MM-DD HH:MM")

    new_tasks = []

    while True:
        text = input("> ").strip()

        if text == "":
            break

        if "|" in text:
            title, due_at = text.split("|", 1)
            title = title.strip()
            due_at = due_at.strip()
        else:
            title = text
            due_at = ""

        if title == "":
            print("任务名称不能为空，请重新输入")
            continue

        if due_at != "":
            try:
                datetime.strptime(due_at, DUE_TIME_FORMAT)
            except ValueError:
                print("截止时间格式错误，本条任务未添加")
                print("正确格式示例：2026-12-01 18:30")
                continue

        new_tasks.append({
            "title": title,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "due_at": due_at,
        })

    if len(new_tasks) == 0:
        print("没有添加任务")
        return

    tasks.extend(new_tasks)

    if save_tasks(tasks):
        print(f"成功添加 {len(new_tasks)} 条任务")


def is_overdue(task):
    if task["completed"]:
        return False

    due_at = task.get("due_at", "")

    if due_at == "":
        return False

    try:
        deadline = datetime.strptime(due_at, DUE_TIME_FORMAT)
    except ValueError:
        return False

    return datetime.now() > deadline


def print_task(index, task):
    status = "已完成" if task["completed"] else "未完成"
    created_at = task.get("created_at", "未知")
    due_at = task.get("due_at", "")

    print(f"{index}. [{status}] {task['title']}")
    print(f"   创建时间：{created_at}")

    if due_at == "":
        print("   截止时间：未设置")
    elif is_overdue(task):
        print(f"   截止时间：{due_at}（已逾期）")
    else:
        print(f"   截止时间：{due_at}")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("当前还没有任务")
        return

    print("\n任务列表：")

    for index, task in enumerate(tasks, start=1):
        print_task(index, task)


def search_task(tasks):
    if len(tasks) == 0:
        print("当前还没有任务")
        return

    keyword = input("请输入任务关键词：").strip()

    if keyword == "":
        print("搜索关键词不能为空")
        return

    keyword_lower = keyword.casefold()
    matches = []

    for index, task in enumerate(tasks, start=1):
        if keyword_lower in task["title"].casefold():
            matches.append((index, task))

    if len(matches) == 0:
        print(f"没有找到包含“{keyword}”的任务")
        return

    print(f"\n找到 {len(matches)} 条匹配任务：")

    for index, task in matches:
        print_task(index, task)


def filter_tasks(tasks):
    if len(tasks) == 0:
        print("当前还没有任务")
        return

    print("\n请选择筛选状态：")
    print("1. 未完成任务")
    print("2. 已完成任务")
    print("3. 已逾期任务")
    choice = input("请选择：").strip()

    if choice == "1":
        title = "未完成任务"
        matches = [
            (index, task)
            for index, task in enumerate(tasks, start=1)
            if not task["completed"]
        ]
    elif choice == "2":
        title = "已完成任务"
        matches = [
            (index, task)
            for index, task in enumerate(tasks, start=1)
            if task["completed"]
        ]
    elif choice == "3":
        title = "已逾期任务"
        matches = [
            (index, task)
            for index, task in enumerate(tasks, start=1)
            if is_overdue(task)
        ]
    else:
        print("筛选项无效")
        return

    if len(matches) == 0:
        print(f"没有{title}")
        return

    print(f"\n{title}：")

    for index, task in matches:
        print_task(index, task)


def edit_task(tasks):
    if len(tasks) == 0:
        print("当前还没有任务")
        return

    show_tasks(tasks)

    try:
        task_number = int(input("请输入要修改的任务编号：").strip())
    except ValueError:
        print("任务编号必须是整数")
        return

    if task_number < 1 or task_number > len(tasks):
        print("任务编号不存在")
        return

    task = tasks[task_number - 1]
    print(f"当前任务名称：{task['title']}")

    new_title = input("请输入新的任务名称，直接回车取消：").strip()

    if new_title == "":
        print("已取消修改")
        return

    if new_title == task["title"]:
        print("任务名称没有变化")
        return

    old_title = task["title"]
    task["title"] = new_title

    if save_tasks(tasks):
        print(f"任务名称已修改：{old_title} -> {new_title}")


def clear_completed_tasks(tasks):
    if len(tasks) == 0:
        print("当前还没有任务")
        return

    completed_count = sum(
        1 for task in tasks
        if task["completed"]
    )

    if completed_count == 0:
        print("当前没有已完成任务")
        return

    confirm = input(
        f"确定清空 {completed_count} 条已完成任务吗？输入 y 确认："
    ).strip().lower()

    if confirm != "y":
        print("已取消清空操作")
        return

    tasks[:] = [
        task for task in tasks
        if not task["completed"]
    ]

    if save_tasks(tasks):
        print(f"已清空 {completed_count} 条已完成任务")


def show_statistics(tasks):
    total = len(tasks)

    if total == 0:
        print("当前还没有任务")
        return

    completed_count = sum(
        1 for task in tasks
        if task["completed"]
    )
    pending_count = total - completed_count
    overdue_count = sum(
        1 for task in tasks
        if is_overdue(task)
    )
    completion_rate = completed_count / total * 100

    print("\n===== 任务统计 =====")
    print(f"任务总数：{total}")
    print(f"已完成：{completed_count}")
    print(f"未完成：{pending_count}")
    print(f"已逾期：{overdue_count}")
    print(f"完成率：{completion_rate:.1f}%")


def export_tasks(tasks):
    if len(tasks) == 0:
        print("当前还没有任务，无法导出")
        return

    try:
        with EXPORT_FILE.open(
            "w",
            encoding="utf-8-sig",
            newline=""
        ) as file:
            writer = csv.writer(file)
            writer.writerow([
                "序号",
                "任务名称",
                "状态",
                "创建时间",
                "截止时间",
                "是否逾期",
            ])

            for index, task in enumerate(tasks, start=1):
                status = "已完成" if task["completed"] else "未完成"
                due_at = task.get("due_at", "") or "未设置"
                overdue = "是" if is_overdue(task) else "否"

                writer.writerow([
                    index,
                    task["title"],
                    status,
                    task.get("created_at", "未知"),
                    due_at,
                    overdue,
                ])
    except OSError as error:
        print(f"导出任务失败：{error}")
        return

    print(f"任务已导出到：{EXPORT_FILE}")


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
        elif choice == "5":
            search_task(tasks)
        elif choice == "6":
            filter_tasks(tasks)
        elif choice == "7":
            edit_task(tasks)
        elif choice == "8":
            clear_completed_tasks(tasks)
        elif choice == "9":
            show_statistics(tasks)
        elif choice == "10":
            export_tasks(tasks)
        else:
            print("输入无效，请输入菜单中的编号")


if __name__ == "__main__":
    main()
