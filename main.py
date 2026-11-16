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
        elif choice in {"3", "4"}:
            print("该功能将在后续版本实现")
        else:
            print("输入无效，请输入菜单中的编号")


if __name__ == "__main__":
    main()