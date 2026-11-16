def show_menu():
    print("\n===== 学习任务管理器 =====")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 完成任务")
    print("4. 删除任务")
    print("0. 退出")


def main():
    while True:
        show_menu()
        choice = input("请选择：").strip()

        if choice == "0":
            print("程序已退出")
            break

        if choice in {"1", "2", "3", "4"}:
            print("该功能将在后续版本实现")
        else:
            print("输入无效，请输入菜单中的编号")


if __name__ == "__main__":
    main()
