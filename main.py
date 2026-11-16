def show_menu():
    print("\n===== 学习任务管理器 =====")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 完成任务")
    print("4. 删除任务")
    print("0. 退出")


def add_task(tasks):
    title = input("请输入任务名称：").strip()

    if title == "":
        print("任务名称不能为空")
        return

    task = {
        "title": title,
        "completed": False,
    }

    tasks.append(task)
    print("任务添加成功")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("当前还没有任务")
        return

    print("\n任务列表：")

    for index, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "已完成"
        else:
            status = "未完成"

        print(f"{index}. [{status}] {task['title']}")


def complete_task(tasks):
    if len(tasks) == 0:
        print("当前还没有任务")
        return

    show_tasks(tasks)

    try:
        task_number = int(input("请输入要完成的任务编号：").strip())
    except ValueError:
        print("任务编号必须是整数")
        return

    if task_number < 1 or task_number > len(tasks):
        print("任务编号不存在")
        return

    task = tasks[task_number - 1]

    if task["completed"]:
        print("这个任务已经完成了")
        return

    task["completed"] = True
    print(f"任务已完成：{task['title']}")


def delete_task(tasks):
    if len(tasks) == 0:
        print("当前还没有任务")
        return

    show_tasks(tasks)

    try:
        task_number = int(input("请输入要删除的任务编号：").strip())
    except ValueError:
        print("任务编号必须是整数")
        return

    if task_number < 1 or task_number > len(tasks):
        print("任务编号不存在")
        return

    deleted_task = tasks.pop(task_number - 1)
    print(f"任务已删除：{deleted_task['title']}")


def main():
    tasks = []

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